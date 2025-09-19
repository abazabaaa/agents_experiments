hen executing Python code, the assistant must NEVER invoke Python directly. Instead, the assistant must ALWAYS use `uv run` to ensure proper environment isolation and dependency management.

**Incorrect approach (FORBIDDEN):**
```
python - <<'PY'
import sys
print(f"Running on Python {sys.version}")
PY
```

**Correct approach (REQUIRED):**
```
uv run python - <<'PY'
import sys
print(f"Running on Python {sys.version}")
PY
```
<project_context>
This is a Python development project that prioritizes code quality, maintainability, and reliable testing. Your role is to help develop robust, well-tested code that follows established patterns and best practices. The project uses modern Python tooling with uv as the package manager.
</project_context>

<development_guidelines>

## Package Management with uv

<motivation>
We use uv exclusively for package management because it provides consistent, reproducible environments and faster dependency resolution than traditional tools.
</motivation>

<instructions>
- Install packages: `uv add package`
- Run tools: `uv run tool`
- Upgrade packages: `uv add --dev package --upgrade-package package`
- Sync dependencies: `uv sync` (run this frequently to ensure consistency)
- For any package operations, always use the uv commands shown above
</instructions>

## Code Quality Standards

<motivation>
High-quality code reduces bugs, improves maintainability, and makes collaboration easier. These standards help ensure our codebase remains professional and scalable.
</motivation>

<requirements>
- Include type hints for all function parameters and return values
- Write docstrings for all public APIs following Google style
- Design functions to be focused and single-purpose
- Follow established patterns in the existing codebase for consistency
- Format code with 88-character line limits for readability
</requirements>

<formatting_guidelines>
When lines exceed 88 characters:
- For strings: wrap using parentheses for implicit concatenation
- For function calls: use multi-line format with proper indentation
- For imports: split into multiple lines with one import per line
</formatting_guidelines>

## Testing Excellence

<motivation>
Comprehensive testing catches bugs early, documents expected behavior, and enables confident refactoring. Well-written tests serve as living documentation of how code should behave.
</motivation>

<testing_approach>
- Framework: Execute tests with `uv run pytest`
- Write tests that cover edge cases and error conditions
- Include tests for all new features
- Add regression tests when fixing bugs
- Current test migration: Tests in `tests_old/` need rewriting to modern standards
</testing_approach>

## Version Control Best Practices

<commit_messages>
Write clear, descriptive commit messages that explain the change and its purpose.

For user-reported issues, acknowledge the reporter:
```bash
git commit --trailer "Reported-by: <user_name>"
```

For GitHub issues, reference the issue number:
```bash
git commit --trailer "Github-Issue: #<number>"
```

Focus commit messages on describing the problem solved and the approach taken.
</commit_messages>

<pull_requests>
- Write detailed PR descriptions focusing on:
  - The problem being solved
  - The high-level approach taken
  - Any important design decisions
- Add Tom and Bob as reviewers for all PRs
- Keep PR descriptions focused on the change itself, not the tools used
</pull_requests>

## Development Workflow

<setup>
- Initialize your environment with `uv lock && uv sync --group dev && uv run pre-commit install` to refresh the lockfile, install the dev group into `.venv`, and register the hooks in the managed env.
- Remember that `uv run` automatically locks and syncs before each command; pass `--locked`/`--frozen` in CI if you need deterministic lockfiles.
</setup>

<code_formatting>
Use Ruff for consistent Python formatting (scoped to `src/` and `tests/`):
- Format code: `uv run ruff format src tests`
- Check style: `uv run ruff check src tests`
- Apply fixes: `uv run ruff check src tests --fix`

Key formatting considerations:
- Line length: 88 characters maximum
- Import sorting: follows isort conventions (I001)
- Remove unused imports for clean code
</code_formatting>

<justfile_shortcuts>
Prefer the project Justfile for common routines:
- `just format` / `just lint` / `just style` for Ruff formatting and checks
- `just typecheck` to run `uv run ty check .`
- `just precommit` to execute all pre-commit hooks (`uv run pre-commit run --all-files`)
- `just quality` to chain formatting, linting, and type checking in one go
</justfile_shortcuts>

<type_checking>
Ensure type safety with ty, Astral's blazingly fast type checker:
- Command: `uv run ty check`
- What ty does:
  - Performs static type analysis on Python code
  - Provides detailed, informative error messages
  - Automatically discovers virtual environments and project structure
  - Utilizes all CPU cores for exceptional performance
- Requirements for your code:
  - Explicit None checks for Optional types
  - Proper type narrowing for string operations
  - All functions properly typed with annotations
- Note: ty is pre-alpha but rapidly improving, created by the team behind Ruff and uv
</type_checking>

<pre_commit_hooks>
The project uses pre-commit hooks defined in `.pre-commit-config.yaml`:
- Prettier: Formats YAML/JSON files  
- Ruff: Enforces Python style
- ty: Validates type annotations

To update Ruff in pre-commit:
1. Check latest version on PyPI
2. Update the rev in config
3. Commit the config update first
</pre_commit_hooks>

## Problem Resolution Guide

<ci_failure_resolution>
When CI fails, address issues in this order for efficiency:
1. Run formatting tools first (`uv run ruff format src tests`)
2. Fix type errors identified by `uv run ty check src tests`
3. Resolve any remaining linting issues

For type errors from ty:
- Examine the full line context in ty's detailed error messages
- Verify Optional type handling
- Add appropriate type narrowing
- Ensure function signatures match usage
- ty provides informative diagnostics explaining both what's wrong and how to fix it
</ci_failure_resolution>

<best_practices>
- Check `git status` before committing to review changes
- Run formatters before type checkers to avoid cascading issues
- Make minimal, focused changes that address specific problems
- Follow existing code patterns for consistency
- Document all public APIs with clear docstrings
- Write comprehensive tests for new functionality
</best_practices>

</development_guidelines>


## CRITICAL BEHAVIORS

- Reading the documentation before beginning code changes is a critical part of ensure adherence to APIs/SDKs. You have access to documentation for trio, trio-asyncio, openai agents sdk ([text](docs/openai-agents-sdk)), uv, ty, ruff, fastmcp, lark and claude code sdk. You should always LS the docs dir, then LS recursively into the docs dirs of interest the recursively rg to explore example code, patterns, function signatures, class signatures/methods and overloads. 

**BAD WORKFLOW:**

1) recieve issue or new feature to implement from the user
2) read through code and identify issues/code touch points or requirements for feature implementation
3) implement the feature or fix the bug

**GOOD WORKFLOW:**

1) recieve issue or new feature to implement from the user
2) read through code and identify issues/code touch points or requirements for feature implementation
3) recursively and proactively investigate the docs/ dir the validate/verify/learn patterns, function signatures, methods, classes, overloads from md documation or example code.
4) PLAN your implementation based on the insight from the documentation
5) implement the fix or feature
