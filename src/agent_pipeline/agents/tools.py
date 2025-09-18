"""Factories for tool registrations used by agents."""

from __future__ import annotations

from typing import Any, Iterable, Mapping, Sequence


def build_tools(_config: Mapping[str, Any] | None) -> Sequence[Any]:
    """Return tool instances based on configuration.

    Placeholder implementation until tool configuration is defined.
    """

    return []
