#!/usr/bin/env python3
"""Concurrent document cleaning pipeline using OpenAI Agents and Trio."""

from __future__ import annotations

import argparse
import json
import logging
import os
import random
import re
import sys
import threading
import traceback
import unicodedata
from collections.abc import Awaitable, Callable, Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

import httpx
import trio_asyncio
from agents import Agent, Runner, set_default_openai_client
from agents.items import ItemHelpers
from agents.lifecycle import RunHooks
from agents.model_settings import ModelSettings
from agents.run import RunConfig
from agents.run_context import RunContextWrapper
from openai import AsyncOpenAI
from openai.types.shared import Reasoning
from pydantic import BaseModel, Field

import trio
from trio.lowlevel import current_task

AGENT_THREAD_LIMIT = 10
DEFAULT_AGENT_TIMEOUT = 300.0
LARGE_DOCUMENT_THRESHOLD = 1_000_000
CHANNEL_PRESSURE_FRACTION = 0.8
CHANNEL_MONITOR_INTERVAL = 10.0

AGENT_THREAD_LIMITER = trio.CapacityLimiter(AGENT_THREAD_LIMIT)


# ---------------------------------------------------------------------------
# Structured logging + lifecycle hooks (adapted from trio_agents_firecrawl)


class StructuredLogger:
    """Thread-safe logger that mirrors console output to a verbose log file."""

    def __init__(self, *, quiet: bool, verbose_path: Path) -> None:
        self.quiet = quiet
        self.verbose_path = verbose_path
        self._lock = threading.Lock()
        self._attached_logger_names: set[str] = set()
        verbose_path.parent.mkdir(parents=True, exist_ok=True)
        verbose_path.write_text("", encoding="utf-8")

    def info(self, message: str, *, spacer: bool = False) -> None:
        formatted = message.rstrip()
        if not self.quiet:
            if spacer:
                print()
            print(formatted)
        self._write_verbose(formatted)

    def blank_line(self) -> None:
        if not self.quiet:
            print()
        self._write_verbose("")

    def verbose(self, message: str) -> None:
        self._write_verbose(message.rstrip())

    def attach_python_logger(self, name: str, level: int = logging.INFO) -> None:
        if name in self._attached_logger_names:
            return
        handler = _StructuredLoggingHandler(self)
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))
        py_logger = logging.getLogger(name)
        py_logger.addHandler(handler)
        py_logger.setLevel(level)
        py_logger.propagate = False
        self._attached_logger_names.add(name)

    def _write_verbose(self, message: str) -> None:
        with self._lock:
            with self.verbose_path.open("a", encoding="utf-8") as stream:
                stream.write(message.rstrip("\n") + "\n")


class _StructuredLoggingHandler(logging.Handler):
    def __init__(self, structured_logger: StructuredLogger) -> None:
        super().__init__()
        self._structured_logger = structured_logger

    def emit(
        self, record: logging.LogRecord
    ) -> None:  # pragma: no cover - logging bridge
        try:
            message = self.format(record)
        except Exception:  # noqa: BLE001
            message = record.getMessage()
        self._structured_logger.verbose(
            f"SDK_LOG level={record.levelname} logger={record.name} message={message}"
        )


class AgentCallContext:
    """Context passed through Agents SDK runs to enrich telemetry."""

    def __init__(
        self,
        logger: StructuredLogger,
        workflow_name: str,
        stage: str,
        run_id: str,
        doc_url: str,
        metadata: dict[str, Any],
        trace_id: str | None = None,
    ) -> None:
        self.logger = logger
        self.workflow_name = workflow_name
        self.stage = stage
        self.run_id = run_id
        self.doc_url = doc_url
        self.metadata = metadata
        self.trace_id = trace_id
        self.prompt_excerpt: str | None = None


class LifecycleLoggingHooks(RunHooks[AgentCallContext]):
    def __init__(self, context: AgentCallContext) -> None:
        self._context = context

    def _ensure_context(
        self, wrapper: RunContextWrapper[AgentCallContext]
    ) -> AgentCallContext:
        ctx = wrapper.context
        if ctx is not self._context:
            self._context = ctx
        return ctx

    async def on_agent_start(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
    ) -> None:
        ctx = self._ensure_context(context)
        ctx.logger.verbose(
            f"AGENT_EVENT event=agent_start stage={ctx.stage} run={ctx.run_id} trace={ctx.trace_id} "
            f"agent={agent.name} doc={ctx.doc_url}"
        )

    async def on_agent_end(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        output: Any,
    ) -> None:
        ctx = self._ensure_context(context)
        usage = context.usage
        ctx.logger.verbose(
            " ".join(
                part
                for part in [
                    "AGENT_EVENT",
                    "event=agent_end",
                    f"stage={ctx.stage}",
                    f"run={ctx.run_id}",
                    f"trace={ctx.trace_id}",
                    f"agent={agent.name}",
                    f"doc={ctx.doc_url}",
                    f"requests={usage.requests}",
                    f"input_tokens={usage.input_tokens}",
                    f"output_tokens={usage.output_tokens}",
                ]
            )
        )

    async def on_llm_start(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        system_prompt: str | None,
        input_items: list[Any],
    ) -> None:
        ctx = self._ensure_context(context)
        ctx.logger.verbose(
            f"AGENT_EVENT event=llm_start stage={ctx.stage} run={ctx.run_id} trace={ctx.trace_id} "
            f"agent={agent.name} doc={ctx.doc_url} items={len(input_items)}"
        )

    async def on_llm_end(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        response: Any,
    ) -> None:
        ctx = self._ensure_context(context)
        outputs = getattr(response, "output", [])
        preview = None
        if outputs:
            try:
                preview = ItemHelpers.extract_last_content(outputs[-1])
            except Exception:  # noqa: BLE001
                preview = None
        ctx.logger.verbose(
            " ".join(
                part
                for part in [
                    "AGENT_EVENT",
                    "event=llm_end",
                    f"stage={ctx.stage}",
                    f"run={ctx.run_id}",
                    f"trace={ctx.trace_id}",
                    f"agent={agent.name}",
                    f"doc={ctx.doc_url}",
                    f"output_items={len(outputs)}",
                    f"preview={_truncate(preview) if preview else ''}",
                ]
            )
        )

    async def on_tool_start(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        tool: Any,
    ) -> None:
        ctx = self._ensure_context(context)
        ctx.logger.verbose(
            f"AGENT_EVENT event=tool_start stage={ctx.stage} run={ctx.run_id} trace={ctx.trace_id} "
            f"agent={agent.name} doc={ctx.doc_url} tool={getattr(tool, 'name', None)}"
        )

    async def on_tool_end(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        tool: Any,
        result: str,
    ) -> None:
        ctx = self._ensure_context(context)
        ctx.logger.verbose(
            " ".join(
                part
                for part in [
                    "AGENT_EVENT",
                    "event=tool_end",
                    f"stage={ctx.stage}",
                    f"run={ctx.run_id}",
                    f"trace={ctx.trace_id}",
                    f"agent={agent.name}",
                    f"doc={ctx.doc_url}",
                    f"tool={getattr(tool, 'name', None)}",
                    f"result={_truncate(result)}",
                ]
            )
        )


# ---------------------------------------------------------------------------
# Structured outputs for agent responses


class RoutingDecision(BaseModel):
    route: Literal["markdown", "notebook"]
    rationale: str | None = None
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)


class MarkdownCleanResult(BaseModel):
    cleaned_markdown: str
    summary: str | None = None


class NotebookRefactorResult(BaseModel):
    python_script: str
    summary: str | None = None


class ReviewResult(BaseModel):
    approved: bool
    issues: str | None = None
    suggestions: str | None = None


class NamingResult(BaseModel):
    file_slug: str
    extension: str
    title: str | None = None


# ---------------------------------------------------------------------------
# Pipeline configuration dataclasses


@dataclass
class AgentSpec:
    name: str
    instructions: str
    model: str
    reasoning_effort: str | None
    verbosity: str | None
    timeout: float | None
    max_tokens: int | None


@dataclass
class RetryPolicy:
    max_attempts: int
    initial_delay: float
    backoff_multiplier: float
    max_delay: float
    jitter_ratio: float


@dataclass
class PipelineConfig:
    log_file: Path
    workflow_name: str
    trace_metadata: dict[str, Any]
    input_artifact: Path
    output_directory: Path
    router_pool: int
    markdown_pool: int
    notebook_pool: int
    review_pool: int
    naming_pool: int
    channel_buffer: int
    max_attempts: int
    retry_policy: RetryPolicy
    agent_specs: dict[str, AgentSpec]

    @classmethod
    def from_json(cls, path: Path) -> PipelineConfig:
        payload = json.loads(path.read_text(encoding="utf-8"))
        logging_cfg = payload.get("logging", {})
        concurrency_cfg = payload.get("concurrency", {})
        retry_cfg = payload.get("retry", {})
        io_cfg = payload.get("io", {})

        agents_cfg = payload.get("agents", {})
        agent_specs: dict[str, AgentSpec] = {}
        for key, spec in agents_cfg.items():
            agent_specs[key] = AgentSpec(
                name=spec["name"],
                instructions=spec["instructions"],
                model=spec["model"],
                reasoning_effort=spec.get("reasoning_effort"),
                verbosity=spec.get("verbosity"),
                timeout=spec.get("timeout"),
                max_tokens=spec.get("max_tokens"),
            )

        return cls(
            log_file=Path(logging_cfg.get("log_file", "logs/agent_pipeline.log")),
            workflow_name=logging_cfg.get("trace_workflow_name", "doc-cleaning"),
            trace_metadata=logging_cfg.get("trace_metadata", {}),
            input_artifact=Path(
                io_cfg.get("input_artifact", "artifacts/lark_docs.json")
            ),
            output_directory=Path(
                io_cfg.get("output_directory", "artifacts/cleaned_docs")
            ),
            router_pool=int(concurrency_cfg.get("router_pool", 2)),
            markdown_pool=int(concurrency_cfg.get("markdown_pool", 4)),
            notebook_pool=int(concurrency_cfg.get("notebook_pool", 2)),
            review_pool=int(concurrency_cfg.get("review_pool", 1)),
            naming_pool=int(concurrency_cfg.get("naming_pool", 1)),
            channel_buffer=int(concurrency_cfg.get("channel_buffer", 10)),
            max_attempts=int(retry_cfg.get("max_attempts", 2)),
            retry_policy=RetryPolicy(
                max_attempts=int(retry_cfg.get("max_attempts", 2)),
                initial_delay=float(retry_cfg.get("initial_delay", 1.0)),
                backoff_multiplier=float(retry_cfg.get("backoff_multiplier", 2.0)),
                max_delay=float(retry_cfg.get("max_delay", 30.0)),
                jitter_ratio=float(retry_cfg.get("jitter_ratio", 0.25)),
            ),
            agent_specs=agent_specs,
        )


# ---------------------------------------------------------------------------
# Utility helpers


def _truncate(value: str | None, limit: int = 160) -> str:
    if not value:
        return ""
    collapsed = " ".join(value.split())
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[:limit] + "..."


def normalize_slug(text: str) -> str:
    text_norm = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text_norm = re.sub(r"[^A-Za-z0-9\-]+", "-", text_norm.lower())
    text_norm = text_norm.strip("-")
    return text_norm or "document"


def infer_doc_kind(url: str, metadata: dict[str, Any]) -> str | None:
    lower_url = url.lower()
    if lower_url.endswith(".ipynb"):
        return "notebook"
    mime = metadata.get("mimeType") or metadata.get("mimetype")
    if mime and "json" in str(mime).lower() and "notebook" in str(mime).lower():
        return "notebook"
    if mime and "markdown" in str(mime).lower():
        return "markdown"
    if lower_url.endswith((".md", ".markdown")):
        return "markdown"
    return None


# ---------------------------------------------------------------------------
# Data containers flowing through the pipeline


@dataclass
class DocTask:
    doc_id: int
    url: str
    content: str
    metadata: dict[str, Any]


@dataclass
class WorkItem:
    doc_id: int
    url: str
    content: str
    metadata: dict[str, Any]
    kind: Literal["markdown", "notebook"]
    attempts: int = 0
    review_feedback: str | None = None


@dataclass
class ProcessedDoc:
    doc_id: int
    url: str
    kind: Literal["markdown", "notebook"]
    processed_text: str
    metadata: dict[str, Any]
    attempts: int
    summary: str | None = None


@dataclass
class ReviewedDoc:
    doc_id: int
    url: str
    kind: Literal["markdown", "notebook"]
    processed_text: str
    metadata: dict[str, Any]
    title_hint: str | None


@dataclass
class NamedDoc:
    doc_id: int
    url: str
    file_slug: str
    extension: str
    processed_text: str
    metadata: dict[str, Any]


# ---------------------------------------------------------------------------
# Agent factory & runner helpers


class AgentFactory:
    def __init__(self, config: PipelineConfig, logger: StructuredLogger) -> None:
        self.config = config
        self.logger = logger
        self._agents: dict[str, Agent[Any]] = {}

    def get_router_agent(self) -> Agent[Any]:
        return self._get_agent("router", output_type=RoutingDecision)

    def get_markdown_agent(self) -> Agent[Any]:
        return self._get_agent("markdown_cleaner", output_type=MarkdownCleanResult)

    def get_notebook_agent(self) -> Agent[Any]:
        return self._get_agent("notebook_refactor", output_type=NotebookRefactorResult)

    def get_reviewer_agent(self) -> Agent[Any]:
        return self._get_agent("reviewer", output_type=ReviewResult)

    def get_namer_agent(self) -> Agent[Any]:
        return self._get_agent("namer", output_type=NamingResult)

    def _get_agent(self, key: str, *, output_type: Any) -> Agent[Any]:
        if key in self._agents:
            return self._agents[key]
        spec = self.config.agent_specs[key]
        reasoning = None
        if spec.reasoning_effort:
            reasoning = Reasoning(effort=spec.reasoning_effort)  # type: ignore[arg-type]
        model_settings = ModelSettings(
            reasoning=reasoning,
            verbosity=spec.verbosity,
            max_tokens=spec.max_tokens,
        )
        agent = Agent[Any](
            name=spec.name,
            instructions=spec.instructions,
            model=spec.model,
            model_settings=model_settings,
            output_type=output_type,
        )
        self._agents[key] = agent
        return agent

    def get_timeout(self, key: str) -> float:
        spec = self.config.agent_specs[key]
        return spec.timeout if spec.timeout is not None else DEFAULT_AGENT_TIMEOUT


async def run_agent(
    agent: Agent[Any],
    message: str,
    context: AgentCallContext,
    *,
    run_config: RunConfig,
    timeout: float | None = None,
) -> Any:
    hooks = LifecycleLoggingHooks(context)
    deadline = timeout if timeout is not None else DEFAULT_AGENT_TIMEOUT
    token = current_task()
    await AGENT_THREAD_LIMITER.acquire_on_behalf_of(token)
    try:
        result: Any = None
        with trio.move_on_after(deadline) as cancel_scope:
            result = await trio_asyncio.aio_as_trio(Runner.run)(
                agent,
                message,
                context=context,
                hooks=hooks,
                run_config=run_config,
            )
        if cancel_scope.cancelled_caught:
            raise TimeoutError(
                f"Agent call timed out after {deadline} seconds during stage {context.stage}"
            )
        return result
    finally:
        AGENT_THREAD_LIMITER.release_on_behalf_of(token)


def build_run_config(config: PipelineConfig, context: AgentCallContext) -> RunConfig:
    trace_metadata = dict(config.trace_metadata)
    trace_metadata.update(
        {"stage": context.stage, "doc_url": context.doc_url, "run_id": context.run_id}
    )
    return RunConfig(
        workflow_name=config.workflow_name,
        trace_id=context.trace_id,
        trace_metadata=trace_metadata,
    )


# ---------------------------------------------------------------------------
# Pipeline implementation


class Pipeline:
    def __init__(self, config: PipelineConfig, quiet: bool = False) -> None:
        self.config = config
        self.logger = StructuredLogger(quiet=quiet, verbose_path=config.log_file)
        self._openai_client = self._initialize_openai_client()
        self.factory = AgentFactory(config, self.logger)
        self.retry_policy = config.retry_policy
        self.failures: list[dict[str, Any]] = []
        self._failure_lock = trio.Lock()

    async def run(self) -> None:
        try:
            self.logger.attach_python_logger("openai.agents", level=logging.DEBUG)
            self.logger.attach_python_logger(
                "openai.agents.tracing", level=logging.INFO
            )
            docs = self._load_documents()
            total_docs = len(docs)
            self.logger.info(
                f"Loaded {total_docs} documents from {self.config.input_artifact}"
            )
            self.config.output_directory.mkdir(parents=True, exist_ok=True)

            router_send, router_receive = trio.open_memory_channel[DocTask](
                self.config.channel_buffer
            )
            markdown_send, markdown_receive = trio.open_memory_channel[WorkItem](
                self.config.channel_buffer
            )
            notebook_send, notebook_receive = trio.open_memory_channel[WorkItem](
                self.config.channel_buffer
            )
            review_send, review_receive = trio.open_memory_channel[ProcessedDoc](
                self.config.channel_buffer
            )
            naming_send, naming_receive = trio.open_memory_channel[ReviewedDoc](
                self.config.channel_buffer
            )
            write_send, write_receive = trio.open_memory_channel[NamedDoc](
                self.config.channel_buffer
            )

            markdown_done = trio.Event()
            notebook_done = trio.Event()
            review_done = trio.Event()
            naming_done = trio.Event()

            completion_counter = CompletionCounter(total_docs)
            channel_map: dict[str, Any] = {
                "router_send": router_send,
                "markdown_send": markdown_send,
                "notebook_send": notebook_send,
                "review_send": review_send,
                "naming_send": naming_send,
                "write_send": write_send,
            }
            done_events: list[trio.Event] = [
                markdown_done,
                notebook_done,
                review_done,
                naming_done,
            ]

            async with trio.open_nursery() as nursery:
                nursery.start_soon(self._ingest_documents, docs, router_send)
                nursery.start_soon(
                    self._router_supervisor,
                    router_receive,
                    markdown_send,
                    notebook_send,
                    completion_counter,
                )
                nursery.start_soon(
                    self._markdown_supervisor,
                    markdown_receive,
                    review_send,
                    markdown_done,
                    completion_counter,
                )
                nursery.start_soon(
                    self._notebook_supervisor,
                    notebook_receive,
                    review_send,
                    notebook_done,
                    completion_counter,
                )
                nursery.start_soon(
                    self._close_when_both_done,
                    markdown_done,
                    notebook_done,
                    review_send,
                )
                nursery.start_soon(
                    self._review_supervisor,
                    review_receive,
                    naming_send,
                    review_done,
                    completion_counter,
                )
                nursery.start_soon(self._close_when_done, review_done, naming_send)
                nursery.start_soon(
                    self._naming_supervisor,
                    naming_receive,
                    write_send,
                    naming_done,
                    completion_counter,
                )
                nursery.start_soon(self._close_when_done, naming_done, write_send)
                nursery.start_soon(self._writer, write_receive, completion_counter)
                nursery.start_soon(
                    self._monitor_channels,
                    channel_map,
                    completion_counter,
                )
                nursery.start_soon(
                    self._watch_completion,
                    completion_counter,
                    nursery,
                    done_events,
                )

            if self.failures:
                self.logger.info(f"Failures encountered: {len(self.failures)}")
                for failure in self.failures:
                    self.logger.info(
                        f" - doc={failure['doc_id']} stage={failure['stage']} url={failure['url']} error={failure['error']}"
                    )
        finally:
            if self._openai_client is not None:
                self._openai_client.close()

    async def _execute_with_retry(
        self,
        *,
        stage: str,
        doc_id: int,
        call_factory: Callable[[int], Awaitable[Any]],
    ) -> Any:
        attempt = 0
        while True:
            try:
                return await call_factory(attempt)
            except Exception as exc:
                attempt += 1
                error_repr = f"{type(exc).__name__}: {exc}"
                self.logger.verbose(
                    f"AGENT_RETRY stage={stage} doc={doc_id} attempt={attempt} error={_truncate(error_repr, 300)}"
                )
                if attempt >= self.retry_policy.max_attempts:
                    raise
                delay = self.retry_policy.initial_delay * (
                    self.retry_policy.backoff_multiplier ** (attempt - 1)
                )
                delay = min(delay, self.retry_policy.max_delay)
                jitter = delay * self.retry_policy.jitter_ratio
                sleep_for = delay + random.uniform(-jitter, jitter)
                sleep_for = max(0.05, sleep_for)
                await trio.sleep(sleep_for)

    async def _record_failure(
        self,
        *,
        doc_id: int,
        url: str,
        stage: str,
        error: Exception,
        counter: CompletionCounter,
    ) -> None:
        error_repr = f"{type(error).__name__}: {error}"
        self.logger.verbose(
            f"PIPELINE_FAILURE doc={doc_id} stage={stage} url={url} error={_truncate(error_repr, 300)}"
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
        await counter.increment()

    def _initialize_openai_client(self) -> AsyncOpenAI | None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            self.logger.verbose("OPENAI_CLIENT skip reason=no_api_key")
            return None
        timeout = httpx.Timeout(connect=5.0, read=120.0, write=30.0, pool=5.0)
        client = AsyncOpenAI(api_key=api_key, timeout=timeout)
        set_default_openai_client(client)
        self.logger.verbose(
            "OPENAI_CLIENT timeout=connect:5.0s read:120.0s write:30.0s pool:5.0s"
        )
        return client

    async def _ingest_documents(
        self, docs: list[DocTask], send_channel: trio.MemorySendChannel[DocTask]
    ) -> None:
        async with send_channel:
            for doc in docs:
                await send_channel.send(doc)

    async def _router_supervisor(
        self,
        receive: trio.MemoryReceiveChannel[DocTask],
        markdown_send: trio.MemorySendChannel[WorkItem],
        notebook_send: trio.MemorySendChannel[WorkItem],
        completion_counter: CompletionCounter,
    ) -> None:
        router_agent = self.factory.get_router_agent()
        router_timeout = self.factory.get_timeout("router")
        router_pool = self.config.router_pool

        async def worker(worker_idx: int) -> None:
            async with receive.clone() as channel:
                async for task in channel:
                    doc_size = len(task.content)
                    if doc_size > LARGE_DOCUMENT_THRESHOLD:
                        self.logger.verbose(
                            f"DOC_SIZE_WARNING doc={task.doc_id} bytes={doc_size}"
                        )
                    kind = infer_doc_kind(task.url, task.metadata)
                    rationale = "heuristic" if kind else None
                    if not kind:

                        async def call(attempt_index: int, task=task) -> Any:
                            metadata = dict(task.metadata)
                            metadata.setdefault("stage", "routing")
                            ctx = AgentCallContext(
                                logger=self.logger,
                                workflow_name=self.config.workflow_name,
                                stage="routing",
                                run_id=f"route-{task.doc_id}-{worker_idx}-try{attempt_index}",
                                doc_url=task.url,
                                metadata=metadata,
                                trace_id=None,
                            )
                            run_config = build_run_config(self.config, ctx)
                            prompt = _build_router_prompt(task)
                            return await run_agent(
                                router_agent,
                                prompt,
                                ctx,
                                run_config=run_config,
                                timeout=router_timeout,
                            )

                        try:
                            result = await self._execute_with_retry(
                                stage="routing",
                                doc_id=task.doc_id,
                                call_factory=call,
                            )
                        except Exception as exc:
                            await self._record_failure(
                                doc_id=task.doc_id,
                                url=task.url,
                                stage="routing",
                                error=exc,
                                counter=completion_counter,
                            )
                            continue

                        decision = result.final_output
                        kind = decision.route
                        rationale = decision.rationale
                    self.logger.verbose(
                        f"ROUTED doc={task.doc_id} url={task.url} kind={kind} rationale={_truncate(rationale)}"
                    )
                    item = WorkItem(
                        doc_id=task.doc_id,
                        url=task.url,
                        content=task.content,
                        metadata=task.metadata,
                        kind=kind,  # type: ignore[arg-type]
                    )
                    if kind == "markdown":
                        await markdown_send.send(item)
                    else:
                        await notebook_send.send(item)

        async with trio.open_nursery() as router_nursery:
            for idx in range(router_pool):
                router_nursery.start_soon(worker, idx)
        await markdown_send.aclose()
        await notebook_send.aclose()

    async def _markdown_supervisor(
        self,
        receive: trio.MemoryReceiveChannel[WorkItem],
        review_send: trio.MemorySendChannel[ProcessedDoc],
        finished_event: trio.Event,
        completion_counter: CompletionCounter,
    ) -> None:
        agent = self.factory.get_markdown_agent()
        markdown_timeout = self.factory.get_timeout("markdown_cleaner")
        pool = self.config.markdown_pool

        async def worker(worker_idx: int) -> None:
            async with receive.clone() as channel:
                async for item in channel:

                    async def call(attempt_index: int, item=item) -> Any:
                        metadata = dict(item.metadata)
                        metadata.setdefault("stage", "markdown-clean")
                        ctx = AgentCallContext(
                            logger=self.logger,
                            workflow_name=self.config.workflow_name,
                            stage="markdown-clean",
                            run_id=f"md-{item.doc_id}-{worker_idx}-try{attempt_index}",
                            doc_url=item.url,
                            metadata=metadata,
                            trace_id=None,
                        )
                        run_config = build_run_config(self.config, ctx)
                        prompt = _build_markdown_prompt(item)
                        return await run_agent(
                            agent,
                            prompt,
                            ctx,
                            run_config=run_config,
                            timeout=markdown_timeout,
                        )

                    try:
                        result = await self._execute_with_retry(
                            stage="markdown",
                            doc_id=item.doc_id,
                            call_factory=call,
                        )
                    except Exception as exc:
                        await self._record_failure(
                            doc_id=item.doc_id,
                            url=item.url,
                            stage="markdown",
                            error=exc,
                            counter=completion_counter,
                        )
                        continue

                    output: MarkdownCleanResult = result.final_output
                    processed = ProcessedDoc(
                        doc_id=item.doc_id,
                        url=item.url,
                        kind="markdown",
                        processed_text=output.cleaned_markdown,
                        metadata=item.metadata,
                        attempts=item.attempts,
                        summary=output.summary,
                    )
                    await review_send.send(processed)

        async with trio.open_nursery() as md_nursery:
            for idx in range(pool):
                md_nursery.start_soon(worker, idx)
        finished_event.set()

    async def _notebook_supervisor(
        self,
        receive: trio.MemoryReceiveChannel[WorkItem],
        review_send: trio.MemorySendChannel[ProcessedDoc],
        finished_event: trio.Event,
        completion_counter: CompletionCounter,
    ) -> None:
        agent = self.factory.get_notebook_agent()
        notebook_timeout = self.factory.get_timeout("notebook_refactor")
        pool = self.config.notebook_pool

        async def worker(worker_idx: int) -> None:
            async with receive.clone() as channel:
                async for item in channel:

                    async def call(attempt_index: int, item=item) -> Any:
                        metadata = dict(item.metadata)
                        metadata.setdefault("stage", "notebook-refactor")
                        ctx = AgentCallContext(
                            logger=self.logger,
                            workflow_name=self.config.workflow_name,
                            stage="notebook-refactor",
                            run_id=f"nb-{item.doc_id}-{worker_idx}-try{attempt_index}",
                            doc_url=item.url,
                            metadata=metadata,
                            trace_id=None,
                        )
                        run_config = build_run_config(self.config, ctx)
                        prompt = _build_notebook_prompt(item)
                        return await run_agent(
                            agent,
                            prompt,
                            ctx,
                            run_config=run_config,
                            timeout=notebook_timeout,
                        )

                    try:
                        result = await self._execute_with_retry(
                            stage="notebook",
                            doc_id=item.doc_id,
                            call_factory=call,
                        )
                    except Exception as exc:
                        await self._record_failure(
                            doc_id=item.doc_id,
                            url=item.url,
                            stage="notebook",
                            error=exc,
                            counter=completion_counter,
                        )
                        continue

                    output: NotebookRefactorResult = result.final_output
                    processed = ProcessedDoc(
                        doc_id=item.doc_id,
                        url=item.url,
                        kind="notebook",
                        processed_text=output.python_script,
                        metadata=item.metadata,
                        attempts=item.attempts,
                        summary=output.summary,
                    )
                    await review_send.send(processed)

        async with trio.open_nursery() as nb_nursery:
            for idx in range(pool):
                nb_nursery.start_soon(worker, idx)
        finished_event.set()

    async def _close_when_both_done(
        self,
        event_one: trio.Event,
        event_two: trio.Event,
        send_channel: trio.MemorySendChannel[Any],
    ) -> None:
        await event_one.wait()
        await event_two.wait()
        await send_channel.aclose()

    async def _review_supervisor(
        self,
        receive: trio.MemoryReceiveChannel[ProcessedDoc],
        naming_send: trio.MemorySendChannel[ReviewedDoc],
        finished_event: trio.Event,
        counter: CompletionCounter,
    ) -> None:
        agent = self.factory.get_reviewer_agent()
        review_timeout = self.factory.get_timeout("reviewer")
        pool = max(1, self.config.review_pool)

        async def worker(worker_idx: int) -> None:
            async with receive.clone() as channel:
                async for doc in channel:

                    async def call(attempt_index: int, doc=doc) -> Any:
                        metadata = dict(doc.metadata)
                        metadata.setdefault("stage", "review")
                        ctx = AgentCallContext(
                            logger=self.logger,
                            workflow_name=self.config.workflow_name,
                            stage="review",
                            run_id=f"rv-{doc.doc_id}-{worker_idx}-try{attempt_index}",
                            doc_url=doc.url,
                            metadata=metadata,
                            trace_id=None,
                        )
                        run_config = build_run_config(self.config, ctx)
                        prompt = _build_review_prompt(doc)
                        return await run_agent(
                            agent,
                            prompt,
                            ctx,
                            run_config=run_config,
                            timeout=review_timeout,
                        )

                    try:
                        result = await self._execute_with_retry(
                            stage="review",
                            doc_id=doc.doc_id,
                            call_factory=call,
                        )
                    except Exception as exc:
                        await self._record_failure(
                            doc_id=doc.doc_id,
                            url=doc.url,
                            stage="review",
                            error=exc,
                            counter=counter,
                        )
                        continue

                    review: ReviewResult = result.final_output
                    if review.approved:
                        reviewed = ReviewedDoc(
                            doc_id=doc.doc_id,
                            url=doc.url,
                            kind=doc.kind,
                            processed_text=doc.processed_text,
                            metadata=doc.metadata,
                            title_hint=review.suggestions or review.issues,
                        )
                        await naming_send.send(reviewed)
                    else:
                        self.logger.verbose(
                            f"REVIEW_REJECT doc={doc.doc_id} issues={_truncate(review.issues)}"
                        )
                        await counter.increment()

        async with trio.open_nursery() as rv_nursery:
            for idx in range(pool):
                rv_nursery.start_soon(worker, idx)
        finished_event.set()

    async def _naming_supervisor(
        self,
        receive: trio.MemoryReceiveChannel[ReviewedDoc],
        write_send: trio.MemorySendChannel[NamedDoc],
        finished_event: trio.Event,
        completion_counter: CompletionCounter,
    ) -> None:
        agent = self.factory.get_namer_agent()
        naming_timeout = self.factory.get_timeout("namer")
        pool = max(1, self.config.naming_pool)

        async def worker(worker_idx: int) -> None:
            async with receive.clone() as channel:
                async for doc in channel:

                    async def call(attempt_index: int, doc=doc) -> Any:
                        metadata = dict(doc.metadata)
                        metadata.setdefault("stage", "naming")
                        ctx = AgentCallContext(
                            logger=self.logger,
                            workflow_name=self.config.workflow_name,
                            stage="naming",
                            run_id=f"name-{doc.doc_id}-{worker_idx}-try{attempt_index}",
                            doc_url=doc.url,
                            metadata=metadata,
                            trace_id=None,
                        )
                        run_config = build_run_config(self.config, ctx)
                        prompt = _build_naming_prompt(doc)
                        return await run_agent(
                            agent,
                            prompt,
                            ctx,
                            run_config=run_config,
                            timeout=naming_timeout,
                        )

                    try:
                        result = await self._execute_with_retry(
                            stage="naming",
                            doc_id=doc.doc_id,
                            call_factory=call,
                        )
                    except Exception as exc:
                        await self._record_failure(
                            doc_id=doc.doc_id,
                            url=doc.url,
                            stage="naming",
                            error=exc,
                            counter=completion_counter,
                        )
                        continue

                    naming: NamingResult = result.final_output
                    named = NamedDoc(
                        doc_id=doc.doc_id,
                        url=doc.url,
                        file_slug=normalize_slug(naming.file_slug),
                        extension=_safe_extension(naming.extension, doc.kind),
                        processed_text=doc.processed_text,
                        metadata=doc.metadata,
                    )
                    await write_send.send(named)

        async with trio.open_nursery() as nm_nursery:
            for idx in range(pool):
                nm_nursery.start_soon(worker, idx)
        finished_event.set()

    async def _writer(
        self, receive: trio.MemoryReceiveChannel[NamedDoc], counter: CompletionCounter
    ) -> None:
        existing_names: dict[str, int] = {}
        lock = trio.Lock()
        async with receive:
            async for doc in receive:
                async with lock:
                    base = doc.file_slug or "document"
                    ext = (
                        doc.extension
                        if doc.extension.startswith(".")
                        else f".{doc.extension}"
                        if doc.extension
                        else ".md"
                    )
                    filename = f"{base}{ext}"
                    while (self.config.output_directory / filename).exists():
                        existing_names[base] = existing_names.get(base, 0) + 1
                        filename = f"{base}-{existing_names[base]}{ext}"
                path = self.config.output_directory / filename
                path.write_text(doc.processed_text, encoding="utf-8")
                await counter.increment()
                self.logger.verbose(f"WROTE doc={doc.doc_id} -> {path}")

    async def _close_when_done(
        self,
        done_event: trio.Event,
        send_channel: trio.MemorySendChannel[Any],
    ) -> None:
        await done_event.wait()
        await send_channel.aclose()

    async def _monitor_channels(
        self,
        channels: dict[str, Any],
        counter: CompletionCounter,
        *,
        interval: float = CHANNEL_MONITOR_INTERVAL,
    ) -> None:
        try:
            while True:
                with trio.move_on_after(interval) as scope:
                    await counter.completed.wait()
                if not scope.cancelled_caught:
                    break
                for name, channel in channels.items():
                    stats_fn = getattr(channel, "statistics", None)
                    if stats_fn is None:
                        continue
                    try:
                        stats = stats_fn()
                    except (trio.ClosedResourceError, RuntimeError):
                        continue
                    max_size = getattr(stats, "max_buffer_size", None)
                    current = getattr(stats, "current_buffer_used", None)
                    if not max_size:
                        continue
                    if current is None:
                        continue
                    if current >= max_size * CHANNEL_PRESSURE_FRACTION:
                        self.logger.verbose(
                            f"CHANNEL_PRESSURE name={name} load={current}/{max_size}"
                        )
        finally:
            self.logger.verbose("Channel monitor exiting")

    async def _watch_completion(
        self,
        counter: CompletionCounter,
        nursery: trio.Nursery,
        done_events: Iterable[trio.Event],
    ) -> None:
        await counter.completed.wait()
        self.logger.verbose("All documents processed, initiating graceful shutdown")
        with trio.move_on_after(30) as scope:
            for event in done_events:
                await event.wait()
            return
        if scope.cancelled_caught:
            self.logger.verbose(
                "Timeout during graceful shutdown, forcing cancellation"
            )
            nursery.cancel_scope.cancel()

    def _load_documents(self) -> list[DocTask]:
        payload = json.loads(self.config.input_artifact.read_text(encoding="utf-8"))
        docs: list[DocTask] = []
        for bucket in ("scraped_documents", "follow_up_documents"):
            entries = payload.get(bucket) or []
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                url = entry.get("url") or entry.get("source_url") or entry.get("link")
                if not url:
                    continue
                markdown = entry.get("markdown") or entry.get("content") or ""
                if not markdown:
                    continue
                metadata = entry.get("metadata") or entry.get("meta") or {}
                doc = DocTask(
                    doc_id=len(docs) + 1, url=url, content=markdown, metadata=metadata
                )
                docs.append(doc)
        return docs


# ---------------------------------------------------------------------------
# Completion counter helper


@dataclass
class CompletionCounter:
    total: int
    count: int = 0
    completed: trio.Event = field(default_factory=trio.Event)
    _lock: trio.Lock = field(default_factory=trio.Lock)

    async def increment(self) -> None:
        async with self._lock:
            self.count += 1
            if self.count >= self.total:
                self.completed.set()


# ---------------------------------------------------------------------------
# Prompt builders


def _build_router_prompt(task: DocTask) -> str:
    return (
        "You will classify documentation content.\n\n"
        f"URL: {task.url}\n\n"
        "--- Document Start ---\n"
        f"{task.content}\n"
        "--- Document End ---\n\n"
        "Respond with whether this is markdown prose or a Jupyter notebook export."
    )


def _build_markdown_prompt(item: WorkItem) -> str:
    feedback = (
        f"\nPrior review feedback to address: {item.review_feedback}\n"
        if item.review_feedback
        else "\n"
    )
    return f"""Clean and normalize the following markdown documentation.{feedback}
URL: {item.url}
--- Raw Markdown ---
{item.content}
--- End ---"""


def _build_notebook_prompt(item: WorkItem) -> str:
    feedback = (
        f"\nPrior review feedback to address: {item.review_feedback}\n"
        if item.review_feedback
        else "\n"
    )
    return f"""Convert the notebook (JSON or markdown export) into a standalone Python script with explanatory comments.{feedback}
URL: {item.url}
--- Notebook Content ---
{item.content}
--- End ---"""


def _build_review_prompt(doc: ProcessedDoc) -> str:
    summary = doc.summary or "N/A"
    return f"""Review the transformed document for quality. Approve only if it is accurate and well formatted.
Type: {doc.kind}
URL: {doc.url}
Summary: {summary}
--- Transformed Document ---
{doc.processed_text}
--- End ---
Return approved=true if the document is production ready."""


def _build_naming_prompt(doc: ReviewedDoc) -> str:
    hint = doc.title_hint or "N/A"
    return f"""Suggest a concise file slug and extension for the following documentation. Use kebab-case for the slug.
Type: {doc.kind}
URL: {doc.url}
Hint: {hint}
--- Content ---
{doc.processed_text}
--- End ---"""


def _safe_extension(ext: str, kind: str) -> str:
    ext = ext.strip()
    if not ext:
        return ".py" if kind == "notebook" else ".md"
    if not ext.startswith("."):
        ext = f".{ext}"
    if kind == "notebook" and ext.lower() not in {".py", ".txt"}:
        return ".py"
    if kind == "markdown" and ext.lower() not in {".md", ".markdown"}:
        return ".md"
    return ext


# ---------------------------------------------------------------------------
# CLI entry point


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the agent-based document cleaning pipeline."
    )
    parser.add_argument(
        "--config",
        default="configs/agent_pipeline_optimized.json",
        help="Pipeline configuration JSON path.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress console logs (still writes verbose log).",
    )
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"Config file not found: {config_path}", file=sys.stderr)
        return 1
    config = PipelineConfig.from_json(config_path)
    pipeline = Pipeline(config, quiet=args.quiet)
    trio_asyncio.run(pipeline.run)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry
    raise SystemExit(main())
