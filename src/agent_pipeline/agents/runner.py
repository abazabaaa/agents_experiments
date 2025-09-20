"""Helpers for invoking agents with concurrency and retry controls."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any

import trio
from agents import Agent, Session
from agents.run import RunConfig

from ..bridge.asyncio import run_agent as run_agent_asyncio
from ..config import RetryPolicy
from ..constants import DEFAULT_AGENT_TIMEOUT
from ..conversation import AgentInput, ensure_conversation
from ..limiters import LimiterPool
from ..logging import (
    TRACE_ID_VAR,
    AgentCallContext,
    LifecycleLoggingHooks,
    StructuredLogger,
)
from ..retry import execute_with_retry


async def call_agent(
    agent: Agent[Any],
    message: AgentInput,
    *,
    context: AgentCallContext,
    run_config: RunConfig,
    limiter_pool: LimiterPool,
    timeout: float | None = None,
    run_max_turns: int | None = None,
    session: Session | None = None,
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
                    "session": session,
                }
                if run_max_turns is not None:
                    kwargs["max_turns"] = run_max_turns
                result = await run_agent_asyncio(
                    agent,
                    ensure_conversation(message),
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
