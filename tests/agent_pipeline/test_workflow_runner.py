from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
from typing import Any

import pytest
import trio
from agent_pipeline.agents.registry import AgentRegistry
from agent_pipeline.config import load_config
from agent_pipeline.limiters import LimiterPool
from agent_pipeline.logging import StructuredLogger
from agent_pipeline.retry import RetryPolicy
from agent_pipeline.conversation import ensure_conversation
from agent_pipeline.stages.models import (
    MarkdownCleanResult,
    NamingResult,
    ReviewResult,
    RoutingDecision,
    WorkflowNamingResult,
    WorkflowOutput,
    WorkflowReviewResult,
)
from agent_pipeline.stages.types import DocTask
from agent_pipeline.workflow.runner import WorkflowArtifacts, WorkflowRunner


class FakeRunItem:
    def __init__(self, content: str) -> None:
        self._message = {"role": "assistant", "content": content}

    def to_input_item(self) -> dict[str, str]:
        return dict(self._message)


class FakeRunResult:
    def __init__(self, final_output: Any, marker: str) -> None:
        self.final_output = final_output
        self._marker = marker
        self.new_items: list[FakeRunItem] = [FakeRunItem(marker)]
        self.input: list[dict[str, str]] = []


class FakeSession:
    def __init__(self) -> None:
        self.items: list[dict[str, str]] = []
        self.pop_calls = 0

    async def get_items(self, limit: int | None = None) -> list[dict[str, str]]:
        if limit is None:
            return list(self.items)
        return list(self.items[-limit:])

    async def add_items(self, new_items: list[dict[str, str]]) -> None:
        for item in new_items:
            self.items.append(dict(item))

    async def pop_item(self) -> dict[str, str] | None:
        self.pop_calls += 1
        if not self.items:
            return None
        return self.items.pop()

    async def clear_session(self) -> None:
        self.items.clear()


@pytest.fixture(scope="module")
def smoke_config() -> Any:
    return load_config(Path("configs/smoke_gpt5_nano.json"))


def make_manual_config(config: Any) -> Any:
    specs = dict(config.agent_specs)
    specs.pop("orchestrator", None)
    return replace(config, agent_specs=specs)


def _build_runner(config: Any, tmp_path: Path) -> WorkflowRunner:
    registry = AgentRegistry(config)
    limiter_pool = LimiterPool(overall_capacity=5, model_limits={})
    logger = StructuredLogger(quiet=True, verbose_path=tmp_path / "workflow.log")
    return WorkflowRunner(
        config=config,
        registry=registry,
        limiter_pool=limiter_pool,
        logger=logger,
    )


def test_workflow_runner_manual_success(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, smoke_config: Any
) -> None:
    config = make_manual_config(smoke_config)
    runner = _build_runner(config, tmp_path)
    doc = DocTask(
        doc_id=1, url="https://example.com/doc", content="raw document", metadata={}
    )
    session = FakeSession()

    stage_outputs = {
        "routing": [
            FakeRunResult(
                RoutingDecision(route="markdown", rationale="markdown content"),
                "routed",
            )
        ],
        "markdown": [
            FakeRunResult(
                MarkdownCleanResult(
                    cleaned_markdown="cleaned markdown", summary="summary"
                ),
                "cleaned",
            )
        ],
        "review": [
            FakeRunResult(
                ReviewResult(approved=True, issues=None, suggestions=None),
                "approved",
            )
        ],
        "naming": [
            FakeRunResult(
                NamingResult(file_slug="doc-clean", extension=".md", title="Doc Clean"),
                "named",
            )
        ],
    }

    async def fake_call_agent_with_retry(
        stage: str,
        doc_id: int,
        logger: StructuredLogger,
        retry_policy: RetryPolicy,
        attempt,
    ):
        return await attempt(1)

    async def fake_call_agent(*args, **kwargs):
        stage_name = kwargs["context"].stage
        try:
            result = stage_outputs[stage_name].pop(0)
        except (KeyError, IndexError) as exc:  # pragma: no cover
            raise AssertionError(f"Unexpected stage call: {stage_name}") from exc

        input_list = ensure_conversation(args[1])
        await session.add_items(input_list)
        await session.add_items(
            [item.to_input_item() for item in result.new_items]
        )
        result.input = input_list
        return result

    monkeypatch.setattr(
        "agent_pipeline.workflow.runner.call_agent_with_retry",
        fake_call_agent_with_retry,
    )
    monkeypatch.setattr("agent_pipeline.workflow.runner.call_agent", fake_call_agent)

    async def run_manual() -> WorkflowArtifacts:
        return await runner.process_document(doc, session=session)

    artifacts = trio.run(run_manual)
    assert artifacts.route == "markdown"
    assert artifacts.processed_text == "cleaned markdown"
    assert artifacts.summary == "summary"
    assert artifacts.review.approved is True
    assert artifacts.naming.extension == ".md"
    assert artifacts.rework_cycles == 0
    assert artifacts.trajectory == []
    assert artifacts.final_output["route"] == "markdown"
    assert all(not outputs for outputs in stage_outputs.values())

    assistant_contents = [
        item["content"]
        for item in session.items
        if item.get("role") == "assistant"
    ]
    assert assistant_contents == ["routed", "cleaned", "approved", "named"]


def test_workflow_runner_manual_rework_cycle(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, smoke_config: Any
) -> None:
    config = make_manual_config(smoke_config)
    runner = _build_runner(config, tmp_path)
    doc = DocTask(
        doc_id=2, url="https://example.com/rework", content="raw", metadata={}
    )
    session = FakeSession()

    stage_outputs = {
        "routing": [
            FakeRunResult(
                RoutingDecision(route="markdown", rationale="markdown"),
                "routed",
            ),
            FakeRunResult(
                RoutingDecision(route="markdown", rationale="still markdown"),
                "rerouted",
            ),
        ],
        "markdown": [
            FakeRunResult(
                MarkdownCleanResult(cleaned_markdown="draft", summary="draft summary"),
                "draft",
            ),
            FakeRunResult(
                MarkdownCleanResult(cleaned_markdown="final", summary="final summary"),
                "final",
            ),
        ],
        "review": [
            FakeRunResult(
                ReviewResult(approved=False, issues="needs polish", suggestions=None),
                "reject",
            ),
            FakeRunResult(
                ReviewResult(approved=True, issues=None, suggestions=None),
                "approve",
            ),
        ],
        "naming": [
            FakeRunResult(
                NamingResult(file_slug="doc-final", extension=".md", title=None),
                "named",
            )
        ],
    }

    async def fake_call_agent_with_retry(
        stage: str,
        doc_id: int,
        logger: StructuredLogger,
        retry_policy: RetryPolicy,
        attempt,
    ):
        return await attempt(1)

    async def fake_call_agent(*args, **kwargs):
        stage_name = kwargs["context"].stage
        try:
            result = stage_outputs[stage_name].pop(0)
        except (KeyError, IndexError) as exc:  # pragma: no cover
            raise AssertionError(f"Unexpected stage call: {stage_name}") from exc

        input_list = ensure_conversation(args[1])
        await session.add_items(input_list)
        await session.add_items(
            [item.to_input_item() for item in result.new_items]
        )
        result.input = input_list
        return result

    monkeypatch.setattr(
        "agent_pipeline.workflow.runner.call_agent_with_retry",
        fake_call_agent_with_retry,
    )
    monkeypatch.setattr("agent_pipeline.workflow.runner.call_agent", fake_call_agent)

    async def run_manual() -> WorkflowArtifacts:
        return await runner.process_document(doc, session=session)

    artifacts = trio.run(run_manual)
    assert artifacts.processed_text == "final"
    assert artifacts.summary == "final summary"
    assert artifacts.review.approved is True
    assert artifacts.rework_cycles == 1
    assert artifacts.trajectory == []
    assert artifacts.final_output["rework_cycles"] == 1
    assert all(not outputs for outputs in stage_outputs.values())

    assistant_contents = [
        item["content"]
        for item in session.items
        if item.get("role") == "assistant"
    ]
    assert "reject" not in assistant_contents
    assert assistant_contents.count("rerouted") == 1
    assert session.pop_calls > 0


def test_workflow_runner_orchestrator(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, smoke_config: Any
) -> None:
    runner = _build_runner(smoke_config, tmp_path)
    doc = DocTask(doc_id=3, url="https://example.com/orch", content="raw", metadata={})
    session = FakeSession()

    orchestrator_calls: list[Any] = []

    async def fake_call_agent(agent, input_items, **kwargs):
        orchestrator_calls.append(agent.name)
        input_list = ensure_conversation(input_items)
        final_output = WorkflowOutput(
            route="markdown",
            processed_text="orchestrated",
            summary="orchestrated summary",
            review=WorkflowReviewResult(
                approved=True,
                issues=None,
                suggestions=None,
            ),
            naming=WorkflowNamingResult(
                file_slug="orch-doc",
                extension="md",
                title="Orchestrated Doc",
            ),
            rework_cycles=0,
        )
        result = FakeRunResult(final_output, "orchestrated")
        await session.add_items(input_list)
        await session.add_items([item.to_input_item() for item in result.new_items])
        result.input = input_list
        return result

    async def fail_call_agent_with_retry(*args, **kwargs):  # pragma: no cover
        raise AssertionError(
            "manual runner should not invoke call_agent_with_retry in orchestrator mode"
        )

    monkeypatch.setattr("agent_pipeline.workflow.runner.call_agent", fake_call_agent)
    monkeypatch.setattr(
        "agent_pipeline.workflow.runner.call_agent_with_retry",
        fail_call_agent_with_retry,
    )

    async def run_orchestrator() -> WorkflowArtifacts:
        return await runner.process_document(doc, session=session)

    artifacts = trio.run(run_orchestrator)
    assert orchestrator_calls == ["WorkflowOrchestrator"]
    assert artifacts.processed_text == "orchestrated"
    assert artifacts.naming.extension == ".md"
    assert artifacts.review.approved is True
    assert artifacts.rework_cycles == 0
    assert artifacts.final_output["naming"]["file_slug"] == "orch-doc"


def test_load_config_missing_instructions(tmp_path: Path) -> None:
    config_path = tmp_path / "bad_config.json"
    missing_file = tmp_path / "missing.md"
    payload = {
        "logging": {},
        "io": {},
        "concurrency": {},
        "retry": {},
        "agents": {
            "router": {
                "name": "Router",
                "instructions_path": str(missing_file),
                "model": "gpt-5-nano",
            },
            "markdown_cleaner": {
                "name": "Markdown",
                "instructions": "Clean markdown",
                "model": "gpt-5-nano",
            },
            "notebook_refactor": {
                "name": "Notebook",
                "instructions": "Refactor notebook",
                "model": "gpt-5-nano",
            },
            "reviewer": {
                "name": "Reviewer",
                "instructions": "Review",
                "model": "gpt-5-nano",
            },
            "namer": {
                "name": "Namer",
                "instructions": "Name",
                "model": "gpt-5-nano",
            },
        },
    }
    config_path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(FileNotFoundError):
        load_config(config_path)
