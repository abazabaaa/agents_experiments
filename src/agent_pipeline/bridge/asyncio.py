"""Helpers for working with trio-asyncio bridges."""

from __future__ import annotations

import logging
from typing import Any

import trio
import trio_asyncio
from agents import Runner

logger = logging.getLogger(__name__)


async def run_agent(*args: Any, **kwargs: Any) -> Any:
    """Trio-friendly wrapper around Runner.run with proper loop context.

    This ensures that asyncio tasks created by the OpenAI SDK are properly
    managed within an explicit event loop context, improving cancellation
    behavior and preventing hanging tasks.
    """
    # Use explicit loop context for better cancellation semantics
    async with trio_asyncio.open_loop() as loop:
        # Log loop creation for debugging
        logger.debug(f"Created asyncio loop {id(loop)} for agent run")

        try:
            # Wrap the Runner.run method for trio compatibility
            aio_run = trio_asyncio.aio_as_trio(Runner.run)
            result = await aio_run(*args, **kwargs)
            logger.debug(f"Agent run completed successfully on loop {id(loop)}")
            return result
        except trio.Cancelled:
            # Trio cancellation - ensure asyncio tasks are cleaned up
            logger.debug(f"Trio cancellation detected, cleaning up loop {id(loop)}")
            # Re-raise to maintain trio cancellation semantics
            raise
        except Exception as e:
            logger.error(f"Agent run failed on loop {id(loop)}: {e}")
            raise


async def run_agent_streamed(*args: Any, **kwargs: Any) -> Any:
    """Trio-friendly wrapper around Runner.run_streamed with proper loop context.

    This enables streaming responses for better progress monitoring and
    early termination of long-running operations.
    """
    # Use explicit loop context for streaming operations
    async with trio_asyncio.open_loop() as loop:
        logger.debug(f"Created asyncio loop {id(loop)} for streamed agent run")

        try:
            # Wrap the Runner.run_streamed method for trio compatibility
            aio_run_streamed = trio_asyncio.aio_as_trio(Runner.run_streamed)
            result = await aio_run_streamed(*args, **kwargs)
            logger.debug(f"Streamed agent run completed on loop {id(loop)}")
            return result
        except trio.Cancelled:
            logger.debug(
                f"Trio cancellation detected in streaming, cleaning up loop {id(loop)}"
            )
            raise
        except Exception as e:
            logger.error(f"Streamed agent run failed on loop {id(loop)}: {e}")
            raise
