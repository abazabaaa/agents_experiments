"""Quality review stage."""

from __future__ import annotations

from typing import Awaitable, Callable

import trio

from ..agents.registry import AgentRegistry
from agents.exceptions import ModelBehaviorError
from agents.model_settings import ModelSettings
from ..agents.runner import call_agent, call_agent_with_retry
from ..agents.runconfig import build_run_config
from ..config import PipelineConfig
from ..limiters import LimiterPool
from ..logging import AgentCallContext, StructuredLogger
from ..retry import RetryPolicy
from ..utils import truncate
from .models import ReviewResult, RoutingDecision
from .prompts import build_review_prompt, build_router_prompt
from .types import CompletionCounter, ProcessedDoc, ReviewedDoc, WorkItem, DocTask

RecordFailureFn = Callable[[int, str, str, Exception], Awaitable[None]]


async def review_supervisor(
    *,
    registry: AgentRegistry,
    config: PipelineConfig,
    logger: StructuredLogger,
    limiter_pool: LimiterPool,
    retry_policy: RetryPolicy,
    receive: trio.MemoryReceiveChannel[ProcessedDoc],
    markdown_send: trio.MemorySendChannel[WorkItem],
    notebook_send: trio.MemorySendChannel[WorkItem],
    naming_send: trio.MemorySendChannel[ReviewedDoc],
    finished_event: trio.Event,
    completion_counter: CompletionCounter,
    record_failure: RecordFailureFn,
) -> None:
    agent = registry.get_agent("reviewer", output_type=ReviewResult)
    agent_spec = config.agent_specs["reviewer"]
    agent_timeout = agent_spec.timeout
    agent_max_turns = agent_spec.run_max_turns
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
                    prompt = build_review_prompt(config, doc)
                    try:
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
                    except ModelBehaviorError as err:
                        # Fallback: retry once using config-driven overrides (no hardcoded knobs).
                        overrides = config.agent_specs["reviewer"].attempt_overrides.get(
                            "on_invalid_json"
                        )
                        if overrides is None:
                            raise ValueError(
                                "Config error: reviewer.attempt_overrides.on_invalid_json is not defined. "
                                "Add an 'on_invalid_json' override with a prompt_suffix and/or model_settings, "
                                "or remove the retry behavior if not desired."
                            ) from err
                        # Build prompt with optional suffix from config
                        repair_prompt = prompt
                        suffix = overrides.prompt_suffix
                        if suffix:
                            repair_prompt = prompt + "\n" + suffix
                        # Build optional ModelSettings from config mapping
                        repair_ms_map = overrides.model_settings
                        repair_config = build_run_config(config, context)
                        if repair_ms_map:
                            # Validation of keys occurs at config load; pass through verbatim.
                            repair_config.model_settings = ModelSettings(**dict(repair_ms_map))
                        result = await call_agent(
                            agent,
                            repair_prompt,
                            context=context,
                            run_config=repair_config,
                            limiter_pool=limiter_pool,
                            timeout=agent_timeout,
                            run_max_turns=agent_max_turns,
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
                    # Optional rework loop with guard rails
                    if config.rework_enabled and config.rework_max_cycles > 0:
                        cycles = int(doc.metadata.get("rework_cycles", 0) or 0)
                        if cycles < config.rework_max_cycles:
                            new_meta = dict(doc.metadata)
                            new_meta["rework_cycles"] = cycles + 1
                            new_meta["last_review_issues"] = review.issues or ""
                            new_meta["last_review_suggestions"] = review.suggestions or ""
                            feedback_text = (review.issues or "").strip()
                            if review.suggestions:
                                feedback_text = (
                                    (feedback_text + "\n\nSuggestions:\n") if feedback_text else "Suggestions:\n"
                                ) + review.suggestions.strip()
                            if config.rework_target_on_reject == "router":
                                # Re-classify using the router agent and forward accordingly
                                router_agent = registry.get_agent(
                                    "router", output_type=RoutingDecision
                                )
                                router_spec = config.agent_specs["router"]
                                router_timeout = router_spec.timeout
                                router_max_turns = router_spec.run_max_turns
                                task = DocTask(
                                    doc_id=doc.doc_id,
                                    url=doc.url,
                                    content=doc.processed_text,
                                    metadata=new_meta,
                                )
                                router_context = AgentCallContext(
                                    logger=logger,
                                    workflow_name=config.workflow_name,
                                    stage="routing",
                                    run_id=f"route-rework-{doc.doc_id}-{worker_idx}",
                                    doc_url=doc.url,
                                    metadata=new_meta,
                                    trace_id=None,
                                )
                                router_run_config = build_run_config(config, router_context)
                                router_prompt = build_router_prompt(config, task)
                                decision = await call_agent(
                                    router_agent,
                                    router_prompt,
                                    context=router_context,
                                    run_config=router_run_config,
                                    limiter_pool=limiter_pool,
                                    timeout=router_timeout,
                                    run_max_turns=router_max_turns,
                                )
                                target_kind = decision.final_output.route
                            else:
                                target_kind = (
                                    doc.kind
                                    if config.rework_target_on_reject == "same"
                                    else config.rework_target_on_reject
                                )
                            rework_item = WorkItem(
                                doc_id=doc.doc_id,
                                url=doc.url,
                                content=doc.processed_text,
                                metadata=new_meta,
                                kind=target_kind,  # type: ignore[arg-type]
                                attempts=doc.attempts + 1,
                                review_feedback=feedback_text or None,
                            )
                            if rework_item.kind == "markdown":
                                await markdown_send.send(rework_item)
                            else:
                                await notebook_send.send(rework_item)
                            # Do not increment completion; item re-enters the pipeline
                        else:
                            logger.verbose(
                                f"REVIEW_REJECT_MAX_CYCLES doc={doc.doc_id} max={config.rework_max_cycles}"
                            )
                            await completion_counter.increment()
                    else:
                        await completion_counter.increment()

    async with trio.open_nursery() as nursery:
        for idx in range(pool):
            nursery.start_soon(worker, idx)

    finished_event.set()
