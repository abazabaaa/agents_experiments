"""Prompt loading utilities."""

from __future__ import annotations

from pathlib import Path


def load_markdown(path: Path, *, description: str) -> str:
    """Load markdown content and fail fast if the file is missing or empty."""

    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"{description} file not found: {path}")
    raw = path.read_text(encoding="utf-8")
    if not raw.strip():
        raise ValueError(f"{description} file is empty: {path}")
    return raw
