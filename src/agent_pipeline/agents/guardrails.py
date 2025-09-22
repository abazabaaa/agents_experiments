"""Built-in guardrails for pipeline agent executions."""

from __future__ import annotations

from collections.abc import Awaitable, Callable, Iterable, Sequence
from typing import Any

from agents import Agent, GuardrailFunctionOutput, RunContextWrapper, input_guardrail

# Aliases for guardrail callables to keep type hints concise.
InputGuardrailFunc = Callable[
    [RunContextWrapper[Any], Agent[Any], Any], Awaitable[GuardrailFunctionOutput]
]
OutputGuardrailFunc = Callable[
    [RunContextWrapper[Any], Agent[Any], Any], Awaitable[GuardrailFunctionOutput]
]


def _extract_user_text(input_payload: Any) -> str:
    """Return concatenated user message text from an agent input payload."""

    if isinstance(input_payload, str):
        return input_payload

    if isinstance(input_payload, Sequence):
        parts: list[str] = []
        for item in input_payload:
            if not isinstance(item, dict):
                continue
            role = item.get("role")
            if role == "user":
                content = item.get("content")
                if isinstance(content, str):
                    parts.append(content)
        return "\n".join(parts)

    return ""


@input_guardrail
async def reject_empty_document(
    ctx: RunContextWrapper[Any],
    agent: Agent[Any],
    input_payload: Any,
) -> GuardrailFunctionOutput:
    """Trip when the initial document payload is empty after trimming."""

    text_content = _extract_user_text(input_payload).strip()
    if text_content:
        return GuardrailFunctionOutput(
            output_info={"reason": "document accepted"},
            tripwire_triggered=False,
        )

    context_obj = getattr(ctx, "context", None)
    logger = getattr(context_obj, "logger", None)
    if logger is not None:
        logger.warning(
            "Guardrail reject_empty_document triggered: agent=%s doc_url=%s",
            agent.name,
            getattr(ctx.context, "doc_url", "unknown"),
        )

    return GuardrailFunctionOutput(
        output_info={"reason": "empty document rejected"},
        tripwire_triggered=True,
    )


INPUT_GUARDRAIL_REGISTRY: dict[str, InputGuardrailFunc] = {
    "reject_empty_document": reject_empty_document,
}

OUTPUT_GUARDRAIL_REGISTRY: dict[str, OutputGuardrailFunc] = {}


def resolve_input_guardrails(names: Iterable[str]) -> list[InputGuardrailFunc]:
    """Convert guardrail names into callables, raising on unknown entries."""

    resolved: list[InputGuardrailFunc] = []
    for name in names:
        guardrail = INPUT_GUARDRAIL_REGISTRY.get(name)
        if guardrail is None:
            raise KeyError(f"Unknown input guardrail '{name}'")
        resolved.append(guardrail)
    return resolved


def resolve_output_guardrails(names: Iterable[str]) -> list[OutputGuardrailFunc]:
    """Resolve output guardrail names, maintaining parity with input helpers."""

    resolved: list[OutputGuardrailFunc] = []
    for name in names:
        guardrail = OUTPUT_GUARDRAIL_REGISTRY.get(name)
        if guardrail is None:
            raise KeyError(f"Unknown output guardrail '{name}'")
        resolved.append(guardrail)
    return resolved
