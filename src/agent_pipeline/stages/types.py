"""Shared data structures used by pipeline stages."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

import trio


@dataclass(slots=True)
class WorkflowContext:
    """Typed context shared across agent runs.

    This carries immutable pipeline-level metadata that dynamic instruction
    functions can access.
    """

    workflow_name: str
    config_path: Path
    trace_metadata: Mapping[str, Any]


@dataclass(slots=True)
class DocumentContext:
    """Per-document context injected into agent runs."""

    doc_id: int
    url: str
    metadata: Mapping[str, Any]


@dataclass(slots=True)
class DocTask:
    doc_id: int
    url: str
    content: str
    metadata: dict[str, Any]


@dataclass(slots=True)
class WorkItem:
    doc_id: int
    url: str
    content: str
    metadata: dict[str, Any]
    kind: Literal["markdown", "notebook"]
    attempts: int = 0
    review_feedback: str | None = None


@dataclass(slots=True)
class ProcessedDoc:
    doc_id: int
    url: str
    kind: Literal["markdown", "notebook"]
    processed_text: str
    metadata: dict[str, Any]
    attempts: int
    summary: str | None = None


@dataclass(slots=True)
class ReviewedDoc:
    doc_id: int
    url: str
    kind: Literal["markdown", "notebook"]
    processed_text: str
    metadata: dict[str, Any]
    title_hint: str | None


@dataclass(slots=True)
class NamedDoc:
    doc_id: int
    url: str
    file_slug: str
    extension: str
    processed_text: str
    metadata: dict[str, Any]


@dataclass(slots=True)
class CompletionCounter:
    """Track total completions and signal when all work is done."""

    total: int
    count: int = 0
    completed: trio.Event = field(default_factory=trio.Event)
    _lock: trio.Lock = field(default_factory=trio.Lock)

    async def increment(self) -> None:
        async with self._lock:
            self.count += 1
            if self.count >= self.total:
                self.completed.set()
