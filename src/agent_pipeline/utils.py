"""Miscellaneous helper functions for the agent pipeline."""

from __future__ import annotations

import re
import unicodedata
from typing import Any


def truncate(value: str | None, limit: int = 160) -> str:
    """Collapse whitespace and truncate ``value`` to ``limit`` characters."""

    if not value:
        return ""
    collapsed = " ".join(value.split())
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[:limit] + "..."


def normalize_slug(text: str) -> str:
    """Return a filesystem-friendly slug derived from ``text``."""

    text_norm = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text_norm = re.sub(r"[^A-Za-z0-9\-]+", "-", text_norm.lower())
    text_norm = text_norm.strip("-")
    return text_norm or "document"


def infer_doc_kind(url: str, metadata: dict[str, Any]) -> str | None:
    """Best-effort guess of document type based on URL and metadata."""

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


def safe_extension(ext: str, kind: str) -> str:
    """Ensure file extension aligns with the processed document kind."""

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
