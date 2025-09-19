"""Pipeline orchestration entrypoints."""

from __future__ import annotations

import json
import logging
import os
import shutil
import traceback
from datetime import datetime
from functools import partial
from pathlib import Path
from uuid import uuid4

import trio
import trio_asyncio
from agents import set_default_openai_client
from openai import AsyncOpenAI

from .agents.registry import AgentRegistry
from .config import PipelineConfig
from .limiters import LimiterPool
from .logging import StructuredLogger
from .openai_client import ClientTuning, build_async_openai_client
from .stages.ingest import load_documents
from .stages.types import CompletionCounter, DocTask, NamedDoc
from .stages.writer import writer_stage
from .workflow.runner import WorkflowError, WorkflowRunner


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

            write_buffer = self.config.concurrency.stage_buffers.get("write", 10)
            write_send, write_receive = trio.open_memory_channel[NamedDoc](write_buffer)

            completion_counter = CompletionCounter(total_docs)
            workflow_runner = WorkflowRunner(
                config=self.config,
                registry=self.registry,
                limiter_pool=self.limiter_pool,
                logger=self.logger,
            )
            max_parallel = max(1, self.config.concurrency.agent_thread_limit)
            document_sem = trio.Semaphore(max_parallel)

            async with trio.open_nursery() as nursery:
                nursery.start_soon(
                    partial(
                        writer_stage,
                        receive=write_receive,
                        output_directory=self.config.output_directory,
                        logger=self.logger,
                        completion_counter=completion_counter,
                    )
                )

                for doc in docs:
                    nursery.start_soon(
                        self._process_document,
                        workflow_runner,
                        doc,
                        write_send.clone(),
                        document_sem,
                        completion_counter,
                    )

                nursery.start_soon(
                    self._close_writer_when_done,
                    completion_counter,
                    write_send,
                )

        finally:
            if self._openai_client is not None:
                try:
                    # Bridge asyncio-based close() into Trio using trio-asyncio.
                    await trio_asyncio.aio_as_trio(self._openai_client.close)()
                except RuntimeError as exc:
                    if "Event loop is closed" in str(exc):
                        self.logger.debug(
                            "OPENAI_CLIENT close skipped: asyncio loop already closed"
                        )
                    else:  # pragma: no cover - unexpected runtime failure
                        raise
                except BaseExceptionGroup as exc_group:  # pragma: no cover - defensive
                    remaining: list[BaseException] = []
                    for exc in exc_group.exceptions:
                        if isinstance(exc, RuntimeError) and "Event loop is closed" in str(exc):
                            self.logger.debug(
                                "OPENAI_CLIENT close skipped: asyncio loop already closed"
                            )
                        else:
                            remaining.append(exc)
                    if remaining:
                        raise BaseExceptionGroup(
                            "Failed to close OpenAI client", remaining
                        ) from None

        if self.failures:
            self.logger.info(f"Failures encountered: {len(self.failures)}")
            for failure in self.failures:
                self.logger.info(
                    f" - doc={failure['doc_id']} stage={failure['stage']} url={failure['url']} error={failure['error']}"
                )

    async def _process_document(
        self,
        workflow_runner: WorkflowRunner,
        doc: DocTask,
        write_send: trio.MemorySendChannel[NamedDoc],
        semaphore: trio.Semaphore,
        completion_counter: CompletionCounter,
    ) -> None:
        async with semaphore:
            try:
                async with write_send:
                    try:
                        artifacts = await workflow_runner.process_document(doc)
                    except WorkflowError as exc:
                        await self._record_failure(doc.doc_id, doc.url, "workflow", exc)
                    except Exception as exc:  # noqa: BLE001
                        await self._record_failure(doc.doc_id, doc.url, "workflow", exc)
                    else:
                        metadata = dict(doc.metadata)
                        metadata.update(
                            {
                                "route": artifacts.route,
                                "summary": artifacts.summary,
                                "review_approved": artifacts.review.approved,
                                "review_issues": artifacts.review.issues,
                                "review_suggestions": artifacts.review.suggestions,
                                "rework_cycles": artifacts.rework_cycles,
                            }
                        )
                        named_doc = NamedDoc(
                            doc_id=doc.doc_id,
                            url=doc.url,
                            file_slug=artifacts.naming.file_slug,
                            extension=artifacts.naming.extension,
                            processed_text=artifacts.processed_text,
                            metadata=metadata,
                            trajectory=artifacts.trajectory,
                            final_output=artifacts.final_output,
                        )
                        self.logger.verbose(
                            "WORKFLOW_RESULT "
                            f"doc={doc.doc_id} url={doc.url} route={artifacts.route} "
                            f"slug={artifacts.naming.file_slug}{artifacts.naming.extension} "
                            f"approved={artifacts.review.approved} rework_cycles={artifacts.rework_cycles}"
                        )
                        await write_send.send(named_doc)
            finally:
                await completion_counter.increment()

    async def _close_writer_when_done(
        self,
        completion_counter: CompletionCounter,
        write_send: trio.MemorySendChannel[NamedDoc],
    ) -> None:
        await completion_counter.completed.wait()
        await write_send.aclose()

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
        client = build_async_openai_client(
            api_key=api_key,
            timeout_cfg=timeout_cfg,
            tuning=ClientTuning(max_retries=5),
        )
        set_default_openai_client(client)
        self.logger.verbose(
            "OPENAI_CLIENT "
            f"timeout=connect:{timeout_cfg.connect}s read:{timeout_cfg.read}s "
            f"write:{timeout_cfg.write}s pool:{timeout_cfg.pool}s max_retries=5"
        )
        return client

    def _load_documents(self) -> list[DocTask]:
        payload = json.loads(self.config.input_artifact.read_text(encoding="utf-8"))
        return load_documents(payload)

    def _prepare_run_artifacts(self) -> tuple[Path, Path]:
        original_log = self.config.log_file
        parent = (
            original_log.parent if original_log.parent != Path("") else Path("logs")
        )
        stem = original_log.stem or "pipeline"
        timestamp = datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")
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
