"""Pydantic models for agent structured outputs."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class RoutingDecision(BaseModel):
    route: Literal["markdown", "notebook"]
    rationale: str | None = None
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)


class MarkdownCleanResult(BaseModel):
    cleaned_markdown: str
    summary: str | None = None


class NotebookRefactorResult(BaseModel):
    python_script: str
    summary: str | None = None


class ReviewResult(BaseModel):
    approved: bool
    # Keep reviewer text compact to reduce truncation/JSON breakage.
    issues: str | None = Field(default=None, max_length=1200)
    suggestions: str | None = Field(default=None, max_length=800)


class NamingResult(BaseModel):
    file_slug: str
    extension: str
    title: str | None = None


class WorkflowReviewResult(BaseModel):
    approved: bool
    issues: str | None = Field(default=None, max_length=1200)
    suggestions: str | None = Field(default=None, max_length=800)


class WorkflowNamingResult(BaseModel):
    file_slug: str
    extension: str
    title: str | None = None


class WorkflowOutput(BaseModel):
    route: Literal["markdown", "notebook"]
    processed_text: str
    summary: str | None = None
    review: WorkflowReviewResult
    naming: WorkflowNamingResult
    rework_cycles: int = Field(ge=0)
