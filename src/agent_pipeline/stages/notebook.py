"""Notebook refactoring stage."""

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
from .models import NotebookRefactorResult
from .prompts import build_notebook_prompt
from .types import CompletionCounter, ProcessedDoc, WorkItem

RecordFailureFn = Callable[[int, str, str, Exception], Awaitable[None]]


async def notebook_supervisor(
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
    record_failure: RecordFailureFn,
) -> None:
    agent = registry.get_agent("notebook_refactor", output_type=NotebookRefactorResult)
    agent_timeout = config.agent_specs["notebook_refactor"].timeout
    pool = config.concurrency.notebook_pool

    async def worker(worker_idx: int) -> None:
        async with receive.clone() as channel:
            async for item in channel:

                async def attempt(attempt_index: int) -> NotebookRefactorResult:
                    metadata = dict(item.metadata)
                    metadata.setdefault("stage", "notebook-refactor")
                    context = AgentCallContext(
                        logger=logger,
                        workflow_name=config.workflow_name,
                        stage="notebook",
                        run_id=f"nb-{item.doc_id}-{worker_idx}-try{attempt_index}",
                        doc_url=item.url,
                        metadata=metadata,
                        trace_id=None,
                    )
                    run_config = build_run_config(config, context)
                    prompt = build_notebook_prompt(item)
                    result = await call_agent(
                        agent,
                        prompt,
                        context=context,
                        run_config=run_config,
                        limiter_pool=limiter_pool,
                        timeout=agent_timeout,
                    )
                    return result.final_output

                try:
                    result = await call_agent_with_retry(
                        "notebook",
                        item.doc_id,
                        logger,
                        retry_policy,
                        attempt,
                    )
                except Exception as exc:  # noqa: BLE001
                    await record_failure(
                        item.doc_id,
                        item.url,
                        "notebook",
                        exc,
                    )
                    await completion_counter.increment()
                    continue

                processed = ProcessedDoc(
                    doc_id=item.doc_id,
                    url=item.url,
                    kind="notebook",
                    processed_text=result.python_script,
                    metadata=item.metadata,
                    attempts=item.attempts,
                    summary=result.summary,
                )
                await review_send.send(processed)

    async with trio.open_nursery() as nursery:
        for idx in range(pool):
            nursery.start_soon(worker, idx)

    finished_event.set()
