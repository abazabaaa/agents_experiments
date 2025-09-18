"""Retry helpers with exponential backoff and jitter."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import TYPE_CHECKING, Awaitable, Callable, Iterable, Optional, TypeVar

import httpx
import trio

from .config import RetryPolicy

if TYPE_CHECKING:  # pragma: no cover
    from .logging import StructuredLogger

T = TypeVar("T")

# HTTP status codes that commonly indicate a transient failure.
DEFAULT_RETRYABLE_STATUS_CODES: frozenset[int] = frozenset({408, 409, 425, 429, 500, 502, 503, 504})

RETRY_STATUS_MESSAGES: dict[int, str] = {
    408: "Request Timeout",
    409: "Conflict",
    425: "Too Early",
    429: "Too Many Requests",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
}


@dataclass(slots=True)
class RetryState:
    """Metadata describing the current retry attempt."""

    attempt: int
    delay: float


def _compute_delay(attempt: int, policy: RetryPolicy, rng: random.Random) -> float:
    """Compute the backoff delay for ``attempt`` using the provided policy."""

    base_delay = policy.initial_delay * (policy.backoff_multiplier ** (attempt - 1))
    capped_delay = min(base_delay, policy.max_delay)
    jitter = capped_delay * policy.jitter_ratio
    if jitter == 0:
        return capped_delay
    low = max(policy.initial_delay, capped_delay - jitter)
    high = capped_delay + jitter
    return rng.uniform(low, high)


def is_retryable_exception(exc: BaseException, retryable_status_codes: Iterable[int]) -> bool:
    """Return ``True`` if ``exc`` represents a transient error."""

    if isinstance(exc, httpx.TimeoutException):
        return True
    if isinstance(exc, httpx.TransportError):
        return True
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code in retryable_status_codes
    if isinstance(exc, httpx.RequestError):
        return True
    return False


def status_reason(status_code: int) -> str:
    """Return a human-readable reason for ``status_code`` if known."""

    return RETRY_STATUS_MESSAGES.get(status_code, f"HTTP {status_code}")


async def retry_async(
    func: Callable[[RetryState], Awaitable[T]],
    *,
    policy: RetryPolicy,
    retryable_status_codes: Iterable[int] = DEFAULT_RETRYABLE_STATUS_CODES,
    rng: Optional[random.Random] = None,
) -> T:
    """Execute ``func`` with retries using ``policy``.

    ``func`` receives a :class:`RetryState` describing the current attempt. The
    first attempt uses ``attempt=1`` and a delay value of ``0.0``.
    """

    rng = rng or random.Random()
    status_codes = frozenset(retryable_status_codes)
    attempt = 1
    delay = 0.0
    while True:
        state = RetryState(attempt=attempt, delay=delay)
        if delay:
            await trio.sleep(delay)
        try:
            return await func(state)
        except BaseException as exc:
            retryable = is_retryable_exception(exc, status_codes)
            if attempt >= policy.max_attempts or not retryable:
                raise
            delay = _compute_delay(attempt, policy, rng)
            attempt += 1


async def execute_with_retry(
    stage: str,
    doc_id: int,
    logger: "StructuredLogger",
    policy: RetryPolicy,
    func: Callable[[int], Awaitable[T]],
    *,
    rng: Optional[random.Random] = None,
) -> T:
    """Execute ``func`` retrying on transient errors while logging attempts."""

    from .utils import truncate  # local import to avoid cycle

    rng = rng or random.Random()

    async def runner(state: RetryState) -> T:
        try:
            return await func(state.attempt)
        except Exception as exc:  # noqa: BLE001
            error_repr = f"{type(exc).__name__}: {exc}"
            logger.verbose(
                f"AGENT_RETRY stage={stage} doc={doc_id} attempt={state.attempt} error={truncate(error_repr, 300)}"
            )
            raise

    return await retry_async(runner, policy=policy, rng=rng)
