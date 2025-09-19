"""Customized AsyncOpenAI client with richer HTTP diagnostics."""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from typing import Any

import httpx
from openai import AsyncOpenAI

from .config import HTTPTimeoutConfig

_HTTP_LOGGER = logging.getLogger("openai.agents.http")


class InstrumentedAsyncClient(httpx.AsyncClient):
    """AsyncClient that logs structured details for each request."""

    def __init__(self, *, log_successes: bool = False, **kwargs: Any) -> None:
        self._log_successes = log_successes
        super().__init__(**kwargs)

    async def send(self, request: httpx.Request, **kwargs: Any) -> httpx.Response:
        start = time.perf_counter()
        try:
            response = await super().send(request, **kwargs)
        except Exception as exc:  # pragma: no cover - exercised in integration
            elapsed = time.perf_counter() - start
            _HTTP_LOGGER.error(
                "HTTP %s %s failed after %.2fs: %s",
                request.method,
                request.url,
                elapsed,
                exc,
            )
            raise

        elapsed = time.perf_counter() - start
        log_this = self._log_successes or response.status_code >= 400
        if log_this:
            level = logging.DEBUG
            if response.status_code >= 500:
                level = logging.ERROR
            elif response.status_code >= 400:
                level = logging.WARNING

            _HTTP_LOGGER.log(
                level,
                "HTTP %s %s -> %s in %.2fs request_id=%s",
                request.method,
                response.request.url,
                response.status_code,
                elapsed,
                response.headers.get("x-request-id"),
            )
        return response


@dataclass(slots=True)
class ClientTuning:
    """Tuning parameters for the AsyncOpenAI client."""

    max_retries: int = 5
    log_successes: bool = False
    max_connections: int = 40
    max_keepalive_connections: int = 20


def build_async_openai_client(
    *,
    api_key: str,
    timeout_cfg: HTTPTimeoutConfig,
    tuning: ClientTuning | None = None,
) -> AsyncOpenAI:
    """Construct an AsyncOpenAI client with custom HTTPX logging and retries."""

    tuning = tuning or ClientTuning()

    timeout = httpx.Timeout(
        connect=timeout_cfg.connect if timeout_cfg.connect is not None else 10.0,
        read=timeout_cfg.read if timeout_cfg.read is not None else 180.0,
        write=timeout_cfg.write if timeout_cfg.write is not None else 60.0,
        pool=timeout_cfg.pool if timeout_cfg.pool is not None else 10.0,
    )

    http_client = InstrumentedAsyncClient(
        log_successes=tuning.log_successes,
        timeout=timeout,
        limits=httpx.Limits(
            max_connections=tuning.max_connections,
            max_keepalive_connections=tuning.max_keepalive_connections,
        ),
    )

    _HTTP_LOGGER.debug(
        "Configured HTTP client timeout(connect=%.1fs read=%s write=%s pool=%.1fs)"
        " max_retries=%s",
        timeout.connect,
        "infinite" if timeout.read is None else f"{timeout.read:.1f}s",
        "infinite" if timeout.write is None else f"{timeout.write:.1f}s",
        timeout.pool,
        tuning.max_retries,
    )

    return AsyncOpenAI(
        api_key=api_key,
        http_client=http_client,
        max_retries=tuning.max_retries,
    )

