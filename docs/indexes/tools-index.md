# Python Development Tools Documentation Index

A comprehensive guide to UV, Ruff, and Ty documentation for Python development workflows.

## Table of Contents

- [UV Documentation](#uv-documentation) - Python package manager and build tool (8 files)
- [Ruff Documentation](#ruff-documentation) - Python linter and formatter (4 files)
- [Ty Documentation](#ty-documentation) - Python type checker (11 files)

---

## UV Documentation

Python package manager and build tool for modern Python development.

### [`docs/uv_docs/build.md`](../uv_docs/build.md)
**Summary:** Explains building Python distributions (sdists and wheels) using uv as build frontend, including `--build-constraint` for reproducible builds with hash verification and limiting to specific distribution types.

**Related:** Check [`docs/uv_docs/configuring.md`](../uv_docs/configuring.md) for build backend settings; the file itself embeds uv build command examples.

### [`docs/uv_docs/configuring.md`](../uv_docs/configuring.md)
**Summary:** Covers project configuration including `requires-python` for version requirements, `project.scripts`/`gui-scripts` entry points for CLI/GUI tools, build system setup, and related pyproject.toml settings.

**Related:** Pair with [`docs/uv_docs/build.md`](../uv_docs/build.md) for distribution steps and [`docs/uv_docs/syncing.md`](../uv_docs/syncing.md) for environment impacts; numerous pyproject fragments act as examples.

### [`docs/uv_docs/creating_projects.md`](../uv_docs/creating_projects.md)
**Summary:** Explains `uv init` for creating applications (default) or libraries (`--lib` flag), including pyproject.toml generation, main.py sample file, and target directory options with project structure examples.

**Related:** See [`docs/uv_docs/structure.md`](../uv_docs/structure.md) for layout expectations and [`docs/uv_docs/run_commands.md`](../uv_docs/run_commands.md) for executing the generated tooling; inline command sessions serve as examples.

### [`docs/uv_docs/dependencies.md`](../uv_docs/dependencies.md)
**Summary:** Explains project dependency management including `dependencies`, `optional-dependencies`, `dependency-groups` fields, `tool.uv.sources` for alternative sources, plus `uv add`/`remove` commands with constraint handling.

**Related:** Combine with [`docs/uv_docs/syncing.md`](../uv_docs/syncing.md) for lockfile effects and [`docs/uv_docs/run_commands.md`](../uv_docs/run_commands.md) for on-demand deps; the file contains rich pyproject and CLI examples.

### [`docs/uv_docs/run_commands.md`](../uv_docs/run_commands.md)
**Summary:** Demonstrates `uv run` for executing commands with automatic environment sync, `--with` flag for temporary dependencies, inline script metadata support, and platform-specific execution behaviors.

**Related:** Review [`docs/uv_docs/syncing.md`](../uv_docs/syncing.md) for locking flags and revisit inline script examples inside this file for reference.

### [`docs/uv_docs/structure.md`](../uv_docs/structure.md)
**Summary:** Details project structure including pyproject.toml requirements, `.venv` project environment management, universal `uv.lock` lockfile for cross-platform reproducibility, and managed environment configuration.

**Related:** Consult [`docs/uv_docs/creating_projects.md`](../uv_docs/creating_projects.md) for generated layouts and [`docs/uv_docs/syncing.md`](../uv_docs/syncing.md) for lock maintenance; embedded pyproject samples illustrate usage.

### [`docs/uv_docs/syncing.md`](../uv_docs/syncing.md)
**Summary:** Explains locking (dependency resolution) and syncing (environment installation) processes, including automatic behavior, `--locked`/`--frozen` flags, editable installations, and checking lockfile status.

**Related:** Tie back to [`docs/uv_docs/dependencies.md`](../uv_docs/dependencies.md) for metadata changes and [`docs/uv_docs/run_commands.md`](../uv_docs/run_commands.md) for invocation flags; CLI snippets throughout serve as examples.

### [`docs/uv_docs/workspaces.md`](../uv_docs/workspaces.md)
**Summary:** Details workspace concept for managing multiple packages together, including member/exclude globs, shared lockfile, workspace sources with `workspace=true` notation, and root vs member package operations.

**Related:** Coordinate with [`docs/uv_docs/dependencies.md`](../uv_docs/dependencies.md) for sources and [`docs/uv_docs/syncing.md`](../uv_docs/syncing.md) for multi-package sync behavior; inline pyproject and tree examples demonstrate patterns.

---

## Ruff Documentation

Fast Python linter and formatter, drop-in replacement for Flake8 and Black.

### [`docs/ruff/config.md`](../ruff/config.md)
**Summary:** Shows Ruff configuration via pyproject.toml/ruff.toml with complete default settings including exclude patterns, line-length, Python version target, enabled rules (E4/E7/E9/F), and Black-compatible format options.

**Related:** Reference [`docs/ruff/linter.md`](../ruff/linter.md) for CLI semantics and [`docs/ruff/format.md`](../ruff/format.md) for formatter settings; numerous pyproject excerpts provide examples.

### [`docs/ruff/format.md`](../ruff/format.md)
**Summary:** Presents the Ruff formatter as Black-compatible drop-in replacement, emphasizing performance and >99.9% formatting parity with Black on major projects, plus philosophy of consistency over innovation.

**Related:** Check [`docs/ruff/config.md`](../ruff/config.md) for enabling options and inspect the before-or-after code formatting examples within this file.

### [`docs/ruff/linter.md`](../ruff/linter.md)
**Summary:** Introduces the Ruff linter as drop-in replacement for Flake8+plugins, covering `ruff check` command, rule selection via prefixes (E, F, etc.), `lint.select`/`ignore` settings, and best practices for rule configuration.

**Related:** Combine with [`docs/ruff/config.md`](../ruff/config.md) for configuration knobs and [`docs/ruff/rules.md`](../ruff/rules.md) to see rule availability; inline command samples show practical usage.

### [`docs/ruff/rules.md`](../ruff/rules.md)
**Summary:** Provides comprehensive catalog of all Ruff rule families organized by source (Pyflakes, pycodestyle, etc.) with rule codes, descriptions, and direct links to detailed documentation.

**Related:** Use with [`docs/ruff/linter.md`](../ruff/linter.md) for enablement strategy and follow the linked rule pages for deeper examples.

---

## Ty Documentation

Python type checker focused on simplicity and speed.

### [`docs/ty/getting_started.md`](../ty/getting_started.md)
**Summary:** Getting started guide covering ty installation via uvx, basic `ty check` command usage, automatic environment discovery, and initial setup workflow.

**Related:** Review [`docs/ty/reference.md`](../ty/reference.md) for full CLI flags; embedded commands illustrate quick starts.

### [`docs/ty/config.md`](../ty/config.md)
**Summary:** Explains configuration file discovery order and precedence rules between pyproject.toml, ty.toml, .ty.toml, and user-level config files with merge semantics.

**Related:** Pair with [`docs/ty/configuration.md`](../ty/configuration.md) for individual option details; inline toml snippets serve as examples.

### [`docs/ty/configuration.md`](../ty/configuration.md)
**Summary:** Comprehensive reference for `tool.ty` settings including rules severity (ignore/warn/error), `environment.extra-paths`, `environment.python` for venv, `python-platform` targeting, and `python-version` for syntax analysis.

**Related:** Use alongside [`docs/ty/config.md`](../ty/config.md) for discovery context and consult [`docs/ty/exclusions.md`](../ty/exclusions.md) or [`docs/ty/modules.md`](../ty/modules.md) for applied examples; numerous pyproject fragments demonstrate usage.

### [`docs/ty/modules.md`](../ty/modules.md)
**Summary:** Details module discovery including first-party modules in root/src, third-party package search in Python environment, and automatic venv detection via `VIRTUAL_ENV` or `.venv` directory.

**Related:** Check [`docs/ty/configuration.md`](../ty/configuration.md) environment settings and [`docs/ty/getting_started.md`](../ty/getting_started.md) for command context; project layout diagrams act as examples.

### [`docs/ty/pythonversion.md`](../ty/pythonversion.md)
**Summary:** Explains `python-version` setting impact on syntax checking, stdlib symbol availability, version inference from project metadata, and version-specific type analysis behavior.

**Related:** Coordinate with [`docs/ty/configuration.md`](../ty/configuration.md) for the setting reference; inline code blocks demonstrate version-guarded examples.

### [`docs/ty/editors.md`](../ty/editors.md)
**Summary:** Documents ty editor integrations including VS Code extension, Neovim configuration, and generic LSP server setup for other editors with installation and configuration instructions.

**Related:** Reference [`docs/ty/reference.md`](../ty/reference.md) for `ty server` invocation; embedded configuration snippets show integration examples.

### [`docs/ty/exclusions.md`](../ty/exclusions.md)
**Summary:** Details file inclusion/exclusion with `src.include`/`exclude` patterns, gitignore-style syntax support, `.tyignore` files, and command-line path overrides for selective checking.

**Related:** Tie to [`docs/ty/configuration.md`](../ty/configuration.md) for exclude defaults and see [`docs/ty/rules.md`](../ty/rules.md) for handling residual diagnostics; toml examples inside illustrate patterns.

### [`docs/ty/suppression.md`](../ty/suppression.md)
**Summary:** Documents inline suppression with `ty: ignore[rule]` comments, standard `type: ignore` support, unused-ignore-comment detection, and `@no_type_check` decorator for disabling type checking.

**Related:** Review [`docs/ty/rules.md`](../ty/rules.md) for severity controls; inline code samples highlight suppression patterns.

### [`docs/ty/rules.md`](../ty/rules.md)
**Summary:** Explains ty's rule system with three severity levels (error/warn/ignore), showing how to configure via CLI flags (`--warn`, `--error`, `--ignore`) or `tool.ty.rules` section, with exit code behavior.

**Related:** Consult [`docs/ty/all_rules.md`](../ty/all_rules.md) for specific diagnostics and [`docs/ty/configuration.md`](../ty/configuration.md) for setting names; included CLI and toml snippets provide examples.

### [`docs/ty/all_rules.md`](../ty/all_rules.md)
**Summary:** Complete catalog of ty diagnostic rules with default levels, what-it-does explanations, why-is-this-bad rationale, and code examples showing incorrect vs correct patterns for each rule.

**Related:** Use with [`docs/ty/rules.md`](../ty/rules.md) to manage levels and [`docs/ty/reference.md`](../ty/reference.md) for invoking checks; each entry embeds illustrative examples.

### [`docs/ty/reference.md`](../ty/reference.md)
**Summary:** Complete CLI reference documenting `ty check` command with all flags, `ty server` for LSP integration, environment options, and output format controls with detailed flag descriptions.

**Related:** Pair with [`docs/ty/getting_started.md`](../ty/getting_started.md) for workflow context and [`docs/ty/config.md`](../ty/config.md) for configuration overrides; command listings within the file serve as examples.
