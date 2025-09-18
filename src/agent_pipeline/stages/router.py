"""Routing stage: classify documents into markdown vs notebook pipelines."""

from __future__ import annotations

from typing import Awaitable, Callable

import trio

from ..agents.registry import AgentRegistry
from ..agents.runner import call_agent, call_agent_with_retry
from ..agents.runconfig import build_run_config
from ..config import PipelineConfig
from ..constants import LARGE_DOCUMENT_THRESHOLD
from ..limiters import LimiterPool
from ..logging import AgentCallContext, StructuredLogger
from ..retry import RetryPolicy
from ..utils import infer_doc_kind, truncate
from .models import RoutingDecision
from .prompts import build_router_prompt
from .types import CompletionCounter, DocTask, WorkItem

RecordFailureFn = Callable[[int, str, str, Exception], Awaitable[None]]


async def router_supervisor(
    *,
    registry: AgentRegistry,
    config: PipelineConfig,
    logger: StructuredLogger,
    limiter_pool: LimiterPool,
    retry_policy: RetryPolicy,
    receive: trio.MemoryReceiveChannel[DocTask],
    markdown_send: trio.MemorySendChannel[WorkItem],
    notebook_send: trio.MemorySendChannel[WorkItem],
    completion_counter: CompletionCounter,
    record_failure: RecordFailureFn,
) -> None:
    router_agent = registry.get_agent("router", output_type=RoutingDecision)
    router_spec = config.agent_specs["router"]
    router_timeout = router_spec.timeout
    router_max_turns = router_spec.run_max_turns
    router_pool = config.concurrency.router_pool

    async def worker(worker_idx: int) -> None:
        async with receive.clone() as channel:
            async for task in channel:
                doc_size = len(task.content)
                if doc_size > LARGE_DOCUMENT_THRESHOLD:
                    logger.verbose(
                        f"DOC_SIZE_WARNING doc={task.doc_id} bytes={doc_size}"
                    )
                kind = infer_doc_kind(task.url, task.metadata)
                rationale: str | None = None
                if not kind:

                    async def attempt(attempt_index: int) -> RoutingDecision:
                        metadata = dict(task.metadata)
                        metadata.setdefault("stage", "routing")
                        context = AgentCallContext(
                            logger=logger,
                            workflow_name=config.workflow_name,
                            stage="routing",
                            run_id=f"route-{task.doc_id}-{worker_idx}-try{attempt_index}",
                            doc_url=task.url,
                            metadata=metadata,
                            trace_id=None,
                        )
                        run_config = build_run_config(config, context)
                        prompt = build_router_prompt(config, task)
                        result = await call_agent(
                            router_agent,
                            prompt,
                            context=context,
                            run_config=run_config,
                            limiter_pool=limiter_pool,
                            timeout=router_timeout,
                            run_max_turns=router_max_turns,
                        )
                        return result.final_output

                    try:
                        decision = await call_agent_with_retry(
                            "routing",
                            task.doc_id,
                            logger,
                            retry_policy,
                            attempt,
                        )
                    except Exception as exc:  # noqa: BLE001
                        await record_failure(
                            task.doc_id,
                            task.url,
                            "routing",
                            exc,
                        )
                        await completion_counter.increment()
                        continue
                    kind = decision.route
                    rationale = decision.rationale
                logger.verbose(
                    f"ROUTED doc={task.doc_id} url={task.url} kind={kind} rationale={truncate(rationale)}"
                )
                # Carry forward any reviewer feedback present in metadata
                feedback_text: str | None = None
                last_issues = task.metadata.get("last_review_issues")
                last_suggestions = task.metadata.get("last_review_suggestions")
                if isinstance(last_issues, str) and last_issues.strip():
                    feedback_text = last_issues.strip()
                if isinstance(last_suggestions, str) and last_suggestions.strip():
                    feedback_text = (
                        (feedback_text + "\n\nSuggestions:\n" if feedback_text else "Suggestions:\n")
                        + last_suggestions.strip()
                    )
                item = WorkItem(
                    doc_id=task.doc_id,
                    url=task.url,
                    content=task.content,
                    metadata=task.metadata,
                    kind=kind,  # type: ignore[arg-type]
                    review_feedback=feedback_text,
                )
                if kind == "markdown":
                    await markdown_send.send(item)
                else:
                    await notebook_send.send(item)

    async with trio.open_nursery() as nursery:
        for idx in range(router_pool):
            nursery.start_soon(worker, idx)

    await markdown_send.aclose()
    await notebook_send.aclose()
