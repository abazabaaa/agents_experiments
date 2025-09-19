"""Structured logging helpers and Agent lifecycle hooks."""

from __future__ import annotations

import contextvars
import logging
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from agents import Agent
from agents.lifecycle import RunHooks
from agents.run_context import RunContextWrapper

TRACE_ID_VAR: contextvars.ContextVar[str | None] = contextvars.ContextVar(
    "agent_pipeline_trace_id", default=None
)


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

    def warning(self, message: str) -> None:
        """Log a warning message."""
        formatted = f"WARNING: {message.rstrip()}"
        if not self.quiet:
            print(formatted)
        self._write_verbose(formatted)

    def error(self, message: str) -> None:
        """Log an error message."""
        formatted = f"ERROR: {message.rstrip()}"
        if not self.quiet:
            print(formatted)
        self._write_verbose(formatted)

    def debug(self, message: str) -> None:
        """Log a debug message (verbose only)."""
        self._write_verbose(f"DEBUG: {message.rstrip()}")

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
        trace_id = TRACE_ID_VAR.get()
        formatted = message.rstrip("\n")
        if trace_id and not formatted.startswith("trace="):
            formatted = f"trace={trace_id} {formatted}"
        with self._lock:
            with self.verbose_path.open("a", encoding="utf-8") as stream:
                stream.write(formatted + "\n")


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


@dataclass
class AgentCallContext:
    """Context passed through Agents SDK runs to enrich telemetry."""

    logger: StructuredLogger
    workflow_name: str
    stage: str
    run_id: str
    doc_url: str
    metadata: dict[str, Any]
    trace_id: str | None = None
    prompt_excerpt: str | None = None


class LifecycleLoggingHooks(RunHooks[AgentCallContext]):
    """Log lifecycle events for Agents SDK runs with enhanced timing metrics."""

    def __init__(self, context: AgentCallContext) -> None:
        self._context = context
        self._timers: dict[str, float] = {}
        self._turn_count = 0

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
        # Track agent start time
        self._timers["agent_start"] = time.perf_counter()
        self._turn_count = 0

        ctx.logger.verbose(
            f"AGENT_EVENT event=agent_start stage={ctx.stage} run={ctx.run_id} "
            f"trace={ctx.trace_id} agent={agent.name} doc={ctx.doc_url}"
        )

    async def on_agent_end(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        output: Any,
    ) -> None:
        ctx = self._ensure_context(context)
        usage = context.usage

        # Calculate total agent execution time
        if "agent_start" in self._timers:
            duration = time.perf_counter() - self._timers["agent_start"]
            ctx.logger.info(
                f"AGENT_METRICS agent={agent.name} stage={ctx.stage} "
                f"duration={duration:.2f}s turns={self._turn_count} "
                f"requests={usage.requests} input_tokens={usage.input_tokens} "
                f"output_tokens={usage.output_tokens}"
            )

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
        # Track LLM call start
        self._timers["llm_start"] = time.perf_counter()
        self._turn_count += 1

        ctx.logger.verbose(
            f"AGENT_EVENT event=llm_start stage={ctx.stage} run={ctx.run_id} "
            f"trace={ctx.trace_id} agent={agent.name} doc={ctx.doc_url} "
            f"items={len(input_items)} turn={self._turn_count}"
        )

    async def on_llm_end(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        response: Any,
    ) -> None:
        ctx = self._ensure_context(context)

        # Calculate LLM response time
        if "llm_start" in self._timers:
            duration = time.perf_counter() - self._timers["llm_start"]
            ctx.logger.verbose(
                f"LLM_METRICS agent={agent.name} stage={ctx.stage} "
                f"duration={duration:.2f}s turn={self._turn_count}"
            )
            # Warn if LLM call is slow
            if duration > 30.0:
                ctx.logger.warning(
                    f"Slow LLM response: agent={agent.name} took {duration:.2f}s"
                )

        ctx.logger.verbose(
            f"AGENT_EVENT event=llm_end stage={ctx.stage} run={ctx.run_id} "
            f"trace={ctx.trace_id} agent={agent.name} doc={ctx.doc_url}"
        )

    async def on_tool_start(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        tool: Any,
    ) -> None:
        ctx = self._ensure_context(context)
        tool_name = getattr(tool, "name", "unknown")

        # Track tool execution start
        self._timers[f"tool_{tool_name}"] = time.perf_counter()

        ctx.logger.verbose(
            f"AGENT_EVENT event=tool_start stage={ctx.stage} run={ctx.run_id} "
            f"trace={ctx.trace_id} agent={agent.name} doc={ctx.doc_url} "
            f"tool={tool_name}"
        )

    async def on_tool_end(
        self,
        context: RunContextWrapper[AgentCallContext],
        agent: Agent[AgentCallContext],
        tool: Any,
        result: Any,
    ) -> None:
        ctx = self._ensure_context(context)
        tool_name = getattr(tool, "name", "unknown")

        # Calculate tool execution time
        timer_key = f"tool_{tool_name}"
        if timer_key in self._timers:
            duration = time.perf_counter() - self._timers[timer_key]
            ctx.logger.verbose(
                f"TOOL_METRICS agent={agent.name} tool={tool_name} "
                f"stage={ctx.stage} duration={duration:.2f}s"
            )
            # Warn if tool execution is slow
            if duration > 60.0:
                ctx.logger.warning(
                    f"Slow tool execution: {tool_name} took {duration:.2f}s"
                )

        # Abbreviate result for logging
        result_str = str(result)
        result_abbrev = (
            result_str[:100] + "..." if len(result_str) > 100 else result_str
        )

        ctx.logger.verbose(
            f"AGENT_EVENT event=tool_end stage={ctx.stage} run={ctx.run_id} "
            f"trace={ctx.trace_id} agent={agent.name} doc={ctx.doc_url} "
            f"tool={tool_name} result={result_abbrev}"
        )

    async def on_handoff(
        self,
        context: RunContextWrapper[AgentCallContext],
        from_agent: Agent[AgentCallContext],
        to_agent: Agent[AgentCallContext],
    ) -> None:
        ctx = self._ensure_context(context)
        ctx.logger.verbose(
            f"AGENT_EVENT event=handoff stage={ctx.stage} run={ctx.run_id} "
            f"trace={ctx.trace_id} from={from_agent.name} to={to_agent.name} "
            f"doc={ctx.doc_url}"
        )
