"""Persist processed documents to disk."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import trio

from ..io import write_text_atomic
from ..logging import StructuredLogger
from .types import CompletionCounter, NamedDoc


async def writer_stage(
    *,
    receive: trio.MemoryReceiveChannel[NamedDoc],
    output_directory: Path,
    logger: StructuredLogger,
    completion_counter: CompletionCounter,
) -> None:
    existing_names: Dict[str, int] = {}
    lock = trio.Lock()
    async with receive:
        async for doc in receive:
            async with lock:
                base = doc.file_slug or "document"
                ext = doc.extension if doc.extension.startswith(".") else f".{doc.extension}"
                filename = f"{base}{ext}"
                target = output_directory / filename
                while target.exists():
                    existing_names[base] = existing_names.get(base, 0) + 1
                    filename = f"{base}-{existing_names[base]}{ext}"
                    target = output_directory / filename
            await trio.to_thread.run_sync(write_text_atomic, target, doc.processed_text)
            await completion_counter.increment()
            logger.verbose(f"WROTE doc={doc.doc_id} -> {target}")
