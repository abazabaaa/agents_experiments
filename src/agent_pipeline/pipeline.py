"""Pipeline orchestration entrypoints."""

from __future__ import annotations

import json
import logging
import os
import shutil
import traceback
from datetime import datetime
from pathlib import Path
from typing import Awaitable, Callable, Iterable
from uuid import uuid4

import httpx
import trio
import trio_asyncio
from agents import set_default_openai_client
from openai import AsyncOpenAI

from .agents.registry import AgentRegistry
from .config import PipelineConfig
from .limiters import LimiterPool
from .logging import StructuredLogger
from .stages.ingest import ingest_documents, load_documents
from .stages.markdown import markdown_supervisor
from .stages.monitor import close_when_both_done, close_when_done, monitor_channels, watch_completion
from .stages.naming import naming_supervisor
from .stages.notebook import notebook_supervisor
from .stages.review import review_supervisor
from .stages.router import router_supervisor
from .stages.types import CompletionCounter, DocTask, NamedDoc, ProcessedDoc, ReviewedDoc, WorkItem
from .stages.writer import writer_stage

RecordFailureFn = Callable[[int, str, str, Exception], Awaitable[None]]


class Pipeline:
    """High-level orchestration for the agent document processing workflow."""

    def __init__(self, config: PipelineConfig, *, quiet: bool = False) -> None:
        self.config = config
        self.quiet = quiet
        log_path, run_dir = self._prepare_run_artifacts()
        self.run_dir = run_dir
        self.config.log_file = log_path
        self.logger = StructuredLogger(quiet=quiet, verbose_path=log_path)
        self.logger.info(f"Pipeline log directory: {self.run_dir}")
        if self.config.path.exists():
            self.logger.info(f"Configuration file: {self.config.path}")
        self.registry = AgentRegistry(config)
        self.limiter_pool = LimiterPool(
            overall_capacity=config.concurrency.agent_thread_limit,
            model_limits=config.concurrency.model_limits,
        )
        self.failures: list[dict[str, object]] = []
        self._failure_lock = trio.Lock()
        self._openai_client: AsyncOpenAI | None = None

    async def run(self) -> None:
        self.logger.attach_python_logger("openai.agents", level=logging.DEBUG)
        self.logger.attach_python_logger("openai.agents.tracing", level=logging.INFO)
        self._openai_client = await self._initialize_openai_client()

        try:
            docs = self._load_documents()
            total_docs = len(docs)
            self.logger.info(
                f"Loaded {total_docs} documents from {self.config.input_artifact}"
            )
            self.config.output_directory.mkdir(parents=True, exist_ok=True)

            stage_buffers = self.config.concurrency.stage_buffers
            router_send, router_receive = trio.open_memory_channel[DocTask](
                stage_buffers["router"]
            )
            markdown_send, markdown_receive = trio.open_memory_channel[WorkItem](
                stage_buffers["markdown"]
            )
            notebook_send, notebook_receive = trio.open_memory_channel[WorkItem](
                stage_buffers["notebook"]
            )
            review_send, review_receive = trio.open_memory_channel[ProcessedDoc](
                stage_buffers["review"]
            )
            naming_send, naming_receive = trio.open_memory_channel[ReviewedDoc](
                stage_buffers["naming"]
            )
            write_send, write_receive = trio.open_memory_channel[NamedDoc](
                stage_buffers["write"]
            )

            markdown_done = trio.Event()
            notebook_done = trio.Event()
            review_done = trio.Event()
            naming_done = trio.Event()

            completion_counter = CompletionCounter(total_docs)
            channel_map = {
                "router_send": router_send,
                "markdown_send": markdown_send,
                "notebook_send": notebook_send,
                "review_send": review_send,
                "naming_send": naming_send,
                "write_send": write_send,
            }
            done_events = [markdown_done, notebook_done, review_done, naming_done]

            async with trio.open_nursery() as nursery:
                nursery.start_soon(ingest_documents, docs, router_send)
                nursery.start_soon(
                    router_supervisor,
                    registry=self.registry,
                    config=self.config,
                    logger=self.logger,
                    limiter_pool=self.limiter_pool,
                    retry_policy=self.config.retry_policy,
                    receive=router_receive,
                    markdown_send=markdown_send,
                    notebook_send=notebook_send,
                    completion_counter=completion_counter,
                    record_failure=self._record_failure,
                )
                nursery.start_soon(
                    markdown_supervisor,
                    registry=self.registry,
                    config=self.config,
                    logger=self.logger,
                    limiter_pool=self.limiter_pool,
                    retry_policy=self.config.retry_policy,
                    receive=markdown_receive,
                    review_send=review_send,
                    finished_event=markdown_done,
                    completion_counter=completion_counter,
                    record_failure=self._record_failure,
                )
                nursery.start_soon(
                    notebook_supervisor,
                    registry=self.registry,
                    config=self.config,
                    logger=self.logger,
                    limiter_pool=self.limiter_pool,
                    retry_policy=self.config.retry_policy,
                    receive=notebook_receive,
                    review_send=review_send,
                    finished_event=notebook_done,
                    completion_counter=completion_counter,
                    record_failure=self._record_failure,
                )
                nursery.start_soon(
                    close_when_both_done,
                    markdown_done,
                    notebook_done,
                    review_send,
                )
                nursery.start_soon(
                    review_supervisor,
                    registry=self.registry,
                    config=self.config,
                    logger=self.logger,
                    limiter_pool=self.limiter_pool,
                    retry_policy=self.config.retry_policy,
                    receive=review_receive,
                    naming_send=naming_send,
                    finished_event=review_done,
                    completion_counter=completion_counter,
                    record_failure=self._record_failure,
                )
                nursery.start_soon(close_when_done, review_done, naming_send)
                nursery.start_soon(
                    naming_supervisor,
                    registry=self.registry,
                    config=self.config,
                    logger=self.logger,
                    limiter_pool=self.limiter_pool,
                    retry_policy=self.config.retry_policy,
                    receive=naming_receive,
                    write_send=write_send,
                    finished_event=naming_done,
                    completion_counter=completion_counter,
                    record_failure=self._record_failure,
                )
                nursery.start_soon(close_when_done, naming_done, write_send)
                nursery.start_soon(
                    writer_stage,
                    receive=write_receive,
                    output_directory=self.config.output_directory,
                    logger=self.logger,
                    completion_counter=completion_counter,
                )
                nursery.start_soon(
                    monitor_channels,
                    logger=self.logger,
                    channels=channel_map,
                    counter=completion_counter,
                )
                nursery.start_soon(
                    watch_completion,
                    logger=self.logger,
                    counter=completion_counter,
                    nursery=nursery,
                    done_events=done_events,
                )

            if self.failures:
                self.logger.info(f"Failures encountered: {len(self.failures)}")
                for failure in self.failures:
                    self.logger.info(
                        f" - doc={failure['doc_id']} stage={failure['stage']} url={failure['url']} error={failure['error']}"
                    )
        finally:
            if self._openai_client is not None:
                await self._openai_client.aclose()

    async def _record_failure(
        self,
        doc_id: int,
        url: str,
        stage: str,
        error: Exception,
    ) -> None:
        error_repr = f"{type(error).__name__}: {error}"
        self.logger.verbose(
            f"PIPELINE_FAILURE doc={doc_id} stage={stage} url={url} error={error_repr}"
        )
        tb_str = "".join(
            traceback.format_exception(type(error), error, error.__traceback__)
        )
        timestamp = trio.current_time()
        async with self._failure_lock:
            self.failures.append(
                {
                    "doc_id": doc_id,
                    "url": url,
                    "stage": stage,
                    "error": error_repr,
                    "traceback": tb_str,
                    "timestamp": timestamp,
                }
            )

    async def _initialize_openai_client(self) -> AsyncOpenAI | None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            self.logger.verbose("OPENAI_CLIENT skip reason=no_api_key")
            return None
        timeout_cfg = self.config.httpx_timeout
        timeout = httpx.Timeout(
            connect=timeout_cfg.connect,
            read=timeout_cfg.read,
            write=timeout_cfg.write,
            pool=timeout_cfg.pool,
        )
        client = AsyncOpenAI(api_key=api_key, timeout=timeout)
        set_default_openai_client(client)
        self.logger.verbose(
            "OPENAI_CLIENT "
            f"timeout=connect:{timeout_cfg.connect}s read:{timeout_cfg.read}s "
            f"write:{timeout_cfg.write}s pool:{timeout_cfg.pool}s"
        )
        return client

    def _load_documents(self) -> list[DocTask]:
        payload = json.loads(self.config.input_artifact.read_text(encoding="utf-8"))
        return load_documents(payload)

    def _prepare_run_artifacts(self) -> tuple[Path, Path]:
        original_log = self.config.log_file
        parent = original_log.parent if original_log.parent != Path("") else Path("logs")
        stem = original_log.stem or "pipeline"
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        run_id = f"{stem}-{timestamp}-{uuid4().hex[:6]}"
        run_dir = parent / run_id
        run_dir.mkdir(parents=True, exist_ok=False)

        if self.config.path.exists():
            try:
                shutil.copy2(self.config.path, run_dir / self.config.path.name)
            except OSError:
                pass

        log_filename = original_log.name if original_log.name else f"{stem}.log"
        log_path = run_dir / log_filename
        return log_path, run_dir


def run_pipeline(config: PipelineConfig, *, quiet: bool = False) -> None:
    """Run the pipeline inside a :func:`trio_asyncio.run` loop."""

    pipeline = Pipeline(config, quiet=quiet)
    trio_asyncio.run(pipeline.run)
