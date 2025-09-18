"""Prompt builders for agent stages.

This module supports stage-specific prompt templates provided at runtime via
``PipelineConfig.stage_prompts``. Templates can reference the following tokens:

- {TYPE}      → Document kind (e.g., "markdown", "notebook")
- {URL}       → Source URL
- {SUMMARY}   → Short summary if available
- {DOCUMENT}  → Full document content to be reviewed/processed

If a template is not provided for a stage, a reasonable default is used.

Note: The OpenAI Agents SDK treats string inputs as user messages. For better
control, we can return structured message lists with explicit roles (user,
developer, system).
"""

from __future__ import annotations

from typing import Any

from ..config import PipelineConfig
from .types import DocTask, ProcessedDoc, ReviewedDoc, WorkItem

# Type alias for agent input - either a string or list of message items
AgentInput = str | list[dict[str, Any]]


def build_developer_message(content: str) -> dict[str, Any]:
    """Build a developer message item for the OpenAI Agents SDK.

    Developer messages have higher priority than user messages and are
    useful for injecting context or instructions.
    """
    return {
        "role": "developer",
        "type": "message",
        "content": [{"type": "input_text", "text": content}],
    }


def build_user_message(content: str) -> dict[str, Any]:
    """Build a user message item for the OpenAI Agents SDK."""
    return {
        "role": "user",
        "type": "message",
        "content": [{"type": "input_text", "text": content}],
    }


def build_router_prompt(config: PipelineConfig, task: DocTask) -> AgentInput:
    template = config.stage_prompts.get("router")
    if template:
        return (
            template.replace("{TYPE}", "N/A")
            .replace("{URL}", task.url)
            .replace("{SUMMARY}", "N/A")
            .replace("{DOCUMENT}", task.content)
        )
    return (
        "You will classify documentation content.\n\n"
        f"URL: {task.url}\n\n"
        "--- Document Start ---\n"
        f"{task.content}\n"
        "--- Document End ---\n\n"
        "Respond with whether this is markdown prose or a Jupyter notebook export."
    )


def build_markdown_prompt(config: PipelineConfig, item: WorkItem) -> AgentInput:
    feedback = (
        f"\nPrior review feedback to address: {item.review_feedback}\n"
        if item.review_feedback
        else "\n"
    )
    template = config.stage_prompts.get("markdown_cleaner")
    if template:
        return (
            template.replace("{TYPE}", item.kind)
            .replace("{URL}", item.url)
            .replace("{SUMMARY}", "N/A")
            .replace("{DOCUMENT}", item.content)
        )
    return (
        "Clean and normalize the following markdown documentation."
        f"{feedback}URL: {item.url}\n"
        "--- Raw Markdown ---\n"
        f"{item.content}\n"
        "--- End ---"
    )


def build_notebook_prompt(config: PipelineConfig, item: WorkItem) -> AgentInput:
    feedback = (
        f"\nPrior review feedback to address: {item.review_feedback}\n"
        if item.review_feedback
        else "\n"
    )
    template = config.stage_prompts.get("notebook_refactor")
    if template:
        return (
            template.replace("{TYPE}", item.kind)
            .replace("{URL}", item.url)
            .replace("{SUMMARY}", "N/A")
            .replace("{DOCUMENT}", item.content)
        )
    return (
        "Convert the notebook (JSON or markdown export) into a standalone Python script with explanatory comments."
        f"{feedback}URL: {item.url}\n"
        "--- Notebook Content ---\n"
        f"{item.content}\n"
        "--- End ---"
    )


def _render_template(template: str, *, doc: ProcessedDoc) -> str:
    summary = doc.summary or "N/A"
    return (
        template.replace("{TYPE}", str(doc.kind))
        .replace("{URL}", doc.url)
        .replace("{SUMMARY}", summary)
        .replace("{DOCUMENT}", doc.processed_text)
    )


def build_review_prompt(config: PipelineConfig, doc: ProcessedDoc) -> AgentInput:
    summary = doc.summary or "N/A"
    user_template = config.stage_prompts.get("review")
    if user_template:
        return _render_template(user_template, doc=doc)

    # Default, conservative template emphasizing strict JSON output
    default = (
        "Review the transformed document for publication quality. Approve only if accurate,"
        " consistent, and well formatted.\n"
        "Output must be strict JSON matching this schema exactly:"
        " {approved: boolean, issues: string|null, suggestions: string|null}.\n"
        "No markdown, no code fences, no extra commentary.\n"
        "Keep strings concise: issues <= 1200 chars, suggestions <= 800 chars."
        " Use short sentences, not long lists.\n"
        f"Type: {doc.kind}\n"
        f"URL: {doc.url}\n"
        f"Summary: {summary}\n"
        "--- Transformed Document ---\n"
        f"{doc.processed_text}\n"
        "--- End ---\n"
        "Return approved=true only if production ready."
    )
    return default


def build_naming_prompt(config: PipelineConfig, doc: ReviewedDoc) -> AgentInput:
    hint = doc.title_hint or "N/A"
    template = config.stage_prompts.get("namer")
    if template:
        return (
            template.replace("{TYPE}", doc.kind)
            .replace("{URL}", doc.url)
            .replace("{SUMMARY}", hint)
            .replace("{DOCUMENT}", doc.processed_text)
        )
    return (
        "Suggest a concise file slug and extension for the following documentation. Use kebab-case for the slug.\n"
        f"Type: {doc.kind}\n"
        f"URL: {doc.url}\n"
        f"Hint: {hint}\n"
        "--- Content ---\n"
        f"{doc.processed_text}\n"
        "--- End ---"
    )
