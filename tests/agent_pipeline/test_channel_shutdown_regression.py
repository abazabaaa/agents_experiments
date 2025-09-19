from __future__ import annotations

import functools
import pathlib
from types import SimpleNamespace
from typing import Any

import pytest
import trio
from agent_pipeline.pipeline import Pipeline
from agent_pipeline.stages.types import CompletionCounter, DocTask, NamedDoc
from agent_pipeline.stages.writer import writer_stage


async def _producer_without_close(send: trio.MemorySendChannel[int]) -> None:
    clone = send.clone()
    await clone.send(1)
    # Intentionally skip closing the clone to model the historical leak.


async def _consumer(receive: trio.MemoryReceiveChannel[int]) -> None:
    async with receive:
        async for _ in receive:
            pass


def test_memory_channel_clone_leak_blocks_consumer() -> None:
    async def run() -> None:
        with trio.fail_after(0.1):
            send, receive = trio.open_memory_channel[int](0)
            async with trio.open_nursery() as nursery:
                nursery.start_soon(_producer_without_close, send)
                nursery.start_soon(_consumer, receive)

    with pytest.raises(trio.TooSlowError):
        trio.run(run)


class _DummyLogger:
    def verbose(self, message: str) -> None:  # pragma: no cover - noop utility
        pass

    def info(self, message: str, *, spacer: bool = False) -> None:  # pragma: no cover
        pass

    def warning(self, message: str) -> None:  # pragma: no cover
        pass

    def error(self, message: str) -> None:  # pragma: no cover
        pass

    def debug(self, message: str) -> None:  # pragma: no cover
        pass


class _FakeWorkflowRunner:
    def __init__(self, artifacts: Any) -> None:
        self._artifacts = artifacts

    async def process_document(self, doc: DocTask) -> Any:  # pragma: no cover - simple stub
        return self._artifacts


def test_pipeline_process_document_closes_send_clone(tmp_path: pathlib.Path) -> None:
    output_dir = tmp_path / "out"
    logger = _DummyLogger()

    artifacts = SimpleNamespace(
        route="markdown",
        summary="processed",
        review=SimpleNamespace(approved=True, issues=[], suggestions=[]),
        naming=SimpleNamespace(file_slug="example", extension=".md"),
        processed_text="content",
        metadata={"review_approved": True},
        trajectory=None,
        final_output={"status": "ok"},
        rework_cycles=0,
    )

    doc = DocTask(
        doc_id=1,
        url="https://example.com",
        content="body",
        metadata={},
    )

    async def run() -> None:
        pipeline = object.__new__(Pipeline)
        pipeline.logger = logger
        pipeline.failures = []
        pipeline._failure_lock = trio.Lock()
        pipeline.config = SimpleNamespace()

        workflow_runner = _FakeWorkflowRunner(artifacts)

        send, receive = trio.open_memory_channel[NamedDoc](0)
        completion_counter = CompletionCounter(total=1)
        semaphore = trio.Semaphore(1)

        output_dir.mkdir(parents=True, exist_ok=True)

        with trio.fail_after(0.5):
            async with trio.open_nursery() as nursery:
                writer_task = functools.partial(
                    writer_stage,
                    receive=receive,
                    output_directory=output_dir,
                    logger=logger,
                    completion_counter=completion_counter,
                )
                nursery.start_soon(writer_task)
                nursery.start_soon(
                    pipeline._process_document,
                    workflow_runner,
                    doc,
                    send.clone(),
                    semaphore,
                    completion_counter,
                )
                nursery.start_soon(
                    pipeline._close_writer_when_done,
                    completion_counter,
                    send,
                )

    trio.run(run)

    produced = list(output_dir.glob("*.md"))
    assert produced, "writer should produce an output file"
    assert produced[0].read_text(encoding="utf-8") == "content"
