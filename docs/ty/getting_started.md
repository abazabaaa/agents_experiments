[Skip to content](https://docs.astral.sh/ty/#ty)

# [ty](https://docs.astral.sh/ty/\#ty)

An extremely fast Python type checker, written in Rust.

## [Getting started](https://docs.astral.sh/ty/\#getting-started)

Try out the [online playground](https://play.ty.dev/), or run ty with
[uvx](https://docs.astral.sh/uv/guides/tools/#running-tools) to get started quickly:

```
uvx ty

```

For other ways to install ty, see the [installation](https://docs.astral.sh/ty/installation/) documentation.

If you do not provide a subcommand, ty will list available commands — for detailed information about
command-line options, see the [CLI reference](https://docs.astral.sh/ty/reference/cli/).

Use the `check` command to run the type checker:

```
uvx ty check

```

ty will run on all Python files in the working directory and or subdirectories. If used from a
project, ty will run on all Python files in the project (starting in the directory with the
`pyproject.toml`)

You can also provide specific paths to check:

```
uvx ty check example.py

```

When type checking, ty will find installed packages in the active virtual environment (via
`VIRTUAL_ENV`) or discover a virtual environment named `.venv` in the project root or working
directory. It will not find packages in non-virtual environments without specifying the target path
with `--python`. See the [module discovery](https://docs.astral.sh/ty/modules/) documentation for
details.

### [Usage](https://docs.astral.sh/ty/\#usage)

Run [`ty check`](https://docs.astral.sh/ty/reference/cli/#ty-check), in your project's top-level directory,
to check the project for type errors using ty's default configuration.

If this provokes a cascade of errors, and you are using the standard library `venv` module
to provide your virtual environment, add the venv directory to your `.gitignore`
or `.ignore` file and then retry.
