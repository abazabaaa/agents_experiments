"""Single-document workflow execution built on Agents SDK."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

from agents.result import RunResult

from ..agents.registry import AgentRegistry
from ..agents.runconfig import build_run_config
from ..agents.runner import call_agent, call_agent_with_retry
from ..config import PipelineConfig
from ..conversation import AgentInput, ConversationBuilder, developer_message
from ..limiters import LimiterPool
from ..logging import AgentCallContext, StructuredLogger
from ..retry import RetryPolicy
from ..stages.models import (
    MarkdownCleanResult,
    NamingResult,
    NotebookRefactorResult,
    ReviewResult,
    RoutingDecision,
)
from ..stages.types import DocTask


@dataclass
class WorkflowArtifacts:
    """Collected artifacts from a single document workflow."""

    route: Literal["markdown", "notebook"]
    processed_text: str
    summary: str | None
    review: ReviewResult
    naming: NamingResult
    rework_cycles: int


class WorkflowError(RuntimeError):
    """Raised when a workflow cannot complete successfully."""


class WorkflowRunner:
    """Execute the end-to-end document workflow for individual docs."""

    def __init__(
        self,
        *,
        config: PipelineConfig,
        registry: AgentRegistry,
        limiter_pool: LimiterPool,
        logger: StructuredLogger,
    ) -> None:
        self._config = config
        self._registry = registry
        self._limiter_pool = limiter_pool
        self._logger = logger
        self._retry_policy: RetryPolicy = config.retry_policy

    async def process_document(
        self,
        doc: DocTask,
    ) -> WorkflowArtifacts:
        """Run the multi-stage workflow for ``doc`` and return collected artifacts."""

        base_metadata = dict(doc.metadata)
        base_metadata.setdefault("doc_url", doc.url)

        conversation = self._initial_conversation(doc)

        router_result = await self._run_stage(
            agent_key="router",
            stage="routing",
            doc=doc,
            input_items=conversation,
            metadata=base_metadata,
            output_type=RoutingDecision,
        )
        conversation = router_result.run_result.to_input_list()
        route = router_result.output.route

        processed_text: str | None = None
        summary: str | None = None
        review_result: ReviewResult | None = None
        rework_cycles = 0

        while True:
            stage_key = (
                "markdown_cleaner" if route == "markdown" else "notebook_refactor"
            )
            stage_label = "markdown" if route == "markdown" else "notebook"

            work_result = await self._run_stage(
                agent_key=stage_key,
                stage=stage_label,
                doc=doc,
                input_items=conversation,
                metadata=base_metadata,
                output_type=(
                    MarkdownCleanResult
                    if route == "markdown"
                    else NotebookRefactorResult
                ),
            )
            conversation = work_result.run_result.to_input_list()
            if route == "markdown":
                processed_text = work_result.output.cleaned_markdown
                summary = work_result.output.summary
            else:
                processed_text = work_result.output.python_script
                summary = work_result.output.summary

            review = await self._run_stage(
                agent_key="reviewer",
                stage="review",
                doc=doc,
                input_items=conversation,
                metadata=base_metadata,
                output_type=ReviewResult,
            )
            conversation = review.run_result.to_input_list()
            review_result = review.output
            if review_result.approved:
                break

            if not self._config.rework_enabled or (
                rework_cycles >= self._config.rework_max_cycles
            ):
                raise WorkflowError(
                    "Review rejected document and rework is disabled or exceeded maximum cycles"
                )

            rework_cycles += 1
            feedback_message = self._compose_feedback_message(review_result)
            if feedback_message:
                conversation.append(developer_message(feedback_message))

            target = self._config.rework_target_on_reject
            if target == "router":
                router_retry = await self._run_stage(
                    agent_key="router",
                    stage="routing",
                    doc=doc,
                    input_items=conversation,
                    metadata=base_metadata,
                    output_type=RoutingDecision,
                )
                conversation = router_retry.run_result.to_input_list()
                route = router_retry.output.route
            elif target in {"markdown", "notebook"}:
                route = target
            # otherwise "same": keep previous route

        if processed_text is None or review_result is None:
            raise WorkflowError(
                "Workflow completed without producing processed content"
            )

        naming = await self._run_stage(
            agent_key="namer",
            stage="naming",
            doc=doc,
            input_items=conversation,
            metadata=base_metadata,
            output_type=NamingResult,
        )

        naming_output = naming.output
        extension = naming_output.extension
        if not extension.startswith("."):
            extension = f".{extension}"
            naming_output = NamingResult(
                file_slug=naming_output.file_slug,
                extension=extension,
                title=naming_output.title,
            )

        return WorkflowArtifacts(
            route=route,
            processed_text=processed_text,
            summary=summary,
            review=review_result,
            naming=naming_output,
            rework_cycles=rework_cycles,
        )

    def _initial_conversation(self, doc: DocTask) -> list[dict[str, Any]]:
        builder = ConversationBuilder()
        builder.add_developer(
            "You will assist with preparing documentation for publication."
        )
        builder.add_user(
            f"Document URL: {doc.url}\n"
            f"Metadata: {doc.metadata}\n\n"
            "--- Raw Document ---\n"
            f"{doc.content}\n"
            "--- End Document ---"
        )
        return builder.build()

    async def _run_stage(
        self,
        *,
        agent_key: str,
        stage: str,
        doc: DocTask,
        input_items: AgentInput,
        metadata: dict[str, Any],
        output_type: Any,
    ) -> StageRunResult:
        stage_spec = self._config.agent_specs[agent_key]
        agent = self._registry.get_agent(agent_key, output_type=output_type)

        async def attempt(attempt_index: int) -> RunResult[Any]:
            attempt_metadata = dict(metadata)
            attempt_metadata["stage"] = stage
            attempt_metadata["attempt"] = attempt_index
            context = AgentCallContext(
                logger=self._logger,
                workflow_name=self._config.workflow_name,
                stage=stage,
                run_id=f"{agent_key}-{doc.doc_id}-try{attempt_index}",
                doc_url=doc.url,
                metadata=attempt_metadata,
                trace_id=None,
            )
            run_config = build_run_config(self._config, context)
            run_result: RunResult[Any] = await call_agent(
                agent,
                input_items,
                context=context,
                run_config=run_config,
                limiter_pool=self._limiter_pool,
                timeout=stage_spec.timeout,
                run_max_turns=stage_spec.run_max_turns,
            )
            return run_result

        run_result: RunResult[Any] = await call_agent_with_retry(
            stage,
            doc.doc_id,
            self._logger,
            self._retry_policy,
            attempt,
        )
        return StageRunResult(
            run_result=run_result,
            output=run_result.final_output,
        )

    @staticmethod
    def _compose_feedback_message(review: ReviewResult) -> str | None:
        parts: list[str] = []
        if review.issues:
            parts.append(f"Issues: {review.issues.strip()}")
        if review.suggestions:
            parts.append(f"Suggestions: {review.suggestions.strip()}")
        if not parts:
            return None
        return "Please address the reviewer feedback. " + " \n".join(parts)


@dataclass
class StageRunResult:
    run_result: RunResult[Any]
    output: Any
