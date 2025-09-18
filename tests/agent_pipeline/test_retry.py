from __future__ import annotations

import random

import httpx
import pytest
from trio.testing import trio_test

from agent_pipeline.config import RetryPolicy
from agent_pipeline.retry import RetryState, retry_async


@trio_test
async def test_retry_async_successful_after_transient_errors() -> None:
    policy = RetryPolicy(
        max_attempts=3,
        initial_delay=0.001,
        backoff_multiplier=2.0,
        max_delay=0.002,
        jitter_ratio=0.0,
    )

    attempts: list[int] = []
    delays: list[float] = []

    async def flaky(state: RetryState) -> str:
        attempts.append(state.attempt)
        delays.append(state.delay)
        if state.attempt < 3:
            request = httpx.Request("GET", "https://example.com")
            response = httpx.Response(429, request=request)
            raise httpx.HTTPStatusError("rate limited", request=request, response=response)
        return "ok"

    result = await retry_async(flaky, policy=policy, rng=random.Random(0))

    assert result == "ok"
    assert attempts == [1, 2, 3]
    # second attempt sleeps before invocation
    assert delays[1] == pytest.approx(policy.initial_delay, rel=0, abs=1e-9)


@trio_test
async def test_retry_async_propagates_non_retryable() -> None:
    policy = RetryPolicy(
        max_attempts=2,
        initial_delay=0.001,
        backoff_multiplier=2.0,
        max_delay=0.002,
        jitter_ratio=0.0,
    )

    async def failing(_state: RetryState) -> None:
        request = httpx.Request("GET", "https://example.com")
        response = httpx.Response(400, request=request)
        raise httpx.HTTPStatusError("bad request", request=request, response=response)

    try:
        await retry_async(failing, policy=policy, rng=random.Random(0))
    except httpx.HTTPStatusError as exc:
        assert exc.response.status_code == 400
    else:  # pragma: no cover - defensive
        raise AssertionError("Expected HTTPStatusError to propagate")
