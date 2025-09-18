"""Document ingestion stage."""

from __future__ import annotations

from typing import Iterable, Sequence

import trio

from .types import DocTask


async def ingest_documents(
    docs: Sequence[DocTask], send_channel: trio.MemorySendChannel[DocTask]
) -> None:
    """Send all documents into the router channel."""

    async with send_channel:
        for doc in docs:
            await send_channel.send(doc)


def load_documents(payload: dict[str, object]) -> list[DocTask]:
    """Construct :class:`DocTask` objects from serialized payload."""

    docs: list[DocTask] = []
    buckets: Iterable[str] = ("scraped_documents", "follow_up_documents")
    for bucket in buckets:
        entries = payload.get(bucket) or []
        if not isinstance(entries, list):
            continue
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            url = entry.get("url") or entry.get("source_url") or entry.get("link")
            if not url:
                continue
            content = entry.get("markdown") or entry.get("content") or ""
            if not content:
                continue
            metadata = entry.get("metadata") or entry.get("meta") or {}
            if not isinstance(metadata, dict):
                metadata = {}
            doc = DocTask(
                doc_id=len(docs) + 1,
                url=str(url),
                content=str(content),
                metadata=dict(metadata),
            )
            docs.append(doc)
    return docs
