"""File naming stage."""

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
from ..utils import normalize_slug, safe_extension
from .models import NamingResult
from .prompts import build_naming_prompt
from .types import CompletionCounter, NamedDoc, ReviewedDoc

RecordFailureFn = Callable[[int, str, str, Exception], Awaitable[None]]


async def naming_supervisor(
    *,
    registry: AgentRegistry,
    config: PipelineConfig,
    logger: StructuredLogger,
    limiter_pool: LimiterPool,
    retry_policy: RetryPolicy,
    receive: trio.MemoryReceiveChannel[ReviewedDoc],
    write_send: trio.MemorySendChannel[NamedDoc],
    finished_event: trio.Event,
    completion_counter: CompletionCounter,
    record_failure: RecordFailureFn,
) -> None:
    agent = registry.get_agent("namer", output_type=NamingResult)
    agent_spec = config.agent_specs["namer"]
    agent_timeout = agent_spec.timeout
    agent_max_turns = agent_spec.run_max_turns
    pool = max(1, config.concurrency.naming_pool)

    async def worker(worker_idx: int) -> None:
        async with receive.clone() as channel:
            async for doc in channel:

                async def attempt(attempt_index: int) -> NamingResult:
                    metadata = dict(doc.metadata)
                    metadata.setdefault("stage", "naming")
                    context = AgentCallContext(
                        logger=logger,
                        workflow_name=config.workflow_name,
                        stage="naming",
                        run_id=f"name-{doc.doc_id}-{worker_idx}-try{attempt_index}",
                        doc_url=doc.url,
                        metadata=metadata,
                        trace_id=None,
                    )
                    run_config = build_run_config(config, context)
                    prompt = build_naming_prompt(config, doc)
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
                    naming = await call_agent_with_retry(
                        "naming",
                        doc.doc_id,
                        logger,
                        retry_policy,
                        attempt,
                    )
                except Exception as exc:  # noqa: BLE001
                    await record_failure(
                        doc.doc_id,
                        doc.url,
                        "naming",
                        exc,
                    )
                    await completion_counter.increment()
                    continue

                named = NamedDoc(
                    doc_id=doc.doc_id,
                    url=doc.url,
                    file_slug=normalize_slug(naming.file_slug),
                    extension=safe_extension(naming.extension, doc.kind),
                    processed_text=doc.processed_text,
                    metadata=doc.metadata,
                )
                await write_send.send(named)

    async with trio.open_nursery() as nursery:
        for idx in range(pool):
            nursery.start_soon(worker, idx)

    finished_event.set()
