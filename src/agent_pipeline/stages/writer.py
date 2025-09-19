"""Persist processed documents to disk."""

from __future__ import annotations

import json
from pathlib import Path

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
    existing_names: dict[str, int] = {}
    failure_root = output_directory / "failures"
    lock = trio.Lock()
    async with receive:
        async for doc in receive:
            approved = bool(doc.metadata.get("review_approved"))
            safe_slug = (doc.file_slug or "document").strip() or "document"
            if safe_slug in {".", ""}:
                safe_slug = "document"
            ext = (
                doc.extension if doc.extension.startswith(".") else f".{doc.extension}"
            )

            if approved:
                async with lock:
                    filename = f"{safe_slug}{ext}"
                    target_dir = output_directory
                    target = target_dir / filename
                    while target.exists():
                        existing_names[safe_slug] = existing_names.get(safe_slug, 0) + 1
                        filename = f"{safe_slug}-{existing_names[safe_slug]}{ext}"
                        target = target_dir / filename
            else:
                target_dir = failure_root / f"doc-{doc.doc_id}"
                target_dir.mkdir(parents=True, exist_ok=True)
                target = target_dir / f"{safe_slug}{ext}"

            target.parent.mkdir(parents=True, exist_ok=True)
            content = _strip_code_fence(doc.processed_text)
            await trio.to_thread.run_sync(write_text_atomic, target, content)
            if not approved:
                details = {
                    "doc_id": doc.doc_id,
                    "url": doc.url,
                    "metadata": doc.metadata,
                    "final_output": doc.final_output,
                    "trajectory": doc.trajectory,
                }
                details_path = target.parent / "run_details.json"
                details_text = json.dumps(details, indent=2, sort_keys=True)
                await trio.to_thread.run_sync(
                    write_text_atomic, details_path, details_text
                )
            await completion_counter.increment()
            logger.verbose(f"WROTE doc={doc.doc_id} -> {target}")


def _strip_code_fence(text: str) -> str:
    """Remove a single top-level Markdown code fence if present."""

    if not text:
        return text

    stripped = text.strip()
    if not stripped.startswith("```"):
        return text

    fence_header_end = stripped.find("\n")
    if fence_header_end == -1:
        return text
    fence_content = stripped[fence_header_end + 1 :]
    if not fence_content.endswith("```"):
        return text

    inner = fence_content[:-3]
    # Preserve original newline structure without the fencing lines.
    return inner.strip("\n") + ("\n" if text.endswith("\n") else "")
