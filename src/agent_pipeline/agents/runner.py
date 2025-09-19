"""Helpers for invoking agents with concurrency and retry controls."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any

import trio
from agents import Agent
from agents.exceptions import MaxTurnsExceeded
from agents.run import RunConfig

from ..bridge.asyncio import run_agent as run_agent_asyncio
from ..bridge.asyncio import run_agent_streamed
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
                try:
                    result = await run_agent_asyncio(
                        agent,
                        ensure_conversation(message),
                        **kwargs,
                    )
                except MaxTurnsExceeded as e:
                    # Log the max turns exceeded for debugging
                    context.logger.warning(
                        f"Agent exceeded max turns: agent={agent.name} stage={context.stage} "
                        f"max_turns={run_max_turns} error={e}"
                    )
                    # Re-raise as TimeoutError to maintain interface consistency
                    raise TimeoutError(
                        f"Agent '{agent.name}' exceeded maximum turns ({run_max_turns}) "
                        f"in stage '{context.stage}'"
                    ) from e
            if cancel_scope.cancelled_caught:
                context.logger.warning(
                    f"Agent timed out: agent={agent.name} stage={context.stage} "
                    f"timeout={deadline}s"
                )
                raise TimeoutError(
                    f"Agent call timed out after {deadline} seconds during stage {context.stage}"
                )
            return result
        except trio.Cancelled:
            # Log trio cancellation for debugging
            context.logger.debug(
                f"Agent cancelled by trio: agent={agent.name} stage={context.stage}"
            )
            raise
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


async def call_agent_streamed(
    agent: Agent[Any],
    message: AgentInput,
    *,
    context: AgentCallContext,
    run_config: RunConfig,
    limiter_pool: LimiterPool,
    timeout: float | None = None,
    run_max_turns: int | None = None,
) -> Any:
    """Call ``agent`` with streaming support for progress monitoring.

    This version uses Runner.run_streamed() to enable real-time progress
    tracking and early termination detection for long-running operations.
    """

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

                try:
                    # Use streaming version for better progress monitoring
                    result = await run_agent_streamed(
                        agent,
                        ensure_conversation(message),
                        **kwargs,
                    )

                    # Track progress and detect stuck patterns
                    turn_count = 0
                    last_progress_time = trio.current_time()
                    progress_timeout = 30.0  # Alert if no progress for 30s

                    async for event in result.stream_events():
                        current_time = trio.current_time()

                        # Check for progress
                        if event.type == "run_item_stream_event":
                            turn_count += 1
                            last_progress_time = current_time
                            context.logger.debug(
                                f"Agent progress: agent={agent.name} turn={turn_count} "
                                f"stage={context.stage}"
                            )

                        # Detect stuck agent
                        if current_time - last_progress_time > progress_timeout:
                            context.logger.warning(
                                f"Agent appears stuck: agent={agent.name} "
                                f"stage={context.stage} no_progress_for={progress_timeout}s"
                            )

                    # Return the final result
                    return await result.final_result()

                except MaxTurnsExceeded as e:
                    context.logger.warning(
                        f"Streaming agent exceeded max turns: agent={agent.name} "
                        f"stage={context.stage} max_turns={run_max_turns}"
                    )
                    raise TimeoutError(
                        f"Agent '{agent.name}' exceeded maximum turns in stage '{context.stage}'"
                    ) from e

            if cancel_scope.cancelled_caught:
                context.logger.warning(
                    f"Streaming agent timed out: agent={agent.name} "
                    f"stage={context.stage} timeout={deadline}s"
                )
                raise TimeoutError(
                    f"Streaming agent call timed out after {deadline} seconds"
                )

        except trio.Cancelled:
            context.logger.debug(
                f"Streaming agent cancelled: agent={agent.name} stage={context.stage}"
            )
            raise
        finally:
            TRACE_ID_VAR.reset(token)
