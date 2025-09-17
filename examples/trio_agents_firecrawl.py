#!/usr/bin/env python3
"""
LLM-guided Firecrawl harvesting pipeline built on Trio.

This script performs the following high-level flow:

1. Map a documentation site to discover candidate URLs.
2. Batch-scrape the discovered URLs (concurrently, with configurable limits).
3. Hand off any remaining URLs to an LLM-powered review using Firecrawl's
   `extract` endpoint to decide whether a follow-up scrape is warranted.
4. Dispatch additional scrapes for URLs the LLM flags as relevant (also concurrently).

Progress is streamed to stdout as the pipeline runs, and the final results are
printed as formatted JSON (or optionally written to a file).

Usage example:

    uv run python scripts/firecrawl_trio_guided_scraper.py \
        --base-url https://lark-parser.readthedocs.io/en/stable/ \
        --objective "Collect all pages explaining Lark grammars" \
        --output guided_scrape.json

The script expects ``FIRECRAWL_API_KEY`` to be defined in the environment.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import random
import threading
import uuid
from dataclasses import dataclass, asdict, field
from functools import partial
from itertools import count
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    cast,
    Literal,
)
from urllib.parse import urldefrag, urlparse

import trio

from agents import Agent, Runner
from agents.items import (
    ItemHelpers,
    MessageOutputItem,
    RunItem,
    ToolCallItem,
    ToolCallOutputItem,
)
from agents.lifecycle import RunHooks
from agents.exceptions import AgentsException
from agents.model_settings import ModelSettings
from agents.run import RunConfig
from agents.run_context import RunContextWrapper
from openai.types.shared import Reasoning
from pydantic import BaseModel

from firecrawl import Firecrawl
from firecrawl.v2.types import Document, MapData
from dotenv import load_dotenv


# ---------------------------- Constants & Defaults ----------------------------

DEFAULT_BASE_URL = "https://lark-parser.readthedocs.io/en/stable/"


# ------------------------------- Data Contracts -------------------------------


@dataclass
class ScrapedDocument:
    """Captured output for a successfully scraped page."""

    url: str
    markdown: str
    metadata: Dict[str, Any]


@dataclass
class LLMDecision:
    """Structured response produced by the relevance evaluator."""

    url: str
    should_scrape: bool
    reason: str


@dataclass
class PipelineResult:
    """Aggregate summary returned at the end of the pipeline."""

    base_url: str
    mapped_urls: List[str]
    scraped_documents: List[ScrapedDocument]
    follow_up_documents: List[ScrapedDocument]
    llm_decisions: List[LLMDecision]
    skipped_urls: List[str]
    triage_runs: List["TriageRun"]
    prefix_suppressions: List["PrefixSuppression"]
    key_map: Dict[str, str]


@dataclass
class AgentConfig:
    """Tunable knobs for agent orchestration."""

    keygen_model: str = "gpt-5-nano"
    keygen_reasoning_effort: str = "minimal"
    keygen_verbosity: str = "low"
    triage_model: str = "gpt-5"
    triage_reasoning_effort: str = "medium"
    triage_verbosity: str = "medium"
    triage_timeout: float = 30.0
    triage_max_retries: int = 4
    triage_retry_initial_delay: float = 0.5
    triage_retry_backoff_base: float = 2.0
    triage_retry_max_delay: float = 60.0
    triage_retry_jitter_ratio: float = 0.25
    # Worker-thread concurrency for agent calls (to_thread.run_sync limiter)
    thread_concurrency: int = 8


@dataclass
class TriageRun:
    """Verbose telemetry for each triage agent execution."""

    attempt: int
    keys_considered: List[str]
    kept_keys: List[str]
    dropped_keys: List[str]
    prompt_excerpt: str
    raw_output: Any
    error: Optional[str] = None
    wait_seconds: Optional[float] = None
    model: str = ""


@dataclass
class PrefixSuppression:
    """Record of a URL prefix suppressed during triage."""

    prefix: str
    reason: str
    key: str
    url: str


class CircuitBreaker:
    """Simple async-aware circuit breaker for repeated failures."""

    def __init__(
        self,
        *,
        failure_threshold: int = 5,
        reset_timeout: float = 60.0,
    ) -> None:
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.last_failure_time: float | None = None
        self._lock = trio.Lock()

    async def call(self, async_fn: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        async with self._lock:
            if self.last_failure_time is not None:
                elapsed = trio.current_time() - self.last_failure_time
                if elapsed > self.reset_timeout:
                    self.failure_count = 0
                    self.last_failure_time = None
            if self.failure_count >= self.failure_threshold:
                raise RuntimeError(
                    f"Circuit breaker open after {self.failure_count} consecutive failures"
                )

        try:
            result = await async_fn(*args, **kwargs)
        except Exception:
            async with self._lock:
                self.failure_count += 1
                self.last_failure_time = trio.current_time()
            raise
        else:
            async with self._lock:
                self.failure_count = 0
                self.last_failure_time = None
            return result


class KeyAssignment(BaseModel):
    """Expected payload from the key generation agent."""

    key: str
    url: str
    notes: Optional[str] = None


class TriageDecisionPayload(BaseModel):
    """Agent-authored decision referencing previously issued keys."""

    key: str
    action: Literal["keep", "drop"]
    reason: str
    notes: Optional[str] = None


# -------------------------- Agent Context & Logging --------------------------


@dataclass
class AgentCallContext:
    """Shared context passed into Agents SDK runs for structured logging."""

    logger: "StructuredLogger"
    workflow_name: str
    stage: str
    run_id: str
    objective: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    trace_id: Optional[str] = None
    prompt_excerpt: Optional[str] = None


def truncate(value: str, limit: int = 200) -> str:
    """Return a single-line, length-limited representation of ``value``."""

    collapsed = " ".join(value.split())
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[:limit] + "..."


def describe_output(value: Any) -> str:
    """Summarize final agent outputs without logging entire payloads."""

    if value is None:
        return "None"
    if isinstance(value, str):
        return truncate(value, limit=160)
    if isinstance(value, list):
        return f"list(len={len(value)})"
    if isinstance(value, dict):
        keys = list(value.keys())
        preview = ",".join(keys[:5])
        more = "" if len(keys) <= 5 else f"+{len(keys) - 5}"
        suffix = f" {more}" if more else ""
        return f"dict(keys={preview}{suffix})"
    return type(value).__name__


def context_log(context: AgentCallContext, event: str, **fields: Any) -> None:
    """Emit a structured log line for an agent run event."""

    parts = [
        "AGENT_EVENT",
        f"event={event}",
        f"stage={context.stage}",
        f"run={context.run_id}",
    ]
    trace_id = context.trace_id
    if trace_id:
        parts.append(f"trace={trace_id}")
    metadata = context.metadata
    if metadata:
        for key, value in sorted(metadata.items()):
            if value is None:
                continue
            parts.append(f"meta_{key}={value}")
    for key, value in fields.items():
        if value is None or value == "":
            continue
        if isinstance(value, str):
            value = truncate(value)
        parts.append(f"{key}={value}")
    context.logger.verbose(" ".join(str(part) for part in parts))


# --------------------------------- Utilities ----------------------------------


class StructuredLogger:
    """
    Dual-channel logger keeping console output tidy while mirroring to disk.

    Thread-safe and safe to use from Trio tasks because it uses an OS thread lock.
    """

    def __init__(self, *, quiet: bool, verbose_path: Path) -> None:
        self.quiet = quiet
        self.verbose_path = verbose_path
        self._lock = threading.Lock()
        self._attached_logger_names: Set[str] = set()
        verbose_path.parent.mkdir(parents=True, exist_ok=True)
        # Reset file on each run
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
        """Attach a Python ``logging`` handler that mirrors logs into the verbose file."""

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
    """Bridge Python's logging records into our structured log sink."""

    def __init__(self, structured_logger: StructuredLogger) -> None:
        super().__init__()
        self._structured_logger = structured_logger

    def emit(self, record: logging.LogRecord) -> None:
        try:
            message = self.format(record)
        except Exception:  # noqa: BLE001
            message = record.getMessage()
        prefix = f"SDK_LOG level={record.levelname} logger={record.name}"
        self._structured_logger.verbose(f"{prefix} message={message}")


class LifecycleLoggingHooks(RunHooks[AgentCallContext]):
    """Run-level hooks that forward Agents SDK lifecycle events to the log."""

    def __init__(self, context: AgentCallContext) -> None:
        self._context = context

    def _ensure_context(self, wrapper: RunContextWrapper[AgentCallContext]) -> AgentCallContext:
        ctx = wrapper.context
        if ctx is not self._context:
            self._context = ctx
        return ctx

    async def on_agent_start(
        self, context: RunContextWrapper[AgentCallContext], agent: Agent[AgentCallContext]
    ) -> None:
        ctx = self._ensure_context(context)
        context_log(ctx, "agent_start", agent=agent.name, prompt=ctx.prompt_excerpt)

    async def on_agent_end(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        output: Any,
    ) -> None:
        ctx = self._ensure_context(context)
        usage = context.usage
        context_log(
            ctx,
            "agent_end",
            agent=agent.name,
            output_summary=describe_output(output),
            requests=usage.requests,
            input_tokens=usage.input_tokens,
            output_tokens=usage.output_tokens,
            total_tokens=usage.total_tokens,
        )

    async def on_llm_start(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        system_prompt: Optional[str],
        input_items: list[Any],
    ) -> None:
        ctx = self._ensure_context(context)
        context_log(
            ctx,
            "llm_start",
            agent=agent.name,
            system_prompt=system_prompt or "",
            input_items=len(input_items),
        )

    async def on_llm_end(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        response: Any,
    ) -> None:
        ctx = self._ensure_context(context)
        usage = getattr(response, "usage", None)
        preview = None
        outputs = getattr(response, "output", [])
        if outputs:
            try:
                preview = ItemHelpers.extract_last_content(outputs[-1])
            except Exception:  # noqa: BLE001
                preview = None
        context_log(
            ctx,
            "llm_end",
            agent=agent.name,
            response_id=getattr(response, "response_id", None),
            output_items=len(outputs),
            preview=preview,
            total_tokens=getattr(usage, "total_tokens", None),
            input_tokens=getattr(usage, "input_tokens", None),
            output_tokens=getattr(usage, "output_tokens", None),
        )

    async def on_handoff(
        self,
        context: RunContextWrapper[AgentCallContext],
        from_agent: Agent[AgentCallContext],
        to_agent: Agent[AgentCallContext],
    ) -> None:
        ctx = self._ensure_context(context)
        context_log(
            ctx,
            "handoff",
            source=from_agent.name,
            target=to_agent.name,
        )

    async def on_tool_start(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        tool: Any,
    ) -> None:
        ctx = self._ensure_context(context)
        context_log(ctx, "tool_start", agent=agent.name, tool=getattr(tool, "name", None))

    async def on_tool_end(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        tool: Any,
        result: str,
    ) -> None:
        ctx = self._ensure_context(context)
        context_log(
            ctx,
            "tool_end",
            agent=agent.name,
            tool=getattr(tool, "name", None),
            result=result,
        )


class CandidateKeyRegistry:
    """Manages stable key assignments for candidate URLs."""

    def __init__(self) -> None:
        self._url_to_key: Dict[str, str] = {}
        self._key_to_url: Dict[str, str] = {}
        self._slug_counts: Dict[str, int] = {}

    @property
    def key_map(self) -> Dict[str, str]:
        return dict(self._url_to_key)

    def get_key(self, url: str) -> Optional[str]:
        return self._url_to_key.get(url)

    def get_url(self, key: str) -> Optional[str]:
        return self._key_to_url.get(key)

    def ensure_assignments(
        self,
        assignments: Mapping[str, str],
        *,
        logger: StructuredLogger,
    ) -> None:
        for url, raw_key in assignments.items():
            self._assign(url, raw_key, logger=logger, source="agent")

    def ensure_fallback(self, url: str, *, logger: StructuredLogger) -> str:
        key = self._assign(url, self._fallback_key(url), logger=logger, source="fallback")
        return key

    def _assign(self, url: str, raw_key: str, *, logger: StructuredLogger, source: str) -> str:
        normalized_url = normalize_url(url)
        normalized_key = self._normalize_key(raw_key)
        if not normalized_key:
            normalized_key = self._fallback_key(normalized_url)
            source = "fallback"
        existing = self._url_to_key.get(normalized_url)
        if existing:
            return existing
        unique_key = self._dedupe_key(normalized_key, normalized_url)
        self._url_to_key[normalized_url] = unique_key
        self._key_to_url[unique_key] = normalized_url
        logger.verbose(
            f"KEY_ASSIGN source={source} url={normalized_url} key={unique_key} raw={raw_key!r}"
        )
        return unique_key

    def _normalize_key(self, key: str) -> str:
        cleaned = re.sub(r"[^A-Za-z0-9]+", "_", key.strip().upper())
        cleaned = cleaned.strip("_")
        return cleaned[:32]

    def _dedupe_key(self, key: str, url: str) -> str:
        candidate = key or "URL"
        counter = self._slug_counts.get(candidate, 0)
        result = candidate
        # Ensure keys are unique and stable
        while result in self._key_to_url and self._key_to_url[result] != url:
            counter += 1
            result = f"{candidate}_{counter}"
        self._slug_counts[candidate] = counter
        return result

    def _fallback_key(self, url: str) -> str:
        parsed = urlparse(url)
        segments = [segment for segment in parsed.path.split("/") if segment]
        candidate = segments[-1] if segments else (parsed.netloc or "URL")
        return self._normalize_key(candidate)


class AgentRuntime:
    """Thin wrapper around the Agents SDK suitable for Trio orchestration."""

    def __init__(self, config: AgentConfig, logger: StructuredLogger) -> None:
        self._config = config
        self._logger = logger
        self._rng = random.Random()
        self._thread_limiter = trio.CapacityLimiter(max(1, config.thread_concurrency))
        self._workflow_name = "firecrawl.trio_agents"
        self._run_counter = count(1)

        # Surface SDK diagnostics in the verbose log for transparency.
        self._logger.attach_python_logger("openai.agents", level=logging.DEBUG)
        self._logger.attach_python_logger("openai.agents.tracing", level=logging.INFO)

        self._key_agent = Agent[AgentCallContext](
            name="KeyGenerator",
            instructions=(
                "Generate short, human-memorable identifier strings for URLs. "
                "Respond with unique uppercase keys (<=12 characters) composed of letters, "
                "numbers, or underscores. Keys must be easy to type. Include the original URL "
                "and optionally a note clarifying the choice."
            ),
            model=self._config.keygen_model,
            model_settings=ModelSettings(
                reasoning=Reasoning(effort=self._config.keygen_reasoning_effort),
                verbosity=self._config.keygen_verbosity,
            ),
            output_type=list[KeyAssignment],
        )

        self._triage_agent = Agent[AgentCallContext](
            name="RelevanceTriage",
            instructions=(
                "Review candidate documentation pages referenced by stable keys. "
                "For each key decide whether to KEEP (scrape) or DROP (skip) based on the "
                "stated objective and already-scraped content. Provide a concise reason."
            ),
            model=self._config.triage_model,
            model_settings=ModelSettings(
                reasoning=Reasoning(effort=self._config.triage_reasoning_effort),
                verbosity=self._config.triage_verbosity,
            ),
            output_type=list[TriageDecisionPayload],
        )

    async def generate_keys(
        self,
        objective: str,
        urls: Sequence[str],
    ) -> List[KeyAssignment]:
        if not urls:
            # Ensure at least one checkpoint even on early return
            await trio.sleep(0)
            return []
        prompt = self._build_key_prompt(objective, urls)
        self._logger.verbose(f"KEY_AGENT_PROMPT\n{prompt}")
        try:
            result = await self._run_in_thread(
                self._key_agent,
                prompt,
                abandon_on_cancel=True,
                stage="keygen",
                objective=objective,
                metadata={"url_count": len(urls)},
            )
            payload = cast(List[KeyAssignment], result.final_output)
            self._logger.verbose(f"KEY_AGENT_OUTPUT items={len(payload)}")
            return payload or []
        except AgentsException as exc:
            self._logger.verbose(f"KEY_AGENT_ERROR {exc}")
            return []

    async def triage_once(
        self,
        objective: str,
        key_lines: Sequence[Tuple[str, str]],
        scraped_summary: str,
        suppressed_prefixes: Sequence[str],
    ) -> Tuple[List[TriageDecisionPayload], str]:
        if not key_lines:
            await trio.sleep(0)
            return [], ""
        prompt = self._build_triage_prompt(
            objective=objective,
            key_lines=key_lines,
            scraped_summary=scraped_summary,
            suppressed_prefixes=suppressed_prefixes,
        )
        self._logger.verbose(f"TRIAGE_PROMPT\n{prompt}")
        result = await self._run_in_thread(
            self._triage_agent,
            prompt,
            abandon_on_cancel=False,
            stage="triage",
            objective=objective,
            metadata={
                "candidate_count": len(key_lines),
                "suppressed_count": len(suppressed_prefixes),
            },
        )
        payload = cast(List[TriageDecisionPayload], result.final_output)
        self._logger.verbose(
            "TRIAGE_OUTPUT keys=%s" % ",".join(decision.key for decision in payload)
        )
        return payload or [], prompt

    async def _run_in_thread(
        self,
        agent: Agent[AgentCallContext],
        prompt: str,
        *,
        abandon_on_cancel: bool,
        stage: str,
        objective: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Any:
        context_data = self._make_context(stage, objective, metadata)
        context_data.prompt_excerpt = prompt[:400]
        run_config = self._build_run_config(context_data)
        hooks = LifecycleLoggingHooks(context_data)

        def _run_sync() -> Any:
            return Runner.run_sync(
                agent,
                prompt,
                context=context_data,
                hooks=hooks,
                run_config=run_config,
            )

        result = await trio.to_thread.run_sync(
            _run_sync,
            abandon_on_cancel=abandon_on_cancel,
            limiter=self._thread_limiter,
        )
        self._log_result(context_data, result)
        return result

    def _make_context(
        self, stage: str, objective: str, metadata: Optional[Dict[str, Any]] = None
    ) -> AgentCallContext:
        run_number = next(self._run_counter)
        run_id = f"{stage}-{run_number}"
        trace_id = f"trace_{uuid.uuid4().hex}"
        return AgentCallContext(
            logger=self._logger,
            workflow_name=self._workflow_name,
            stage=stage,
            run_id=run_id,
            objective=objective,
            metadata=dict(metadata or {}),
            trace_id=trace_id,
        )

    def _build_run_config(self, context: AgentCallContext) -> RunConfig:
        trace_metadata = {
            "stage": context.stage,
            "run_id": context.run_id,
            "objective": context.objective,
        }
        trace_metadata.update(context.metadata)
        return RunConfig(
            workflow_name=context.workflow_name,
            trace_id=context.trace_id,
            trace_metadata=trace_metadata,
        )

    def _log_result(self, context: AgentCallContext, result: Any) -> None:
        wrapper = getattr(result, "context_wrapper", None)
        usage_obj = wrapper.usage if wrapper else None
        last_agent = getattr(result, "last_agent", None)
        context_log(
            context,
            "run_result",
            final_agent=getattr(last_agent, "name", None),
            final_output=describe_output(getattr(result, "final_output", None)),
            new_items=len(getattr(result, "new_items", []) or []),
            raw_responses=len(getattr(result, "raw_responses", []) or []),
            requests=getattr(usage_obj, "requests", None) if usage_obj else None,
            input_tokens=getattr(usage_obj, "input_tokens", None) if usage_obj else None,
            output_tokens=getattr(usage_obj, "output_tokens", None) if usage_obj else None,
            total_tokens=getattr(usage_obj, "total_tokens", None) if usage_obj else None,
            response_id=getattr(result, "last_response_id", None),
        )
        for item in getattr(result, "new_items", []) or []:
            summary = self._summarize_run_item(item)
            context_log(context, "run_item", **summary)
        for response in getattr(result, "raw_responses", []) or []:
            usage_info = getattr(response, "usage", None)
            context_log(
                context,
                "raw_response",
                response_id=getattr(response, "response_id", None),
                output_items=len(getattr(response, "output", []) or []),
                total_tokens=getattr(usage_info, "total_tokens", None),
            )

    def _summarize_run_item(self, item: RunItem) -> Dict[str, Any]:
        summary: Dict[str, Any] = {
            "type": getattr(item, "type", type(item).__name__),
            "agent": getattr(getattr(item, "agent", None), "name", None),
        }
        if isinstance(item, MessageOutputItem):
            try:
                summary["text"] = truncate(ItemHelpers.text_message_output(item), limit=160)
            except Exception:  # noqa: BLE001
                summary["text"] = None
        raw_item = getattr(item, "raw_item", None)
        if raw_item is not None and summary.get("text") in (None, ""):
            try:
                summary["preview"] = truncate(str(raw_item), limit=160)
            except Exception:  # noqa: BLE001
                summary["preview"] = "<unprintable>"
        if isinstance(item, ToolCallItem):
            function = getattr(item.raw_item, "function", None)
            name = getattr(function, "name", None) if function is not None else None
            summary["tool_name"] = name or getattr(item.raw_item, "name", None)
        if isinstance(item, ToolCallOutputItem):
            summary["call_id"] = getattr(item.raw_item, "call_id", None)
            if getattr(item, "output", None) is not None:
                try:
                    summary["output_preview"] = truncate(str(item.output), limit=160)
                except Exception:  # noqa: BLE001
                    summary["output_preview"] = "<unprintable>"
        return summary

    @property
    def config(self) -> AgentConfig:
        """Expose the configuration used by this runtime."""
        return self._config

    def jitter_delay(self, base_delay: float) -> float:
        jitter_ratio = self._config.triage_retry_jitter_ratio
        if jitter_ratio <= 0:
            return base_delay
        delta = base_delay * jitter_ratio
        return base_delay + self._rng.uniform(-delta, delta)

    def _build_key_prompt(self, objective: str, urls: Sequence[str]) -> str:
        lines = ["Generate stable keys for the following URLs."]
        lines.append(f"Objective: {objective}")
        lines.append("Return one entry per URL.")
        for index, url in enumerate(urls, start=1):
            lines.append(f"{index}. {url}")
        lines.append(
            "Focus on short, descriptive keys (<=12 chars) using letters, numbers, underscore."
        )
        return "\n".join(lines)

    def _build_triage_prompt(
        self,
        *,
        objective: str,
        key_lines: Sequence[Tuple[str, str]],
        scraped_summary: str,
        suppressed_prefixes: Sequence[str],
    ) -> str:
        lines = [
            "You evaluate whether to KEEP (scrape now) or DROP (skip) URLs.",
            f"Objective: {objective}",
            "Already scraped (recent pages):",
            scraped_summary or "(none)",
            "",
            "Do not propose new URLs; only classify provided keys.",
        ]
        if suppressed_prefixes:
            lines.append(
                "Prefixes already suppressed: "
                + ", ".join(suppressed_prefixes[:10])
                + ("..." if len(suppressed_prefixes) > 10 else "")
            )
        lines.append("Candidates (key -> url):")
        for key, url in key_lines:
            lines.append(f"- {key}: {url}")
        lines.append(
            "Output a list where each item has fields key, action (keep|drop), and reason."
        )
        return "\n".join(lines)


# ------------------------------ Firecrawl Wrapper -----------------------------


class ManagedFirecrawlClient:
    """Async context manager that wraps Firecrawl with Trio-friendly semantics."""

    def __init__(self, api_key: str, thread_limiter: trio.CapacityLimiter) -> None:
        self._client = Firecrawl(api_key=api_key)
        self._thread_limiter = thread_limiter
        self._closed = False

    async def __aenter__(self) -> "ManagedFirecrawlClient":
        return self

    async def __aexit__(self, *exc_info: Any) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        if not self._closed:
            self._closed = True
            # allow pending operations to progress
            await trio.sleep(0)

    def _ensure_open(self) -> None:
        if self._closed:
            raise trio.ClosedResourceError("Firecrawl client is closed")

    async def map(self, base_url: str, *, limit: int) -> MapData:
        self._ensure_open()
        fn = partial(self._client.map, base_url, limit=limit)
        return await trio.to_thread.run_sync(
            fn,
            abandon_on_cancel=False,
            limiter=self._thread_limiter,
        )

    async def batch_scrape(
        self,
        urls: Sequence[str],
        *,
        formats: Sequence[str],
        only_main_content: bool,
        max_age: Optional[int],
        poll_interval: int,
        wait_timeout: int,
    ) -> Any:
        self._ensure_open()
        fn = partial(
            self._client.batch_scrape,
            list(urls),
            formats=formats,
            only_main_content=only_main_content,
            max_age=max_age,
            poll_interval=poll_interval,
            wait_timeout=wait_timeout,
        )
        return await trio.to_thread.run_sync(
            fn,
            abandon_on_cancel=False,
            limiter=self._thread_limiter,
        )


class ScrapingCoordinator:
    """Coordinates pipeline stage transitions using Trio events."""

    def __init__(self) -> None:
        self._mapping_done = trio.Event()
        self._initial_scrape_done = trio.Event()

    async def wait_for_mapping(self) -> None:
        await self._mapping_done.wait()

    async def signal_mapping_complete(self) -> None:
        self._mapping_done.set()

    async def wait_for_initial_scrape(self) -> None:
        await self._initial_scrape_done.wait()

    async def signal_initial_scrape_complete(self) -> None:
        self._initial_scrape_done.set()


# ------------------------------ CLI & Arguments -------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Map, scrape, and LLM-triage documentation with Firecrawl + Trio",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Root URL to map and scrape")
    parser.add_argument(
        "--objective",
        required=True,
        help="Human-readable objective that guides the relevance LLM",
    )
    parser.add_argument(
        "--map-limit", type=int, default=250, help="Maximum URLs to return from map"
    )
    parser.add_argument("--batch-size", type=int, default=50, help="URLs per batch scrape job")
    parser.add_argument(
        "--eval-batch-size", type=int, default=15, help="URLs evaluated per LLM extract call"
    )
    parser.add_argument(
        "--formats",
        nargs="+",
        default=["markdown"],
        help="Firecrawl output formats to request during scraping",
    )
    parser.add_argument(
        "--no-main-content", action="store_true", help="Disable onlyMainContent scraping option"
    )
    parser.add_argument("--max-age", type=int, help="Reuse cached scrapes newer than this (ms)")
    parser.add_argument(
        "--poll-interval", type=int, default=2, help="Seconds between job status polls"
    )
    parser.add_argument("--job-timeout", type=int, default=300, help="Timeout (s) for scrape jobs")
    parser.add_argument(
        "--eval-timeout", type=int, default=180, help="Timeout (s) for LLM extract jobs"
    )
    parser.add_argument(
        "--relevance-prompt",
        default=(
            "Decide whether each remaining URL should be scraped to satisfy the objective."
            " Answer yes if the page is likely to contain new or still-needed information,"
            " otherwise answer no. Provide a short reason."
        ),
        help="Instruction appended to the LLM prompt when triaging URLs",
    )
    parser.add_argument(
        "--output", help="Optional path to write the final JSON payload instead of stdout"
    )
    parser.add_argument("--quiet", action="store_true", help="Suppress intermediate progress logs")
    parser.add_argument(
        "--log-file",
        default="log.txt",
        help="Path to write verbose log output",
    )
    # Concurrency & control
    parser.add_argument(
        "--scrape-concurrency",
        type=int,
        default=3,
        help="Maximum number of concurrent Firecrawl batch-scrape jobs",
    )
    parser.add_argument(
        "--thread-concurrency",
        type=int,
        default=8,
        help="Maximum concurrent worker threads for blocking API calls (agents & Firecrawl)",
    )
    parser.add_argument(
        "--progress-interval",
        type=float,
        default=15.0,
        help="Seconds between progress log updates while scraping batches",
    )
    parser.add_argument(
        "--prefix-depth",
        type=int,
        default=2,
        help="Number of path segments to include when deriving suppression prefixes",
    )
    return parser.parse_args()


# ----------------------------- Generic Helpers --------------------------------


def normalize_url(url: str) -> str:
    """Normalize a URL by removing trailing slashes and fragments."""
    stripped = url.strip()
    if not stripped:
        return stripped
    no_fragment, _ = urldefrag(stripped)
    if no_fragment.endswith("/"):
        return no_fragment[:-1]
    return no_fragment


def chunked(seq: Sequence[str], size: int) -> Iterable[List[str]]:
    """Yield successive chunks of size `size` from `seq`."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    for index in range(0, len(seq), size):
        yield list(seq[index : index + size])


def summarize_list(values: Sequence[str], limit: int = 5) -> str:
    """Friendly summary representation of a list with ellipsis."""
    items = list(values)
    if not items:
        return "[]"
    if len(items) <= limit:
        return "[" + ", ".join(items) + "]"
    remaining = len(items) - limit
    return "[" + ", ".join(items[:limit]) + f", … ({remaining} more)]"


def summarize_scraped(scraped: Sequence[ScrapedDocument]) -> str:
    """Emit a readable tail summary of scraped URLs for the triage prompt."""
    if not scraped:
        return "(no pages scraped yet)"
    top = [f"- {item.url}" for item in scraped[-20:]]
    if len(scraped) > 20:
        top.insert(0, f"- ... ({len(scraped) - 20} earlier pages omitted)")
    return "\n".join(top)


def extract_doc_url(doc: Document, fallback: str) -> str:
    """Best-effort extraction of a document's canonical source URL."""
    if hasattr(doc, "metadata_typed"):
        meta = doc.metadata_typed
        source_value = getattr(meta, "source_url", None)
        if isinstance(source_value, str) and source_value:
            return normalize_url(source_value)
        direct_value = getattr(meta, "url", None)
        if isinstance(direct_value, str) and direct_value:
            return normalize_url(direct_value)
    metadata_dict = doc.metadata_dict if hasattr(doc, "metadata_dict") else {}
    for key in ("source_url", "sourceURL", "url"):
        value = metadata_dict.get(key)
        if isinstance(value, str) and value:
            return normalize_url(value)
        if value:
            return normalize_url(str(value))
    return normalize_url(fallback)


def document_to_record(doc: Document, fallback_url: str) -> ScrapedDocument:
    """Convert a Firecrawl Document to our ScrapedDocument record."""
    url = extract_doc_url(doc, fallback_url)
    markdown = (
        getattr(doc, "markdown", None)
        or getattr(doc, "html", None)
        or getattr(doc, "raw_html", None)
        or ""
    )
    metadata = doc.metadata_dict if hasattr(doc, "metadata_dict") else {}
    if not url:
        url = normalize_url(fallback_url)
    return ScrapedDocument(url=url, markdown=markdown, metadata=metadata)


def derive_prefix(url: str, depth: int = 2) -> str:
    """
    Derive a suppression prefix from a URL consisting of scheme://host + leading path segments.
    Example (depth=2):
      https://example.com/a/b/c -> https://example.com/a/b
    """
    parsed = urlparse(url)
    segments = [segment for segment in parsed.path.split("/") if segment]
    limited_segments = segments[: max(0, depth)]
    path = "/".join(limited_segments)
    if path:
        path = "/" + path
    return f"{parsed.scheme}://{parsed.netloc}{path}"


# ------------------------------- Core Pipeline --------------------------------


async def map_site(
    client: ManagedFirecrawlClient,
    args: argparse.Namespace,
    logger: StructuredLogger,
) -> List[str]:
    """Use Firecrawl's `map` to discover URLs under the base URL."""
    logger.info(f"🔍 Mapping {args.base_url} (limit={args.map_limit})")
    map_data: MapData = await client.map(args.base_url, limit=args.map_limit)
    discovered: List[str] = []
    seen: Set[str] = set()
    links = getattr(map_data, "links", []) or []
    for entry in links:
        url = getattr(entry, "url", None)
        if not url:
            continue
        normalized = normalize_url(url)
        if normalized in seen:
            continue
        seen.add(normalized)
        discovered.append(normalized)
    if args.base_url:
        normalized_base = normalize_url(args.base_url)
        if normalized_base and normalized_base not in seen:
            discovered.insert(0, normalized_base)
    logger.info(f"🗺️  Discovered {len(discovered)} URLs")
    logger.verbose(
        "MAP_LINKS "
        + json.dumps({"count": len(discovered), "sample": discovered[:10]}, ensure_ascii=False)
    )
    return discovered


async def batch_scrape(
    client: ManagedFirecrawlClient,
    batch: Sequence[str],
    args: argparse.Namespace,
    logger: StructuredLogger,
) -> Tuple[List[ScrapedDocument], List[str]]:
    """Submit one Firecrawl batch-scrape job and collect results."""
    if not batch:
        return [], []
    logger.info(f"📦 Scraping batch of {len(batch)} URLs")
    try:
        job = await client.batch_scrape(
            batch,
            formats=args.formats,
            only_main_content=not args.no_main_content,
            max_age=args.max_age,
            poll_interval=args.poll_interval,
            wait_timeout=args.job_timeout,
        )
    except Exception as exc:  # noqa: BLE001 - surfaced in log
        logger.info(f"❌ Batch scrape failed: {exc}")
        logger.verbose(f"BATCH_ERROR batch={batch} error={exc}")
        return [], [normalize_url(url) for url in batch]

    records: List[ScrapedDocument] = []
    scraped_urls: Set[str] = set()
    for doc in getattr(job, "data", []) or []:
        record = document_to_record(doc, fallback_url=batch[0])
        records.append(record)
        scraped_urls.add(record.url)
    missing = [normalize_url(url) for url in batch if normalize_url(url) not in scraped_urls]
    logger.info(
        f"✅ Batch status={getattr(job, 'status', 'unknown')} completed={getattr(job, 'completed', '?')}/{getattr(job, 'total', '?')}"
    )
    logger.verbose(
        "BATCH_SUMMARY "
        + json.dumps(
            {
                "requested": list(batch),
                "records": len(records),
                "missing": missing,
                "status": getattr(job, "status", "unknown"),
            },
            ensure_ascii=False,
        )
    )
    return records, missing


async def scrape_urls_concurrently(
    client: ManagedFirecrawlClient,
    urls: Sequence[str],
    args: argparse.Namespace,
    logger: StructuredLogger,
    *,
    progress_interval: float,
) -> Tuple[List[ScrapedDocument], List[str], Dict[str, Exception]]:
    """
    Scrape all given URLs by chunking into Firecrawl batches and running multiple
    batch jobs concurrently, limited by --scrape-concurrency.
    """
    all_batches = list(chunked(list(dict.fromkeys(urls)), args.batch_size))
    if not all_batches:
        await trio.sleep(0)
        return [], [], {}

    sem = trio.Semaphore(max(1, args.scrape_concurrency))
    scraped_docs: List[ScrapedDocument] = []
    failed_urls: List[str] = []
    errors: Dict[str, Exception] = {}
    result_lock = trio.Lock()
    progress_lock = trio.Lock()
    stop_event = trio.Event()
    completed = 0
    total_batches = len(all_batches)

    async def monitor_progress() -> None:
        while True:
            with trio.move_on_after(progress_interval) as scope:
                await stop_event.wait()
            if not scope.cancelled_caught:
                break
            async with progress_lock:
                logger.info(
                    f"Progress: {completed}/{total_batches} batches completed"
                )

    async def worker(batch: List[str]) -> None:
        nonlocal completed
        async with sem:
            try:
                recs, missing = await batch_scrape(client, batch, args, logger)
                async with result_lock:
                    scraped_docs.extend(recs)
                    failed_urls.extend(missing)
            except Exception as exc:  # noqa: BLE001
                errors[",".join(batch)] = exc
                raise
            finally:
                async with progress_lock:
                    completed += 1
                    if completed >= total_batches:
                        stop_event.set()

    logger.info(
        f"🚀 Launching {len(all_batches)} batches with concurrency={args.scrape_concurrency}"
    )

    try:
        async with trio.open_nursery() as nursery:
            nursery.start_soon(monitor_progress)
            for batch in all_batches:
                nursery.start_soon(worker, batch)
    except* Exception as excgroup:
        logger.info(f"Some batches failed: {excgroup}")
    finally:
        stop_event.set()

    return scraped_docs, failed_urls, errors


async def ensure_keys_for_candidates(
    registry: CandidateKeyRegistry,
    runtime: AgentRuntime,
    objective: str,
    urls: Sequence[str],
    logger: StructuredLogger,
) -> None:
    """Ensure each URL has a stable key assignment, generating them in bulk if needed."""
    normalized = [normalize_url(url) for url in urls if url]
    missing = [url for url in normalized if registry.get_key(url) is None]
    if not missing:
        # checkpoint to play nicely with Trio even if nothing to do
        await trio.sleep(0)
        return

    assignments = await runtime.generate_keys(objective, missing)
    mapping: Dict[str, str] = {}
    for assignment in assignments:
        normalized_url = normalize_url(assignment.url)
        if normalized_url in missing and assignment.key:
            mapping[normalized_url] = assignment.key
            if assignment.notes:
                logger.verbose(
                    f"KEY_AGENT_NOTE url={normalized_url} key={assignment.key} notes={assignment.notes}"
                )

    if mapping:
        registry.ensure_assignments(mapping, logger=logger)

    # Fallback for any missing mappings
    for url in missing:
        if registry.get_key(url) is None:
            registry.ensure_fallback(url, logger=logger)


async def triage_candidates(
    runtime: AgentRuntime,
    registry: CandidateKeyRegistry,
    candidates: Sequence[str],
    scraped: Sequence[ScrapedDocument],
    args: argparse.Namespace,
    logger: StructuredLogger,
    suppressed_prefixes: Set[str],
    triage_runs: List[TriageRun],
    prefix_records: List[PrefixSuppression],
    *,
    prefix_depth: int,
    config: AgentConfig,
    breaker: CircuitBreaker,
    coordinator: ScrapingCoordinator,
) -> List[LLMDecision]:
    """
    Ask the LLM to decide KEEP/DROP for candidate URLs, honoring previous suppressions.
    Applies exponential backoff with jitter/retries on failures/timeouts.
    """
    await coordinator.wait_for_mapping()
    await coordinator.wait_for_initial_scrape()

    # Normalize & filter already-suppressed
    normalized_candidates: List[str] = []
    for url in candidates:
        normalized = normalize_url(url)
        if not normalized:
            continue
        if derive_prefix(normalized, depth=prefix_depth) in suppressed_prefixes:
            logger.verbose(f"TRIAGE_SKIP_SUPPRESSED url={normalized}")
            continue
        normalized_candidates.append(normalized)

    # Ensure stable keys before triage
    await ensure_keys_for_candidates(
        registry,
        runtime,
        args.objective,
        normalized_candidates,
        logger,
    )

    scraped_summary = summarize_scraped(scraped)
    decisions: List[LLMDecision] = []
    max_attempts = config.triage_max_retries + 1

    for chunk in chunked(normalized_candidates, args.eval_batch_size):
        key_lines: List[Tuple[str, str]] = []
        for url in chunk:
            key = registry.get_key(url)
            if not key:
                key = registry.ensure_fallback(url, logger=logger)
            key_lines.append((key, url))

        if not key_lines:
            continue

        logger.info(f"🧠 Triage {len(key_lines)} candidates")

        delay = config.triage_retry_initial_delay
        attempt = 0

        while True:
            attempt += 1
            payload: List[TriageDecisionPayload] = []
            prompt_excerpt = ""
            error_message: Optional[str] = None

            # Timeout the LLM call itself
            async def run_triage() -> Tuple[List[TriageDecisionPayload], str]:
                return await runtime.triage_once(
                    objective=args.objective,
                    key_lines=key_lines,
                    scraped_summary=scraped_summary,
                    suppressed_prefixes=sorted(suppressed_prefixes),
                )

            with trio.move_on_after(args.eval_timeout) as cancel_scope:
                try:
                    payload, prompt = await breaker.call(run_triage)
                    prompt_excerpt = prompt[:400]
                except AgentsException as exc:
                    error_message = str(exc)
                except Exception as exc:  # noqa: BLE001
                    error_message = str(exc)

            if cancel_scope.cancelled_caught and error_message is None:
                error_message = f"timeout after {args.eval_timeout}s"

            payload_dump = [item.model_dump() for item in payload]

            if payload and error_message is None:
                payload_map = {item.key.strip().upper(): item for item in payload}
                kept_keys: List[str] = []
                dropped_keys: List[str] = []

                for key, url in key_lines:
                    lookup_key = key.strip().upper()
                    item = payload_map.get(lookup_key)
                    if not item:
                        reason = "Agent response missing key"
                        decisions.append(LLMDecision(url=url, should_scrape=False, reason=reason))
                        prefix = derive_prefix(url, depth=prefix_depth)
                        suppressed_prefixes.add(prefix)
                        prefix_records.append(
                            PrefixSuppression(prefix=prefix, reason=reason, key=lookup_key, url=url)
                        )
                        dropped_keys.append(lookup_key)
                        continue

                    should_keep = item.action.lower() == "keep"
                    reason = item.reason.strip() or "(no reason provided)"
                    decisions.append(LLMDecision(url=url, should_scrape=should_keep, reason=reason))
                    if should_keep:
                        kept_keys.append(lookup_key)
                    else:
                        dropped_keys.append(lookup_key)
                        prefix = derive_prefix(url, depth=prefix_depth)
                        suppressed_prefixes.add(prefix)
                        prefix_records.append(
                            PrefixSuppression(prefix=prefix, reason=reason, key=lookup_key, url=url)
                        )

                triage_runs.append(
                    TriageRun(
                        attempt=attempt,
                        keys_considered=[key for key, _ in key_lines],
                        kept_keys=kept_keys,
                        dropped_keys=dropped_keys,
                        prompt_excerpt=prompt_excerpt,
                        raw_output=payload_dump,
                        error=None,
                        wait_seconds=None,
                        model=config.triage_model,
                    )
                )

                logger.info(
                    "🧠 triage keep=%s drop=%s"
                    % (
                        summarize_list(kept_keys),
                        summarize_list(dropped_keys),
                    )
                )
                break

            # Failure path -> schedule retry or mark dropped
            triage_runs.append(
                TriageRun(
                    attempt=attempt,
                    keys_considered=[key for key, _ in key_lines],
                    kept_keys=[],
                    dropped_keys=[],
                    prompt_excerpt=prompt_excerpt,
                    raw_output=payload_dump,
                    error=error_message or "triage failed",
                    wait_seconds=None,
                    model=config.triage_model,
                )
            )

            if attempt >= max_attempts:
                logger.info("⚠️ triage failed; marking candidates as skipped")
                for key, url in key_lines:
                    reason = error_message or "triage failure"
                    decisions.append(LLMDecision(url=url, should_scrape=False, reason=reason))
                    prefix = derive_prefix(url, depth=prefix_depth)
                    suppressed_prefixes.add(prefix)
                    prefix_records.append(
                        PrefixSuppression(prefix=prefix, reason=reason, key=key, url=url)
                    )
                break

            wait_seconds = min(config.triage_retry_max_delay, delay)
            wait_seconds = max(0.0, runtime.jitter_delay(wait_seconds))
            triage_runs[-1].wait_seconds = wait_seconds
            logger.info(
                f"⏳ triage retry in {wait_seconds:.1f}s (attempt {attempt}/{max_attempts})"
            )
            await trio.sleep(wait_seconds)
            delay = min(
                config.triage_retry_max_delay,
                delay * config.triage_retry_backoff_base,
            )

    return decisions


# -------------------------------- Orchestration -------------------------------


async def orchestrate(args: argparse.Namespace) -> PipelineResult:
    """Run the full mapping → scraping → triage → follow-up scraping pipeline."""
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("FIRECRAWL_API_KEY is not set", file=sys.stderr)
        raise SystemExit(1)

    # Validation
    if args.batch_size <= 0:
        raise SystemExit("--batch-size must be positive")
    if args.eval_batch_size <= 0:
        raise SystemExit("--eval-batch-size must be positive")
    if args.scrape_concurrency <= 0:
        raise SystemExit("--scrape-concurrency must be positive")
    if args.thread_concurrency <= 0:
        raise SystemExit("--thread-concurrency must be positive")
    if args.prefix_depth < 0:
        raise SystemExit("--prefix-depth cannot be negative")
    if args.progress_interval <= 0:
        raise SystemExit("--progress-interval must be positive")

    # Initialize core components
    logger = StructuredLogger(quiet=args.quiet, verbose_path=Path(args.log_file))
    config = AgentConfig(thread_concurrency=args.thread_concurrency)
    runtime = AgentRuntime(config, logger)
    registry = CandidateKeyRegistry()
    thread_limiter = trio.CapacityLimiter(max(1, args.thread_concurrency))
    coordinator = ScrapingCoordinator()
    triage_breaker = CircuitBreaker(
        failure_threshold=3,
        reset_timeout=max(float(args.eval_timeout), 1.0) * 2,
    )

    logger.verbose(f"AGENT_CONFIG {config}")

    suppressed_prefixes: Set[str] = set()
    triage_runs: List[TriageRun] = []
    prefix_records: List[PrefixSuppression] = []

    scraped_docs: List[ScrapedDocument] = []
    scraped_set: Set[str] = set()
    failed_urls: List[str] = []
    decisions: List[LLMDecision] = []
    follow_up_docs: List[ScrapedDocument] = []
    skipped_due_to_triage: Set[str] = set()
    remaining_set: Set[str] = set()

    async with ManagedFirecrawlClient(api_key=cast(str, api_key), thread_limiter=thread_limiter) as client:
        # 1) Map the site
        mapped_urls = await map_site(client, args, logger)
        pending: List[str] = list(mapped_urls)
        await coordinator.signal_mapping_complete()

        # 2) Initial scrape (concurrent batches)
        if pending:
            batch_scraped, batch_missing, batch_errors = await scrape_urls_concurrently(
                client,
                pending,
                args,
                logger,
                progress_interval=args.progress_interval,
            )
            scraped_docs.extend(batch_scraped)
            failed_urls.extend(batch_missing)

            if batch_errors:
                logger.info(f"⚠️ Batch errors encountered: {list(batch_errors.keys())}")
                for label, exc in batch_errors.items():
                    logger.verbose(f"BATCH_ERROR {label}: {exc}")

            # Update suppression state for any successfully scraped prefixes
            for record in batch_scraped:
                scraped_set.add(normalize_url(record.url))
                suppressed_prefixes.discard(derive_prefix(record.url, depth=args.prefix_depth))

        await coordinator.signal_initial_scrape_complete()

        # Collect remaining set for triage consideration
        remaining_set = {
            url
            for url in failed_urls
            if url and derive_prefix(url, depth=args.prefix_depth) not in suppressed_prefixes
        }

        # 3) Triage + 4) Follow-up scrapes (concurrent)
        if remaining_set:
            decisions = await triage_candidates(
                runtime,
                registry,
                sorted(remaining_set),
                scraped_docs,
                args,
                logger,
                suppressed_prefixes,
                triage_runs,
                prefix_records,
                prefix_depth=args.prefix_depth,
                config=config,
                breaker=triage_breaker,
                coordinator=coordinator,
            )

            yes_urls: List[str] = []
            for decision in decisions:
                normalized = normalize_url(decision.url)
                if not normalized:
                    continue
                if decision.should_scrape:
                    if normalized not in scraped_set:
                        yes_urls.append(normalized)
                else:
                    skipped_due_to_triage.add(normalized)
                    remaining_set.discard(normalized)

            yes_urls = list(dict.fromkeys(yes_urls))
            filtered_yes_urls = [
                url
                for url in yes_urls
                if derive_prefix(url, depth=args.prefix_depth) not in suppressed_prefixes
            ]

            if filtered_yes_urls:
                follow_scraped, follow_missing, follow_errors = await scrape_urls_concurrently(
                    client,
                    filtered_yes_urls,
                    args,
                    logger,
                    progress_interval=args.progress_interval,
                )
                follow_up_docs.extend(follow_scraped)
                for record in follow_scraped:
                    normalized_url = normalize_url(record.url)
                    if normalized_url:
                        scraped_set.add(normalized_url)
                        remaining_set.discard(normalized_url)
                        suppressed_prefixes.discard(
                            derive_prefix(normalized_url, depth=args.prefix_depth)
                        )
                for url in follow_missing:
                    normalized = normalize_url(url)
                    if not normalized:
                        continue
                    if derive_prefix(normalized, depth=args.prefix_depth) in suppressed_prefixes:
                        continue
                    remaining_set.add(normalized)
                if follow_errors:
                    logger.info(f"⚠️ Follow-up batch errors: {list(follow_errors.keys())}")
                    for label, exc in follow_errors.items():
                        logger.verbose(f"FOLLOWUP_ERROR {label}: {exc}")

    skipped_urls = sorted(
        set(remaining_set)
        | {normalize_url(url) for url in skipped_due_to_triage if url}
        - {normalize_url(doc.url) for doc in follow_up_docs if doc.url}
    )

    if prefix_records:
        logger.blank_line()
        logger.info(
            "🚫 Suppressed prefixes: "
            + summarize_list([record.prefix for record in prefix_records], limit=5)
        )

    logger.blank_line()
    logger.info(
        "✅ Completed. scraped=%d follow_up=%d skipped=%d"
        % (len(scraped_docs), len(follow_up_docs), len(skipped_urls))
    )

    return PipelineResult(
        base_url=args.base_url,
        mapped_urls=mapped_urls,
        scraped_documents=scraped_docs,
        follow_up_documents=follow_up_docs,
        llm_decisions=decisions,
        skipped_urls=skipped_urls,
        triage_runs=triage_runs,
        prefix_suppressions=prefix_records,
        key_map=registry.key_map,
    )


def result_to_json_ready(result: PipelineResult) -> Dict[str, Any]:
    """Convert the pipeline result to a JSON-serializable dictionary."""
    return {
        "base_url": result.base_url,
        "mapped_urls": result.mapped_urls,
        "scraped_documents": [asdict(doc) for doc in result.scraped_documents],
        "follow_up_documents": [asdict(doc) for doc in result.follow_up_documents],
        "llm_decisions": [asdict(decision) for decision in result.llm_decisions],
        "skipped_urls": result.skipped_urls,
        "triage_runs": [asdict(run) for run in result.triage_runs],
        "prefix_suppressions": [asdict(entry) for entry in result.prefix_suppressions],
        "key_map": result.key_map,
    }


# --------------------------------- Entrypoint ---------------------------------


async def async_main() -> None:
    args = parse_args()
    result = await orchestrate(args)
    payload = result_to_json_ready(result)
    serialized = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(serialized, encoding="utf-8")
        if not args.quiet:
            print(f"💾 Wrote results to {output_path}")
    else:
        print(serialized)


def main() -> None:
    load_dotenv()
    trio.run(async_main)


if __name__ == "__main__":
    main()
