"""Prompt builders for agent stages."""

from __future__ import annotations

from .types import DocTask, WorkItem, ProcessedDoc, ReviewedDoc


def build_router_prompt(task: DocTask) -> str:
    return (
        "You will classify documentation content.\n\n"
        f"URL: {task.url}\n\n"
        "--- Document Start ---\n"
        f"{task.content}\n"
        "--- Document End ---\n\n"
        "Respond with whether this is markdown prose or a Jupyter notebook export."
    )


def build_markdown_prompt(item: WorkItem) -> str:
    feedback = (
        f"\nPrior review feedback to address: {item.review_feedback}\n"
        if item.review_feedback
        else "\n"
    )
    return (
        "Clean and normalize the following markdown documentation."
        f"{feedback}URL: {item.url}\n"
        "--- Raw Markdown ---\n"
        f"{item.content}\n"
        "--- End ---"
    )


def build_notebook_prompt(item: WorkItem) -> str:
    feedback = (
        f"\nPrior review feedback to address: {item.review_feedback}\n"
        if item.review_feedback
        else "\n"
    )
    return (
        "Convert the notebook (JSON or markdown export) into a standalone Python script with explanatory comments."
        f"{feedback}URL: {item.url}\n"
        "--- Notebook Content ---\n"
        f"{item.content}\n"
        "--- End ---"
    )


def build_review_prompt(doc: ProcessedDoc) -> str:
    summary = doc.summary or "N/A"
    return (
        "Review the transformed document for quality. Approve only if it is accurate and well formatted.\n"
        f"Type: {doc.kind}\n"
        f"URL: {doc.url}\n"
        f"Summary: {summary}\n"
        "--- Transformed Document ---\n"
        f"{doc.processed_text}\n"
        "--- End ---\n"
        "Return approved=true if the document is production ready."
    )


def build_naming_prompt(doc: ReviewedDoc) -> str:
    hint = doc.title_hint or "N/A"
    return (
        "Suggest a concise file slug and extension for the following documentation. Use kebab-case for the slug.\n"
        f"Type: {doc.kind}\n"
        f"URL: {doc.url}\n"
        f"Hint: {hint}\n"
        "--- Content ---\n"
        f"{doc.processed_text}\n"
        "--- End ---"
    )
