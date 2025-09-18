"""Helpers for invoking agents with concurrency and retry controls."""

from __future__ import annotations

from typing import Any, Awaitable, Callable, Optional

import trio

from agents import Agent
from agents.run import RunConfig

from ..config import RetryPolicy
from ..constants import DEFAULT_AGENT_TIMEOUT
from ..logging import (
    AgentCallContext,
    LifecycleLoggingHooks,
    StructuredLogger,
    TRACE_ID_VAR,
)
from ..limiters import LimiterPool
from ..retry import execute_with_retry
from ..bridge.asyncio import run_agent as run_agent_asyncio


async def call_agent(
    agent: Agent[Any],
    message: str,
    *,
    context: AgentCallContext,
    run_config: RunConfig,
    limiter_pool: LimiterPool,
    timeout: Optional[float] = None,
    run_max_turns: Optional[int] = None,
) -> Any:
    """Call ``agent`` with concurrency limiting and logging."""

    hooks = LifecycleLoggingHooks(context)
    deadline = timeout if timeout is not None else DEFAULT_AGENT_TIMEOUT
    model_name = getattr(agent, "model", None)
    model_key = model_name if isinstance(model_name, str) else None
    async with limiter_pool.acquire(model=model_key):
        token = TRACE_ID_VAR.set(context.trace_id or context.run_id)
        try:
            with trio.move_on_after(deadline) as cancel_scope:
                kwargs: dict[str, Any] = {
                    "context": context,
                    "hooks": hooks,
                    "run_config": run_config,
                }
                if run_max_turns is not None:
                    kwargs["max_turns"] = run_max_turns
                result = await run_agent_asyncio(
                    agent,
                    message,
                    **kwargs,
                )
            if cancel_scope.cancelled_caught:
                raise TimeoutError(
                    f"Agent call timed out after {deadline} seconds during stage {context.stage}"
                )
            return result
        finally:
            TRACE_ID_VAR.reset(token)


async def call_agent_with_retry(
    stage: str,
    doc_id: int,
    logger: StructuredLogger,
    retry_policy: RetryPolicy,
    func: Callable[[int], Awaitable[Any]],
) -> Any:
    """Retry ``func`` according to ``retry_policy`` while logging attempts."""

    return await execute_with_retry(stage, doc_id, logger, retry_policy, func)
