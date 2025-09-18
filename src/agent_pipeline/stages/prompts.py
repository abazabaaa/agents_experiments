"""Prompt builders for agent stages."""

from __future__ import annotations

from ..config import PipelineConfig
from ..conversation import AgentInput, ConversationBuilder, user_message
from .types import DocTask, ProcessedDoc, ReviewedDoc, WorkItem


def _apply_template(
    template: str,
    *,
    kind: str,
    url: str,
    summary: str,
    document: str,
) -> str:
    return (
        template.replace("{TYPE}", kind)
        .replace("{URL}", url)
        .replace("{SUMMARY}", summary)
        .replace("{DOCUMENT}", document)
    )


def _feedback_message(feedback: str | None) -> str | None:
    if not feedback:
        return None
    feedback = feedback.strip()
    if not feedback:
        return None
    return f"Prior review feedback to address:\n{feedback}"


def build_router_prompt(config: PipelineConfig, task: DocTask) -> AgentInput:
    template = config.stage_prompts.get("router")
    if template:
        return [
            user_message(
                _apply_template(
                    template,
                    kind="N/A",
                    url=task.url,
                    summary="N/A",
                    document=task.content,
                )
            )
        ]

    builder = ConversationBuilder()
    builder.add_developer(
        "Classify the incoming document as markdown prose or a Jupyter notebook export."
    )
    builder.add_user(
        (
            f"URL: {task.url}\n\n"
            "--- Document Start ---\n"
            f"{task.content}\n"
            "--- Document End ---"
        )
    )
    return builder.build()


def build_markdown_prompt(config: PipelineConfig, item: WorkItem) -> AgentInput:
    template = config.stage_prompts.get("markdown_cleaner")
    if template:
        return [
            user_message(
                _apply_template(
                    template,
                    kind=item.kind,
                    url=item.url,
                    summary="N/A",
                    document=item.content,
                )
            )
        ]

    builder = ConversationBuilder()
    builder.add_developer(
        "Clean and normalize the following markdown documentation for publication."
    )
    feedback = _feedback_message(item.review_feedback)
    if feedback:
        builder.add_developer(feedback)
    builder.add_user(
        (f"URL: {item.url}\n--- Raw Markdown ---\n{item.content}\n--- End ---")
    )
    return builder.build()


def build_notebook_prompt(config: PipelineConfig, item: WorkItem) -> AgentInput:
    template = config.stage_prompts.get("notebook_refactor")
    if template:
        return [
            user_message(
                _apply_template(
                    template,
                    kind=item.kind,
                    url=item.url,
                    summary="N/A",
                    document=item.content,
                )
            )
        ]

    builder = ConversationBuilder()
    builder.add_developer(
        "Convert the notebook (JSON or markdown export) into a standalone Python script with explanatory comments."
    )
    feedback = _feedback_message(item.review_feedback)
    if feedback:
        builder.add_developer(feedback)
    builder.add_user(
        (f"URL: {item.url}\n--- Notebook Content ---\n{item.content}\n--- End ---")
    )
    return builder.build()


def build_review_prompt(config: PipelineConfig, doc: ProcessedDoc) -> AgentInput:
    summary = doc.summary or "N/A"
    template = config.stage_prompts.get("review")
    if template:
        return [
            user_message(
                _apply_template(
                    template,
                    kind=str(doc.kind),
                    url=doc.url,
                    summary=summary,
                    document=doc.processed_text,
                )
            )
        ]

    builder = ConversationBuilder()
    builder.add_developer(
        (
            "Review the transformed document for publication quality. Approve only if accurate, consistent, and well formatted.\n"
            "Output must be strict JSON with schema {approved: boolean, issues: string|null, suggestions: string|null}.\n"
            "No markdown, no code fences, no commentary beyond the JSON."
        )
    )
    builder.add_developer(
        "Keep strings concise: issues <= 1200 characters, suggestions <= 800 characters. Use short sentences, not long lists."
    )
    builder.add_user(
        (
            f"Type: {doc.kind}\n"
            f"URL: {doc.url}\n"
            f"Summary: {summary}\n"
            "--- Transformed Document ---\n"
            f"{doc.processed_text}\n"
            "--- End ---"
        )
    )
    return builder.build()


def build_naming_prompt(config: PipelineConfig, doc: ReviewedDoc) -> AgentInput:
    hint = doc.title_hint or "N/A"
    template = config.stage_prompts.get("namer")
    if template:
        return [
            user_message(
                _apply_template(
                    template,
                    kind=doc.kind,
                    url=doc.url,
                    summary=hint,
                    document=doc.processed_text,
                )
            )
        ]

    builder = ConversationBuilder()
    builder.add_developer(
        "Suggest a concise file slug and extension for the document. Use kebab-case for the slug."
    )
    builder.add_user(
        (
            f"Type: {doc.kind}\n"
            f"URL: {doc.url}\n"
            f"Hint: {hint}\n"
            "--- Content ---\n"
            f"{doc.processed_text}\n"
            "--- End ---"
        )
    )
    return builder.build()
