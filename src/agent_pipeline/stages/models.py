"""Pydantic models for agent structured outputs."""

from __future__ import annotations

from typing import Any, Literal

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
    issues: str | None = None
    suggestions: str | None = None


class NamingResult(BaseModel):
    file_slug: str
    extension: str
    title: str | None = None
