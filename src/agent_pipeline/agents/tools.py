"""Factories for tool registrations used by agents."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any


def build_tools(_config: Mapping[str, Any] | None) -> Sequence[Any]:
    """Return tool instances based on configuration.

    Placeholder implementation until tool configuration is defined.
    """

    return []
