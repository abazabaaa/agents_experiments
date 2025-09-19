"""Shared data structures used by pipeline stages."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import trio


@dataclass(slots=True)
class DocTask:
    doc_id: int
    url: str
    content: str
    metadata: dict[str, Any]


@dataclass(slots=True)
class NamedDoc:
    doc_id: int
    url: str
    file_slug: str
    extension: str
    processed_text: str
    metadata: dict[str, Any]
    trajectory: list[Any] | None = None
    final_output: dict[str, Any] | None = None


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
