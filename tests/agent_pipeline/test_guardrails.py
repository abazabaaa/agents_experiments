from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest
from agent_pipeline.agents.guardrails import (
    INPUT_GUARDRAIL_REGISTRY,
    reject_empty_document,
    resolve_input_guardrails,
    resolve_output_guardrails,
)


def _run_guardrail(*args):
    return asyncio.run(reject_empty_document.guardrail_function(*args))


def test_reject_empty_document_accepts_text() -> None:
    ctx = SimpleNamespace(context=SimpleNamespace(logger=None, doc_url="doc"))
    result = _run_guardrail(ctx, SimpleNamespace(name="Router"), "Hello")
    assert result.tripwire_triggered is False
    assert result.output_info["reason"] == "document accepted"


def test_reject_empty_document_rejects_blank_payload() -> None:
    ctx = SimpleNamespace(context=SimpleNamespace(logger=None, doc_url="doc"))
    result = _run_guardrail(ctx, SimpleNamespace(name="Router"), "   ")
    assert result.tripwire_triggered is True
    assert result.output_info["reason"] == "empty document rejected"


def test_reject_empty_document_handles_message_list() -> None:
    messages = [
        {"role": "developer", "content": "instructions"},
        {"role": "user", "content": "   important doc   "},
        {"role": "assistant", "content": "irrelevant"},
        "not-a-dict",
        {"role": "user", "content": None},
    ]
    ctx = SimpleNamespace(context=SimpleNamespace(logger=None, doc_url="doc"))
    result = _run_guardrail(ctx, SimpleNamespace(name="Router"), messages)
    assert result.tripwire_triggered is False


def test_reject_empty_document_without_context() -> None:
    ctx = SimpleNamespace()  # no ``context`` attribute
    result = _run_guardrail(ctx, SimpleNamespace(name="Router"), "")
    assert result.tripwire_triggered is True


def test_resolve_input_guardrails_known() -> None:
    guardrail = resolve_input_guardrails(["reject_empty_document"])
    assert guardrail == [INPUT_GUARDRAIL_REGISTRY["reject_empty_document"]]


def test_resolve_input_guardrails_unknown() -> None:
    with pytest.raises(KeyError):
        resolve_input_guardrails(["unknown_guardrail"])


def test_resolve_output_guardrails_empty() -> None:
    assert resolve_output_guardrails([]) == []


def test_resolve_output_guardrails_unknown() -> None:
    with pytest.raises(KeyError):
        resolve_output_guardrails(["unknown_output_guardrail"])
