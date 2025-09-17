[Skip to content](https://docs.astral.sh/ty/reference/cli/#cli-reference)

# [CLI Reference](https://docs.astral.sh/ty/reference/cli/\#cli-reference)

## [ty](https://docs.astral.sh/ty/reference/cli/\#ty)

An extremely fast Python type checker.

### Usage

```
ty <COMMAND>

```

### Commands

[`ty check`](https://docs.astral.sh/ty/reference/cli/#ty-check)

Check a project for type errors

[`ty server`](https://docs.astral.sh/ty/reference/cli/#ty-server)

Start the language server

[`ty version`](https://docs.astral.sh/ty/reference/cli/#ty-version)

Display ty's version

[`ty help`](https://docs.astral.sh/ty/reference/cli/#ty-help)

Print this message or the help of the given subcommand(s)

## [ty check](https://docs.astral.sh/ty/reference/cli/\#ty-check)

Check a project for type errors

### Usage

```
ty check [OPTIONS] [PATH]...

```

### Arguments

[`PATHS`](https://docs.astral.sh/ty/reference/cli/#ty-check--paths)

List of files or directories to check \[default: the project root\]

### Options

[`--color`](https://docs.astral.sh/ty/reference/cli/#ty-check--color) _when_

Control when colored output is used

Possible values:

- `auto`: Display colors if the output goes to an interactive terminal
- `always`: Always display colors
- `never`: Never display colors

[`--config`](https://docs.astral.sh/ty/reference/cli/#ty-check--config), `-c` _config-option_

A TOML `<KEY> = <VALUE>` pair (such as you might find in a `ty.toml` configuration file)
overriding a specific configuration option.

Overrides of individual settings using this option always take precedence
over all configuration files.

[`--config-file`](https://docs.astral.sh/ty/reference/cli/#ty-check--config-file) _path_

The path to a `ty.toml` file to use for configuration.

While ty configuration can be included in a `pyproject.toml` file, it is not allowed in this context.

May also be set with the `TY_CONFIG_FILE` environment variable.

[`--error`](https://docs.astral.sh/ty/reference/cli/#ty-check--error) _rule_

Treat the given rule as having severity 'error'. Can be specified multiple times.

[`--error-on-warning`](https://docs.astral.sh/ty/reference/cli/#ty-check--error-on-warning)

Use exit code 1 if there are any warning-level diagnostics

[`--exclude`](https://docs.astral.sh/ty/reference/cli/#ty-check--exclude) _exclude_

Glob patterns for files to exclude from type checking.

Uses gitignore-style syntax to exclude files and directories from type checking. Supports patterns like `tests/`, `*.tmp`, `**/__pycache__/**`.

[`--exit-zero`](https://docs.astral.sh/ty/reference/cli/#ty-check--exit-zero)

Always use exit code 0, even when there are error-level diagnostics

[`--extra-search-path`](https://docs.astral.sh/ty/reference/cli/#ty-check--extra-search-path) _path_

Additional path to use as a module-resolution source (can be passed multiple times)

[`--help`](https://docs.astral.sh/ty/reference/cli/#ty-check--help), `-h`

Print help (see a summary with '-h')

[`--ignore`](https://docs.astral.sh/ty/reference/cli/#ty-check--ignore) _rule_

Disables the rule. Can be specified multiple times.

[`--output-format`](https://docs.astral.sh/ty/reference/cli/#ty-check--output-format) _output-format_

The format to use for printing diagnostic messages

Possible values:

- `full`: Print diagnostics verbosely, with context and helpful hints \[default\]
- `concise`: Print diagnostics concisely, one per line

[`--project`](https://docs.astral.sh/ty/reference/cli/#ty-check--project) _project_

Run the command within the given project directory.

All `pyproject.toml` files will be discovered by walking up the directory tree from the given project directory, as will the project's virtual environment ( `.venv`) unless the `venv-path` option is set.

Other command-line arguments (such as relative paths) will be resolved relative to the current working directory.

[`--python`](https://docs.astral.sh/ty/reference/cli/#ty-check--python) _path_

Path to the Python environment.

ty uses the Python environment to resolve type information and third-party dependencies.

If not specified, ty will attempt to infer it from the `VIRTUAL_ENV` or `CONDA_PREFIX` environment variables, or discover a `.venv` directory in the project root or working directory.

If a path to a Python interpreter is provided, e.g., `.venv/bin/python3`, ty will attempt to find an environment two directories up from the interpreter's path, e.g., `.venv`. At this time, ty does not invoke the interpreter to determine the location of the environment. This means that ty will not resolve dynamic executables such as a shim.

ty will search in the resolved environment's `site-packages` directories for type information and third-party imports.

[`--python-platform`](https://docs.astral.sh/ty/reference/cli/#ty-check--python-platform), `--platform` _platform_

Target platform to assume when resolving types.

This is used to specialize the type of `sys.platform` and will affect the visibility of platform-specific functions and attributes. If the value is set to `all`, no assumptions are made about the target platform. If unspecified, the current system's platform will be used.

[`--python-version`](https://docs.astral.sh/ty/reference/cli/#ty-check--python-version), `--target-version` _version_

Python version to assume when resolving types.

The Python version affects allowed syntax, type definitions of the standard library, and type definitions of first- and third-party modules that are conditional on the Python version.

If a version is not specified on the command line or in a configuration file, ty will try the following techniques in order of preference to determine a value: 1. Check for the `project.requires-python` setting in a `pyproject.toml` file and use the minimum version from the specified range 2. Check for an activated or configured Python environment and attempt to infer the Python version of that environment 3. Fall back to the latest stable Python version supported by ty (currently Python 3.13)

Possible values:

- `3.7`
- `3.8`
- `3.9`
- `3.10`
- `3.11`
- `3.12`
- `3.13`

[`--quiet`](https://docs.astral.sh/ty/reference/cli/#ty-check--quiet), `-q`

Use quiet output (or `-qq` for silent output)

[`--respect-ignore-files`](https://docs.astral.sh/ty/reference/cli/#ty-check--respect-ignore-files)

Respect file exclusions via `.gitignore` and other standard ignore files. Use `--no-respect-gitignore` to disable

[`--typeshed`](https://docs.astral.sh/ty/reference/cli/#ty-check--typeshed), `--custom-typeshed-dir` _path_

Custom directory to use for stdlib typeshed stubs

[`--verbose`](https://docs.astral.sh/ty/reference/cli/#ty-check--verbose), `-v`

Use verbose output (or `-vv` and `-vvv` for more verbose output)

[`--warn`](https://docs.astral.sh/ty/reference/cli/#ty-check--warn) _rule_

Treat the given rule as having severity 'warn'. Can be specified multiple times.

[`--watch`](https://docs.astral.sh/ty/reference/cli/#ty-check--watch), `-W`

Watch files for changes and recheck files related to the changed files

## [ty server](https://docs.astral.sh/ty/reference/cli/\#ty-server)

Start the language server

### Usage

```
ty server

```

### Options

[`--help`](https://docs.astral.sh/ty/reference/cli/#ty-server--help), `-h`

Print help

## [ty version](https://docs.astral.sh/ty/reference/cli/\#ty-version)

Display ty's version

### Usage

```
ty version

```

### Options

[`--help`](https://docs.astral.sh/ty/reference/cli/#ty-version--help), `-h`

Print help

## [ty generate-shell-completion](https://docs.astral.sh/ty/reference/cli/\#ty-generate-shell-completion)

Generate shell completion

### Usage

```
ty generate-shell-completion <SHELL>

```

### Arguments

[`SHELL`](https://docs.astral.sh/ty/reference/cli/#ty-generate-shell-completion--shell)

### Options

[`--help`](https://docs.astral.sh/ty/reference/cli/#ty-generate-shell-completion--help), `-h`

Print help

## [ty help](https://docs.astral.sh/ty/reference/cli/\#ty-help)

Print this message or the help of the given subcommand(s)

### Usage

```
ty help [COMMAND]

```
