"""Markdown cleaning stage."""

from __future__ import annotations

from typing import Awaitable, Callable

import trio

from ..agents.registry import AgentRegistry
from ..agents.runner import call_agent, call_agent_with_retry
from ..agents.runconfig import build_run_config
from ..config import PipelineConfig
from ..limiters import LimiterPool
from ..logging import AgentCallContext, StructuredLogger
from ..retry import RetryPolicy
from .models import MarkdownCleanResult
from .prompts import build_markdown_prompt
from .types import CompletionCounter, ProcessedDoc, WorkItem


async def markdown_supervisor(
    *,
    registry: AgentRegistry,
    config: PipelineConfig,
    logger: StructuredLogger,
    limiter_pool: LimiterPool,
    retry_policy: RetryPolicy,
    receive: trio.MemoryReceiveChannel[WorkItem],
    review_send: trio.MemorySendChannel[ProcessedDoc],
    finished_event: trio.Event,
    completion_counter: CompletionCounter,
    record_failure: Callable[[int, str, str, Exception], Awaitable[None]],
) -> None:
    agent = registry.get_agent("markdown_cleaner", output_type=MarkdownCleanResult)
    agent_spec = config.agent_specs["markdown_cleaner"]
    agent_timeout = agent_spec.timeout
    agent_max_turns = agent_spec.run_max_turns
    pool = config.concurrency.markdown_pool

    async def worker(worker_idx: int) -> None:
        async with receive.clone() as channel:
            async for item in channel:

                async def attempt(attempt_index: int) -> MarkdownCleanResult:
                    metadata = dict(item.metadata)
                    metadata.setdefault("stage", "markdown-clean")
                    context = AgentCallContext(
                        logger=logger,
                        workflow_name=config.workflow_name,
                        stage="markdown",
                        run_id=f"md-{item.doc_id}-{worker_idx}-try{attempt_index}",
                        doc_url=item.url,
                        metadata=metadata,
                        trace_id=None,
                    )
                    run_config = build_run_config(config, context)
                    prompt = build_markdown_prompt(config, item)
                    result = await call_agent(
                        agent,
                        prompt,
                        context=context,
                        run_config=run_config,
                        limiter_pool=limiter_pool,
                        timeout=agent_timeout,
                        run_max_turns=agent_max_turns,
                    )
                    return result.final_output

                try:
                    result = await call_agent_with_retry(
                        "markdown",
                        item.doc_id,
                        logger,
                        retry_policy,
                        attempt,
                    )
                except Exception as exc:  # noqa: BLE001
                    await record_failure(
                        item.doc_id,
                        item.url,
                        "markdown",
                        exc,
                    )
                    await completion_counter.increment()
                    continue

                processed = ProcessedDoc(
                    doc_id=item.doc_id,
                    url=item.url,
                    kind="markdown",
                    processed_text=result.cleaned_markdown,
                    metadata=item.metadata,
                    attempts=item.attempts,
                    summary=result.summary,
                )
                await review_send.send(processed)

    async with trio.open_nursery() as nursery:
        for idx in range(pool):
            nursery.start_soon(worker, idx)

    finished_event.set()
