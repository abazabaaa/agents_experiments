[Skip to content](https://docs.astral.sh/ty/modules/#module-discovery)

# [Module discovery](https://docs.astral.sh/ty/modules/\#module-discovery)

## [First-party modules](https://docs.astral.sh/ty/modules/\#first-party-modules)

First-party modules are Python files that are part of your project source code.

By default, ty searches for first-party modules in the project's root directory or the `src`
directory, if present.

If your project uses a different layout, configure the project's
[`environment.root`](https://docs.astral.sh/ty/reference/configuration/#root) in your `pyproject.toml` or `ty.toml`. For example,
if your project's code is in an `app/` directory:

```
example-pkg
├── README.md
├── pyproject.toml
└── app
    └── example_pkg
        └── __init__.py

```

then set [`environment.root`](https://docs.astral.sh/ty/reference/configuration/#root) in your `pyproject.toml` to `["./app"]`:

```
[tool.ty.environment]
root = ["./app"]

```

## [Third-party modules](https://docs.astral.sh/ty/modules/\#third-party-modules)

Third-party modules are Python packages that are not part of your project or the standard library.
These are usually declared as dependencies in a `pyproject.toml` or `requirements.txt` file
and installed using a package manager like uv or pip. Examples of popular third-party
modules are `requests`, `numpy` and `django`.

ty searches for third-party modules in the configured [Python environment](https://docs.astral.sh/ty/modules/#python-environment).

## [Python environment](https://docs.astral.sh/ty/modules/\#python-environment)

The Python environment is used for discovery of third-party modules.

By default, ty will attempt to discover a virtual environment.

First, ty checks for an active virtual environment using the `VIRTUAL_ENV` environment variable. If
not set, ty will search for a `.venv` directory in the project root or working directory. ty only
supports discovery of virtual environments at this time.

Note

When using project management tools, such as uv or Poetry, the `run` command usually automatically
activates the virtual environment and will be detected by ty.

The Python environment may be explicitly configured using the
[`environment.python`](https://docs.astral.sh/ty/reference/configuration/#python) setting or
[`--python`](https://docs.astral.sh/ty/reference/cli/#ty-check--python) flag.

When setting the environment explicitly, non-virtual environments can be provided.
