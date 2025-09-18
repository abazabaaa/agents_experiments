"""I/O helpers for the agent pipeline."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path


def write_text_atomic(path: Path, text: str, *, encoding: str = "utf-8") -> None:
    """Write ``text`` to ``path`` atomically.

    The data is written to a temporary file in the destination directory and then
    :func:`os.replace` is used to swap it into place.
    """

    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding=encoding) as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, path)
        dir_flags = getattr(os, "O_DIRECTORY", 0)
        dir_fd = None
        try:
            dir_fd = os.open(path.parent, os.O_RDONLY | dir_flags)
        except OSError:
            dir_fd = None
        if dir_fd is not None:
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
    finally:
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)
