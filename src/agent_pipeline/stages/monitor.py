"""Monitoring and shutdown helpers for the pipeline."""

from __future__ import annotations

from typing import Any, Iterable

import trio

from ..constants import (
    CHANNEL_MONITOR_INTERVAL,
    CHANNEL_PRESSURE_FRACTION,
    SHUTDOWN_TIMEOUT,
)
from ..logging import StructuredLogger
from .types import CompletionCounter


async def monitor_channels(
    *,
    logger: StructuredLogger,
    channels: dict[str, Any],
    counter: CompletionCounter,
    interval: float = CHANNEL_MONITOR_INTERVAL,
) -> None:
    try:
        while True:
            with trio.move_on_after(interval) as scope:
                await counter.completed.wait()
            if not scope.cancelled_caught:
                break
            for name, channel in channels.items():
                stats_fn = getattr(channel, "statistics", None)
                if stats_fn is None:
                    continue
                try:
                    stats = stats_fn()
                except (trio.ClosedResourceError, RuntimeError):
                    continue
                max_size = getattr(stats, "max_buffer_size", None)
                current = getattr(stats, "current_buffer_used", None)
                waiting_senders = getattr(stats, "tasks_waiting_send", None)
                waiting_receivers = getattr(stats, "tasks_waiting_receive", None)
                if (
                    isinstance(max_size, int)
                    and max_size > 0
                    and isinstance(current, int)
                    and current >= int(max_size * CHANNEL_PRESSURE_FRACTION)
                ):
                    logger.verbose(
                        f"CHANNEL_PRESSURE name={name} load={current}/{max_size}"
                    )
                if isinstance(waiting_senders, int) and waiting_senders > 0:
                    logger.verbose(
                        f"CHANNEL_BACKPRESSURE name={name} waiting_senders={waiting_senders}"
                    )
                if isinstance(waiting_receivers, int) and waiting_receivers > 0:
                    logger.verbose(
                        f"CHANNEL_STARVATION name={name} waiting_receivers={waiting_receivers}"
                    )
    finally:
        logger.verbose("Channel monitor exiting")


async def watch_completion(
    *,
    logger: StructuredLogger,
    counter: CompletionCounter,
    nursery: trio.Nursery,
    done_events: Iterable[trio.Event],
) -> None:
    await counter.completed.wait()
    logger.verbose("All documents processed, initiating graceful shutdown")
    with trio.move_on_after(SHUTDOWN_TIMEOUT) as scope:
        for event in done_events:
            await event.wait()
        return
    if scope.cancelled_caught:
        logger.verbose("Timeout during graceful shutdown, forcing cancellation")
        nursery.cancel_scope.cancel()


async def close_when_done(
    done_event: trio.Event, send_channel: trio.MemorySendChannel[Any]
) -> None:
    await done_event.wait()
    await send_channel.aclose()


async def close_when_both_done(
    event_one: trio.Event,
    event_two: trio.Event,
    send_channel: trio.MemorySendChannel[Any],
) -> None:
    await event_one.wait()
    await event_two.wait()
    await send_channel.aclose()
