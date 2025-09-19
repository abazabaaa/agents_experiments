"""Concurrency limiter utilities for agent execution."""

from __future__ import annotations

from collections.abc import AsyncIterator, Mapping
from contextlib import asynccontextmanager

import trio
from trio.lowlevel import current_task


class LimiterPool:
    """Manage global and per-model :class:`trio.CapacityLimiter` instances."""

    def __init__(self, *, overall_capacity: int, model_limits: Mapping[str, int]):
        if overall_capacity < 1:
            raise ValueError("overall_capacity must be >= 1")
        self._overall = trio.CapacityLimiter(overall_capacity)
        self._model_limiters = {
            model: trio.CapacityLimiter(limit) for model, limit in model_limits.items()
        }

    @property
    def overall_capacity(self) -> int:
        """Return the configured global concurrency limit."""

        return self._overall.total_tokens

    def get_model_capacity(self, model: str) -> int | None:
        """Return the concurrency limit for ``model`` if configured."""

        limiter = self._model_limiters.get(model)
        return limiter.total_tokens if limiter else None

    @asynccontextmanager
    async def acquire(self, *, model: str | None = None) -> AsyncIterator[None]:
        """Acquire the global limiter and optionally the model limiter."""

        token = current_task()
        await self._overall.acquire_on_behalf_of(token)
        model_limiter = self._model_limiters.get(model) if model is not None else None
        if model_limiter is not None:
            await model_limiter.acquire_on_behalf_of(token)
        try:
            yield
        finally:
            if model_limiter is not None:
                model_limiter.release_on_behalf_of(token)
            self._overall.release_on_behalf_of(token)
