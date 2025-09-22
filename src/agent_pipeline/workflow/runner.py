"""Single-document workflow execution built on Agents SDK."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal
from uuid import uuid4

import trio_asyncio
from agents import ItemHelpers, trace
from agents.items import (
    MessageOutputItem,
    ReasoningItem,
    ToolCallItem,
    ToolCallOutputItem,
)
from agents.memory import SQLiteSession
from agents.result import RunResult
from pydantic import BaseModel

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
    WorkflowNamingResult,
    WorkflowOutput,
    WorkflowReviewResult,
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
    trajectory: list[dict[str, Any]]
    final_output: dict[str, Any]


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
        workflow_name = self._config.workflow_name or "document-workflow"
        trace_id = f"trace_{uuid4().hex}"
        group_id = f"doc-{doc.doc_id}"
        trace_metadata = {"doc_url": doc.url}

        with trace(
            workflow_name,
            trace_id=trace_id,
            group_id=group_id,
            metadata=trace_metadata,
        ):
            if "orchestrator" in self._config.agent_specs:
                return await self._run_with_orchestrator(doc, trace_id=trace_id)
            return await self._run_manual(doc, trace_id=trace_id)

    async def _run_with_orchestrator(self, doc: DocTask, *, trace_id: str) -> WorkflowArtifacts:
        # Ensure dependent agents exist before constructing orchestrator handoffs.
        self._registry.get_agent("router", output_type=RoutingDecision)
        self._registry.get_agent("markdown_cleaner", output_type=MarkdownCleanResult)
        self._registry.get_agent(
            "notebook_refactor", output_type=NotebookRefactorResult
        )
        self._registry.get_agent("reviewer", output_type=ReviewResult)
        self._registry.get_agent("namer", output_type=NamingResult)

        orchestrator_spec = self._config.agent_specs["orchestrator"]
        tool_descriptions = []
        for tool_spec in orchestrator_spec.tools:
            tool_name = tool_spec.tool_name or tool_spec.agent_key
            tool_descriptions.append(f"{tool_name} ({tool_spec.agent_key})")

        builder = ConversationBuilder()
        builder.add_developer(
            "You orchestrate the document preparation workflow. Use the provided specialist tools for routing, transformation, review, and naming."
        )
        if tool_descriptions:
            tool_list = ", ".join(tool_descriptions)
            builder.add_developer(
                f"Available tools: {tool_list}. Capture each tool's output before proceeding."
            )
        builder.add_developer(
            f"Do not exceed {self._config.rework_max_cycles} rework cycles. If you reach the limit, return review.approved=false and include the reviewer feedback."
        )
        builder.add_user(
            f"Document URL: {doc.url}\n"
            f"Metadata: {doc.metadata}\n\n"
            "--- Raw Document ---\n"
            f"{doc.content}\n"
            "--- End Document ---"
        )
        initial_messages = builder.build()

        metadata = {
            "stage": "workflow",
            "doc_url": doc.url,
            "rework_enabled": self._config.rework_enabled,
            "rework_max_cycles": self._config.rework_max_cycles,
        }
        session = self._create_session(doc.doc_id, "orchestrator")
        stage_result = await self._run_stage(
            agent_key="orchestrator",
            stage="workflow",
            doc=doc,
            input_items=initial_messages,
            metadata=metadata,
            output_type=WorkflowOutput,
            session=session,
            trace_id=trace_id,
        )
        run_result = stage_result.run_result

        final_output: WorkflowOutput = run_result.final_output
        trajectory = self._serialize_run_items(run_result)
        final_output_dict = final_output.model_dump(exclude_none=True)
        naming_extension = final_output.naming.extension
        if not naming_extension.startswith("."):
            naming_extension = f".{naming_extension}"

        review_result = ReviewResult(
            approved=final_output.review.approved,
            issues=final_output.review.issues,
            suggestions=final_output.review.suggestions,
        )
        naming_result = NamingResult(
            file_slug=final_output.naming.file_slug,
            extension=naming_extension,
            title=final_output.naming.title,
        )

        return WorkflowArtifacts(
            route=final_output.route,
            processed_text=final_output.processed_text,
            summary=final_output.summary,
            review=review_result,
            naming=naming_result,
            rework_cycles=final_output.rework_cycles,
            trajectory=trajectory,
            final_output=final_output_dict,
        )

    async def _run_manual(self, doc: DocTask, *, trace_id: str) -> WorkflowArtifacts:
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
            trace_id=trace_id,
        )
        conversation = await self._get_session_items(router_result.session)
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
                trace_id=trace_id,
            )
            conversation = await self._get_session_items(work_result.session)
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
                trace_id=trace_id,
            )
            conversation = await self._get_session_items(review.session)
            review_result = review.output
            if review_result.approved:
                break

            if (
                not self._config.rework_enabled
                or rework_cycles >= self._config.rework_max_cycles
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
                    trace_id=trace_id,
                )
                conversation = await self._get_session_items(router_retry.session)
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
            trace_id=trace_id,
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

        workflow_output = WorkflowOutput(
            route=route,
            processed_text=processed_text,
            summary=summary,
            review=WorkflowReviewResult(
                approved=review_result.approved,
                issues=review_result.issues,
                suggestions=review_result.suggestions,
            ),
            naming=WorkflowNamingResult(
                file_slug=naming_output.file_slug,
                extension=naming_output.extension,
                title=naming_output.title,
            ),
            rework_cycles=rework_cycles,
        )

        return WorkflowArtifacts(
            route=route,
            processed_text=processed_text,
            summary=summary,
            review=review_result,
            naming=naming_output,
            rework_cycles=rework_cycles,
            trajectory=[],
            final_output=workflow_output.model_dump(exclude_none=True),
        )

    def _serialize_run_items(self, run_result: RunResult) -> list[dict[str, Any]]:
        serialized: list[dict[str, Any]] = []
        for item in getattr(run_result, "new_items", []):
            entry: dict[str, Any] = {
                "type": getattr(item, "type", type(item).__name__),
                "agent": getattr(getattr(item, "agent", None), "name", None),
            }
            raw_item = getattr(item, "raw_item", None)
            entry["raw"] = self._jsonable(raw_item)

            if isinstance(item, MessageOutputItem):
                entry["role"] = getattr(item.raw_item, "role", None)
                entry["text"] = ItemHelpers.text_message_output(item)

            if isinstance(item, ToolCallItem):
                entry["tool_call_type"] = getattr(item.raw_item, "type", None)

            if isinstance(item, ToolCallOutputItem):
                entry["output"] = self._jsonable(item.output)

            if isinstance(item, ReasoningItem):
                entry["reasoning"] = self._jsonable(item.raw_item)

            serialized.append(entry)
        return serialized

    @staticmethod
    def _jsonable(value: Any) -> Any:
        if isinstance(value, BaseModel):
            return value.model_dump(exclude_none=True)
        if isinstance(value, dict):
            return {k: WorkflowRunner._jsonable(v) for k, v in value.items()}
        if isinstance(value, list):
            return [WorkflowRunner._jsonable(v) for v in value]
        return value

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

    @staticmethod
    def _create_session(doc_id: int, agent_key: str) -> SQLiteSession:
        """Return a session keyed to the document/stage pair."""

        session_id = f"doc-{doc_id}-{agent_key}"
        return SQLiteSession(session_id)

    @staticmethod
    async def _get_session_items(session: SQLiteSession) -> list[dict[str, Any]]:
        """Bridge session history access from asyncio into Trio."""

        return await trio_asyncio.aio_as_trio(session.get_items)()

    async def _run_stage(
        self,
        *,
        agent_key: str,
        stage: str,
        doc: DocTask,
        input_items: AgentInput,
        metadata: dict[str, Any],
        output_type: Any,
        session: SQLiteSession | None = None,
        trace_id: str | None = None,
    ) -> StageRunResult:
        stage_spec = self._config.agent_specs[agent_key]
        agent = self._registry.get_agent(agent_key, output_type=output_type)
        session = session or self._create_session(doc.doc_id, agent_key)

        async def attempt(attempt_index: int) -> RunResult[Any]:
            attempt_metadata = dict(metadata)
            attempt_metadata["stage"] = stage
            attempt_metadata["attempt"] = attempt_index
            attempt_metadata["progress_timeout_seconds"] = (
                stage_spec.progress_timeout_seconds
            )
            context = AgentCallContext(
                logger=self._logger,
                workflow_name=self._config.workflow_name,
                stage=stage,
                run_id=f"{agent_key}-{doc.doc_id}-try{attempt_index}",
                doc_url=doc.url,
                metadata=attempt_metadata,
                trace_id=trace_id,
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
                session=session,
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
            session=session,
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
    session: SQLiteSession
