[Skip to content](https://docs.astral.sh/ruff/linter/#the-ruff-linter)

# [The Ruff Linter](https://docs.astral.sh/ruff/linter/\#the-ruff-linter)

The Ruff Linter is an extremely fast Python linter designed as a drop-in replacement for [Flake8](https://pypi.org/project/flake8/)
(plus dozens of plugins), [isort](https://pypi.org/project/isort/), [pydocstyle](https://pypi.org/project/pydocstyle/),
[pyupgrade](https://pypi.org/project/pyupgrade/), [autoflake](https://pypi.org/project/autoflake/),
and more.

## [`ruff check`](https://docs.astral.sh/ruff/linter/\#ruff-check)

`ruff check` is the primary entrypoint to the Ruff linter. It accepts a list of files or
directories, and lints all discovered Python files, optionally fixing any fixable errors.
When linting a directory, Ruff searches for Python files recursively in that directory
and all its subdirectories:

```
ruff check                  # Lint files in the current directory.
ruff check --fix            # Lint files in the current directory and fix any fixable errors.
ruff check --watch          # Lint files in the current directory and re-lint on change.
ruff check path/to/code/    # Lint files in `path/to/code`.

```

For the full list of supported options, run `ruff check --help`.

## [Rule selection](https://docs.astral.sh/ruff/linter/\#rule-selection)

The set of enabled rules is controlled via the [`lint.select`](https://docs.astral.sh/ruff/settings/#lint_select),
[`lint.extend-select`](https://docs.astral.sh/ruff/settings/#lint_extend-select), and [`lint.ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore) settings.

Ruff's linter mirrors Flake8's rule code system, in which each rule code consists of a one-to-three
letter prefix, followed by three digits (e.g., `F401`). The prefix indicates that "source" of the rule
(e.g., `F` for Pyflakes, `E` for pycodestyle, `ANN` for flake8-annotations).

Rule selectors like [`lint.select`](https://docs.astral.sh/ruff/settings/#lint_select) and [`lint.ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore) accept either
a full rule code (e.g., `F401`) or any valid prefix (e.g., `F`). For example, given the following
configuration file:

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_1_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_1_2)

```
[tool.ruff.lint]
select = ["E", "F"]
ignore = ["F401"]

```

```
[lint]
select = ["E", "F"]
ignore = ["F401"]

```

Ruff would enable all rules with the `E` (pycodestyle) or `F` (Pyflakes) prefix, with the exception
of `F401`. For more on configuring Ruff via `pyproject.toml`, see [_Configuring Ruff_](https://docs.astral.sh/ruff/configuration/).

As a special-case, Ruff also supports the `ALL` code, which enables all rules. Note that some
pydocstyle rules conflict (e.g., `D203` and `D211`) as they represent alternative docstring
formats. Ruff will automatically disable any conflicting rules when `ALL` is enabled.

If you're wondering how to configure Ruff, here are some **recommended guidelines**:

- Prefer [`lint.select`](https://docs.astral.sh/ruff/settings/#lint_select) over [`lint.extend-select`](https://docs.astral.sh/ruff/settings/#lint_extend-select) to make your rule set explicit.
- Use `ALL` with discretion. Enabling `ALL` will implicitly enable new rules whenever you upgrade.
- Start with a small set of rules ( `select = ["E", "F"]`) and add a category at-a-time. For example,
you might consider expanding to `select = ["E", "F", "B"]` to enable the popular flake8-bugbear
extension.

For example, a configuration that enables some of the most popular rules (without being too
pedantic) might look like the following:

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_2_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_2_2)

```
[tool.ruff.lint]
select = [\
    # pycodestyle\
    "E",\
    # Pyflakes\
    "F",\
    # pyupgrade\
    "UP",\
    # flake8-bugbear\
    "B",\
    # flake8-simplify\
    "SIM",\
    # isort\
    "I",\
]

```

```
[lint]
select = [\
    # pycodestyle\
    "E",\
    # Pyflakes\
    "F",\
    # pyupgrade\
    "UP",\
    # flake8-bugbear\
    "B",\
    # flake8-simplify\
    "SIM",\
    # isort\
    "I",\
]

```

To resolve the enabled rule set, Ruff may need to reconcile [`lint.select`](https://docs.astral.sh/ruff/settings/#lint_select) and
[`lint.ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore) from a variety of sources, including the current `pyproject.toml`,
any inherited `pyproject.toml` files, and the CLI (e.g., [`--select`](https://docs.astral.sh/ruff/settings/#lint_select)).

In those scenarios, Ruff uses the "highest-priority" [`select`](https://docs.astral.sh/ruff/settings/#lint_select) as the basis for
the rule set, and then applies [`extend-select`](https://docs.astral.sh/ruff/settings/#lint_extend-select) and
[`ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore) adjustments. CLI options are given higher priority than
`pyproject.toml` options, and the current `pyproject.toml` file is given higher priority than any
inherited `pyproject.toml` files.

For example, given the following configuration file:

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_3_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_3_2)

```
[tool.ruff.lint]
select = ["E", "F"]
ignore = ["F401"]

```

```
[lint]
select = ["E", "F"]
ignore = ["F401"]

```

Running `ruff check --select F401` would result in Ruff enforcing `F401`, and no other rules.

Running `ruff check --extend-select B` would result in Ruff enforcing the `E`, `F`, and `B` rules,
with the exception of `F401`.

## [Fixes](https://docs.astral.sh/ruff/linter/\#fixes)

Ruff supports automatic fixes for a variety of lint errors. For example, Ruff can remove unused
imports, reformat docstrings, rewrite type annotations to use newer Python syntax, and more.

To enable fixes, pass the `--fix` flag to `ruff check`:

```
ruff check --fix

```

By default, Ruff will fix all violations for which safe fixes are available; to determine
whether a rule supports fixing, see [_Rules_](https://docs.astral.sh/ruff/rules/).

### [Fix safety](https://docs.astral.sh/ruff/linter/\#fix-safety)

Ruff labels fixes as "safe" and "unsafe". The meaning and intent of your code will be retained when
applying safe fixes, but the meaning could change when applying unsafe fixes.

Specifically, an unsafe fix could lead to a change in runtime behavior, the removal of comments, or both,
while safe fixes are intended to preserve runtime behavior and will only remove comments when deleting
entire statements or expressions (e.g., removing unused imports).

For example, [`unnecessary-iterable-allocation-for-first-element`](https://docs.astral.sh/ruff/rules/unnecessary-iterable-allocation-for-first-element/)
( `RUF015`) is a rule which checks for potentially unperformant use of `list(...)[0]`. The fix
replaces this pattern with `next(iter(...))` which can result in a drastic speedup:

```
$ python -m timeit "head = list(range(99999999))[0]"
1 loop, best of 5: 1.69 sec per loop

```

```
$ python -m timeit "head = next(iter(range(99999999)))"
5000000 loops, best of 5: 70.8 nsec per loop

```

However, when the collection is empty, this raised exception changes from an `IndexError` to `StopIteration`:

```
$ python -c 'list(range(0))[0]'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
IndexError: list index out of range

```

```
$ python -c 'next(iter(range(0)))[0]'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
StopIteration

```

Since the change in exception type could break error handling upstream, this fix is categorized as unsafe.

Ruff only enables safe fixes by default. Unsafe fixes can be enabled by settings [`unsafe-fixes`](https://docs.astral.sh/ruff/settings/#unsafe-fixes) in your configuration file or passing the `--unsafe-fixes` flag to `ruff check`:

```
# Show unsafe fixes
ruff check --unsafe-fixes

# Apply unsafe fixes
ruff check --fix --unsafe-fixes

```

By default, Ruff will display a hint when unsafe fixes are available but not enabled. The suggestion can be silenced
by setting the [`unsafe-fixes`](https://docs.astral.sh/ruff/settings/#unsafe-fixes) setting to `false` or using the `--no-unsafe-fixes` flag.

The safety of fixes can be adjusted per rule using the [`lint.extend-safe-fixes`](https://docs.astral.sh/ruff/settings/#lint_extend-safe-fixes) and [`lint.extend-unsafe-fixes`](https://docs.astral.sh/ruff/settings/#lint_extend-unsafe-fixes) settings.

For example, the following configuration would promote unsafe fixes for `F601` to safe fixes and demote safe fixes for `UP034` to unsafe fixes:

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_4_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_4_2)

```
[tool.ruff.lint]
extend-safe-fixes = ["F601"]
extend-unsafe-fixes = ["UP034"]

```

```
[lint]
extend-safe-fixes = ["F601"]
extend-unsafe-fixes = ["UP034"]

```

You may use prefixes to select rules as well, e.g., `F` can be used to promote fixes for all rules in Pyflakes to safe.

Note

All fixes will always be displayed by Ruff when using the `json` output format. The safety of each fix is available under the `applicability` field.

### [Disabling fixes](https://docs.astral.sh/ruff/linter/\#disabling-fixes)

To limit the set of rules that Ruff should fix, use the [`lint.fixable`](https://docs.astral.sh/ruff/settings/#lint_fixable)
or [`lint.extend-fixable`](https://docs.astral.sh/ruff/settings/#lint_extend-fixable), and [`lint.unfixable`](https://docs.astral.sh/ruff/settings/#lint_unfixable) settings.

For example, the following configuration would enable fixes for all rules except
[`unused-imports`](https://docs.astral.sh/ruff/rules/unused-import/) ( `F401`):

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_5_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_5_2)

```
[tool.ruff.lint]
fixable = ["ALL"]
unfixable = ["F401"]

```

```
[lint]
fixable = ["ALL"]
unfixable = ["F401"]

```

Conversely, the following configuration would only enable fixes for `F401`:

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_6_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_6_2)

```
[tool.ruff.lint]
fixable = ["F401"]

```

```
[lint]
fixable = ["F401"]

```

## [Error suppression](https://docs.astral.sh/ruff/linter/\#error-suppression)

Ruff supports several mechanisms for suppressing lint errors, be they false positives or
permissible violations.

To omit a lint rule entirely, add it to the "ignore" list via the [`lint.ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore)
setting, either on the command-line or in your `pyproject.toml` or `ruff.toml` file.

To suppress a violation inline, Ruff uses a `noqa` system similar to [Flake8](https://flake8.pycqa.org/en/3.1.1/user/ignoring-errors.html).
To ignore an individual violation, add `# noqa: {code}` to the end of the line, like so:

```
# Ignore F841.
x = 1  # noqa: F841

# Ignore E741 and F841.
i = 1  # noqa: E741, F841

# Ignore _all_ violations.
x = 1  # noqa

```

For multi-line strings (like docstrings), the `noqa` directive should come at the end of the string
(after the closing triple quote), and will apply to the entire string, like so:

```
"""Lorem ipsum dolor sit amet.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
"""  # noqa: E501

```

For import sorting, the `noqa` should come at the end of the first line in the import block, and
will apply to all imports in the block, like so:

```
import os  # noqa: I001
import abc

```

To ignore all violations across an entire file, add the line `# ruff: noqa` anywhere in the file,
preferably towards the top, like so:

```
# ruff: noqa

```

To ignore a specific rule across an entire file, add the line `# ruff: noqa: {code}` anywhere in the
file, preferably towards the top, like so:

```
# ruff: noqa: F841

```

Or see the [`lint.per-file-ignores`](https://docs.astral.sh/ruff/settings/#lint_per-file-ignores) setting, which enables the same
functionality from within your `pyproject.toml` or `ruff.toml` file.

Global `noqa` comments must be on their own line to disambiguate from comments which ignore
violations on a single line.

Note that Ruff will also respect Flake8's `# flake8: noqa` directive, and will treat it as
equivalent to `# ruff: noqa`.

### [Full suppression comment specification](https://docs.astral.sh/ruff/linter/\#full-suppression-comment-specification)

The full specification is as follows:

- An inline blanket `noqa` comment is given by a case-insensitive match for
`#noqa` with optional whitespace after the `#` symbol, followed by either: the
end of the comment, the beginning of a new comment ( `#`), or whitespace
followed by any character other than `:`.
- An inline rule suppression is given by first finding a case-insensitive match
for `#noqa` with optional whitespace after the `#` symbol, optional whitespace
after `noqa`, and followed by the symbol `:`. After this we are expected to
have a list of rule codes which is given by sequences of uppercase ASCII
characters followed by ASCII digits, separated by whitespace or commas. The
list ends at the last valid code. We will attempt to interpret rules with a
missing delimiter (e.g. `F401F841`), though a warning will be emitted in this
case.
- A file-level exemption comment is given by a case-sensitive match for `#ruff:`
or `#flake8:`, with optional whitespace after `#` and before `:`, followed by
optional whitespace and a case-insensitive match for `noqa`. After this, the
specification is as in the inline case.

### [Detecting unused suppression comments](https://docs.astral.sh/ruff/linter/\#detecting-unused-suppression-comments)

Ruff implements a special rule, [`unused-noqa`](https://docs.astral.sh/ruff/rules/unused-noqa/),
under the `RUF100` code, to enforce that your `noqa` directives are "valid", in that the violations
they _say_ they ignore are actually being triggered on that line (and thus suppressed). To flag
unused `noqa` directives, run: `ruff check /path/to/file.py --extend-select RUF100`.

Ruff can also _remove_ any unused `noqa` directives via its fix functionality. To remove any
unused `noqa` directives, run: `ruff check /path/to/file.py --extend-select RUF100 --fix`.

### [Inserting necessary suppression comments](https://docs.astral.sh/ruff/linter/\#inserting-necessary-suppression-comments)

Ruff can _automatically add_ `noqa` directives to all lines that contain violations, which is
useful when migrating a new codebase to Ruff. To automatically add `noqa` directives to all
relevant lines (with the appropriate rule codes), run: `ruff check /path/to/file.py --add-noqa`.

### [Action comments](https://docs.astral.sh/ruff/linter/\#action-comments)

Ruff respects isort's [action comments](https://pycqa.github.io/isort/docs/configuration/action_comments.html)
( `# isort: skip_file`, `# isort: on`, `# isort: off`, `# isort: skip`, and `# isort: split`), which
enable selectively enabling and disabling import sorting for blocks of code and other inline
configuration.

Ruff will also respect variants of these action comments with a `# ruff:` prefix
(e.g., `# ruff: isort: skip_file`, `# ruff: isort: on`, and so on). These variants more clearly
convey that the action comment is intended for Ruff, but are functionally equivalent to the
isort variants.

Unlike isort, Ruff does not respect action comments within docstrings.

See the [isort documentation](https://pycqa.github.io/isort/docs/configuration/action_comments.html)
for more.

## [Exit codes](https://docs.astral.sh/ruff/linter/\#exit-codes)

By default, `ruff check` exits with the following status codes:

- `0` if no violations were found, or if all present violations were fixed automatically.
- `1` if violations were found.
- `2` if Ruff terminates abnormally due to invalid configuration, invalid CLI options, or an
internal error.

This convention mirrors that of tools like ESLint, Prettier, and RuboCop.

`ruff check` supports two command-line flags that alter its exit code behavior:

- `--exit-zero` will cause Ruff to exit with a status code of `0` even if violations were found.
Note that Ruff will still exit with a status code of `2` if it terminates abnormally.
- `--exit-non-zero-on-fix` will cause Ruff to exit with a status code of `1` if violations were
found, _even if_ all such violations were fixed automatically. Note that the use of
`--exit-non-zero-on-fix` can result in a non-zero exit code even if no violations remain after
fixing.
