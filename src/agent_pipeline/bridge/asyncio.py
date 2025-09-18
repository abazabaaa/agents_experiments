"""Helpers for working with trio-asyncio bridges."""

from __future__ import annotations

from typing import Any

import trio_asyncio
from agents import Runner

_run_agent = trio_asyncio.aio_as_trio(Runner.run)
_run_streamed = trio_asyncio.aio_as_trio(Runner.run_streamed)


async def run_agent(*args: Any, **kwargs: Any) -> Any:
    """Trio-friendly wrapper around :meth:`Runner.run`."""

    return await _run_agent(*args, **kwargs)


async def run_agent_streamed(*args: Any, **kwargs: Any) -> Any:
    """Trio-friendly wrapper around :meth:`Runner.run_streamed`."""

    return await _run_streamed(*args, **kwargs)
