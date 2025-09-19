"""Utilities for capturing OpenAI Agents SDK tracing and logs locally."""

from __future__ import annotations

import atexit
import json
import logging
import threading
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from agents.tracing import add_trace_processor
from agents.tracing.processors import BatchTraceProcessor, TracingExporter
from agents.tracing.spans import Span
from agents.tracing.traces import Trace


class JSONLinesTraceExporter(TracingExporter):
    """Writes traces and spans to a newline-delimited JSON file."""

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path
        self._lock = threading.Lock()

    def export(self, items: list[Trace | Span[Any]]) -> None:  # pragma: no cover - exercised via integration
        payloads: list[dict[str, Any]] = []
        for item in items:
            exported = item.export()
            if exported is None:
                continue
            payload = dict(exported)
            payload.setdefault(
                "exported_at",
                datetime.now(UTC).isoformat(timespec="milliseconds"),
            )
            payloads.append(payload)

        if not payloads:
            return

        serialized = "\n".join(json.dumps(p, ensure_ascii=False, sort_keys=True) for p in payloads)
        with self._lock:
            self._file_path.parent.mkdir(parents=True, exist_ok=True)
            with self._file_path.open("a", encoding="utf-8") as handle:
                handle.write(serialized)
                handle.write("\n")
                handle.flush()


class ResilientFileHandler(logging.FileHandler):
    """File handler that reopens the stream if logging shuts it down early."""

    def __init__(self, filename: Path) -> None:
        super().__init__(filename, encoding="utf-8")

    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover - integration behaviour
        if self.stream is None or self.stream.closed:
            self.stream = self._open()
        try:
            super().emit(record)
        except ValueError:
            # Stream was unexpectedly closed; reopen and retry once.
            self.stream = self._open()
            super().emit(record)


_CONFIGURED = False
TRACE_DUMP_PATH: Path | None = None
LOG_FILE_PATH: Path | None = None


def configure_sdk_diagnostics(base_dir: Path | None = None) -> tuple[Path, Path]:
    """Configure local tracing and logging for the OpenAI Agents SDK."""

    global _CONFIGURED, TRACE_DUMP_PATH, LOG_FILE_PATH
    if _CONFIGURED and TRACE_DUMP_PATH and LOG_FILE_PATH:
        return TRACE_DUMP_PATH, LOG_FILE_PATH

    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    base_dir = base_dir or Path("logs/openai_sdk")
    trace_path = base_dir / "traces" / f"trace_dump-{timestamp}.jsonl"
    log_path = base_dir / "logs" / f"openai_agents-{timestamp}.log"

    exporter = JSONLinesTraceExporter(trace_path)
    trace_processor = BatchTraceProcessor(
        exporter,
        max_queue_size=16384,
        max_batch_size=256,
        schedule_delay=1.0,
        export_trigger_ratio=0.5,
    )
    add_trace_processor(trace_processor)

    base_dir.mkdir(parents=True, exist_ok=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    handler = ResilientFileHandler(log_path)
    handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    )

    monitored_loggers = []
    for name in ("openai.agents", "openai.agents.tracing"):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        monitored_loggers.append(logger)

    def _cleanup() -> None:  # pragma: no cover - executed during interpreter shutdown
        for logger in monitored_loggers:
            if handler in logger.handlers:
                logger.removeHandler(handler)
        handler.close()
        trace_processor.shutdown(timeout=5.0)

    atexit.register(_cleanup)

    TRACE_DUMP_PATH = trace_path
    LOG_FILE_PATH = log_path
    _CONFIGURED = True
    return trace_path, log_path
