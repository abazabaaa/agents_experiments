"""Quality review stage."""

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
from ..utils import truncate
from .models import ReviewResult
from .prompts import build_review_prompt
from .types import CompletionCounter, ProcessedDoc, ReviewedDoc

RecordFailureFn = Callable[[int, str, str, Exception], Awaitable[None]]


async def review_supervisor(
    *,
    registry: AgentRegistry,
    config: PipelineConfig,
    logger: StructuredLogger,
    limiter_pool: LimiterPool,
    retry_policy: RetryPolicy,
    receive: trio.MemoryReceiveChannel[ProcessedDoc],
    naming_send: trio.MemorySendChannel[ReviewedDoc],
    finished_event: trio.Event,
    completion_counter: CompletionCounter,
    record_failure: RecordFailureFn,
) -> None:
    agent = registry.get_agent("reviewer", output_type=ReviewResult)
    agent_timeout = config.agent_specs["reviewer"].timeout
    pool = max(1, config.concurrency.review_pool)

    async def worker(worker_idx: int) -> None:
        async with receive.clone() as channel:
            async for doc in channel:

                async def attempt(attempt_index: int) -> ReviewResult:
                    metadata = dict(doc.metadata)
                    metadata.setdefault("stage", "review")
                    context = AgentCallContext(
                        logger=logger,
                        workflow_name=config.workflow_name,
                        stage="review",
                        run_id=f"review-{doc.doc_id}-{worker_idx}-try{attempt_index}",
                        doc_url=doc.url,
                        metadata=metadata,
                        trace_id=None,
                    )
                    run_config = build_run_config(config, context)
                    prompt = build_review_prompt(doc)
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
                    review = await call_agent_with_retry(
                        "review",
                        doc.doc_id,
                        logger,
                        retry_policy,
                        attempt,
                    )
                except Exception as exc:  # noqa: BLE001
                    await record_failure(
                        doc.doc_id,
                        doc.url,
                        "review",
                        exc,
                    )
                    await completion_counter.increment()
                    continue

                if review.approved:
                    reviewed = ReviewedDoc(
                        doc_id=doc.doc_id,
                        url=doc.url,
                        kind=doc.kind,
                        processed_text=doc.processed_text,
                        metadata=doc.metadata,
                        title_hint=review.suggestions or review.issues,
                    )
                    await naming_send.send(reviewed)
                else:
                    logger.verbose(
                        f"REVIEW_REJECT doc={doc.doc_id} issues={truncate(review.issues)}"
                    )
                    await completion_counter.increment()

    async with trio.open_nursery() as nursery:
        for idx in range(pool):
            nursery.start_soon(worker, idx)

    finished_event.set()
