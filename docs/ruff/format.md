[Skip to content](https://docs.astral.sh/ruff/formatter/#the-ruff-formatter)

# [The Ruff Formatter](https://docs.astral.sh/ruff/formatter/\#the-ruff-formatter)

The Ruff formatter is an extremely fast Python code formatter designed as a drop-in replacement for
[Black](https://pypi.org/project/black/), available as part of the `ruff` CLI via `ruff format`.

## [`ruff format`](https://docs.astral.sh/ruff/formatter/\#ruff-format)

`ruff format` is the primary entrypoint to the formatter. It accepts a list of files or
directories, and formats all discovered Python files:

```
ruff format                   # Format all files in the current directory.
ruff format path/to/code/     # Format all files in `path/to/code` (and any subdirectories).
ruff format path/to/file.py   # Format a single file.

```

Similar to Black, running `ruff format /path/to/file.py` will format the given file or directory
in-place, while `ruff format --check /path/to/file.py` will avoid writing any formatted files back,
and instead exit with a non-zero status code upon detecting any unformatted files.

For the full list of supported options, run `ruff format --help`.

## [Philosophy](https://docs.astral.sh/ruff/formatter/\#philosophy)

The initial goal of the Ruff formatter is _not_ to innovate on code style, but rather, to innovate
on performance, and provide a unified toolchain across Ruff's linter, formatter, and any and all
future tools.

As such, the formatter is designed as a drop-in replacement for [Black](https://github.com/psf/black),
but with an excessive focus on performance and direct integration with Ruff. Given Black's
popularity within the Python ecosystem, targeting Black compatibility ensures that formatter
adoption is minimally disruptive for the vast majority of projects.

Specifically, the formatter is intended to emit near-identical output when run over existing
Black-formatted code. When run over extensive Black-formatted projects like Django and Zulip, > 99.9%
of lines are formatted identically. (See: [_Style Guide_](https://docs.astral.sh/ruff/formatter/#style-guide).)

Given this focus on Black compatibility, the formatter thus adheres to [Black's (stable) code style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html),
which aims for "consistency, generality, readability and reducing git diffs". To give you a sense
for the enforced code style, here's an example:

```
# Input
def _make_ssl_transport(
    rawsock, protocol, sslcontext, waiter=None,
    *, server_side=False, server_hostname=None,
    extra=None, server=None,
    ssl_handshake_timeout=None,
    call_connection_made=True):
    '''Make an SSL transport.'''
    if waiter is None:
      waiter = Future(loop=loop)

    if extra is None:
      extra = {}

    ...

# Ruff
def _make_ssl_transport(
    rawsock,
    protocol,
    sslcontext,
    waiter=None,
    *,
    server_side=False,
    server_hostname=None,
    extra=None,
    server=None,
    ssl_handshake_timeout=None,
    call_connection_made=True,
):
    """Make an SSL transport."""
    if waiter is None:
        waiter = Future(loop=loop)

    if extra is None:
        extra = {}

    ...

```

Like Black, the Ruff formatter does _not_ support extensive code style configuration; however,
unlike Black, it _does_ support configuring the desired quote style, indent style, line endings,
and more. (See: [_Configuration_](https://docs.astral.sh/ruff/formatter/#configuration).)

While the formatter is designed to be a drop-in replacement for Black, it is not intended to be
used interchangeably with Black on an ongoing basis, as the formatter _does_ differ from
Black in a few conscious ways (see: [_Known deviations_](https://docs.astral.sh/ruff/formatter/black/)). In general,
deviations are limited to cases in which Ruff's behavior was deemed more consistent, or
significantly simpler to support (with negligible end-user impact) given the differences in the
underlying implementations between Black and Ruff.

Going forward, the Ruff Formatter will support Black's preview style under Ruff's own
[preview](https://docs.astral.sh/ruff/preview/) mode.

## [Configuration](https://docs.astral.sh/ruff/formatter/\#configuration)

The Ruff Formatter exposes a small set of configuration options, some of which are also supported
by Black (like line width), some of which are unique to Ruff (like quote, indentation style and
formatting code examples in docstrings).

For example, to configure the formatter to use single quotes, format code
examples in docstrings, a line width of 100, and tab indentation, add the
following to your configuration file:

[pyproject.toml](https://docs.astral.sh/ruff/formatter/#__tabbed_1_1)[ruff.toml](https://docs.astral.sh/ruff/formatter/#__tabbed_1_2)

```
[tool.ruff]
line-length = 100

[tool.ruff.format]
quote-style = "single"
indent-style = "tab"
docstring-code-format = true

```

```
line-length = 100

[format]
quote-style = "single"
indent-style = "tab"
docstring-code-format = true

```

For the full list of supported settings, see [_Settings_](https://docs.astral.sh/ruff/settings/#format). For more on
configuring Ruff via `pyproject.toml`, see [_Configuring Ruff_](https://docs.astral.sh/ruff/configuration/).

Given the focus on Black compatibility (and unlike formatters like [YAPF](https://github.com/google/yapf)),
Ruff does not currently expose any other configuration options.

## [Docstring formatting](https://docs.astral.sh/ruff/formatter/\#docstring-formatting)

The Ruff formatter provides an opt-in feature for automatically formatting
Python code examples in docstrings. The Ruff formatter currently recognizes
code examples in the following formats:

- The Python [doctest](https://docs.python.org/3/library/doctest.html) format.
- CommonMark [fenced code blocks](https://spec.commonmark.org/0.30/#fenced-code-blocks) with the following info strings: `python`,
`py`, `python3`, or `py3`. Fenced code blocks without an info string are
assumed to be Python code examples and also formatted.
- reStructuredText [literal blocks](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks). While literal blocks may contain things
other than Python, this is meant to reflect a long-standing convention in the
Python ecosystem where literal blocks often contain Python code.
- reStructuredText \[ `code-block` and `sourcecode` directives\]. As with
Markdown, the language names recognized for Python are `python`, `py`,
`python3`, or `py3`.

If a code example is recognized and treated as Python, the Ruff formatter will
automatically skip it if the code does not parse as valid Python or if the
reformatted code would produce an invalid Python program.

Users may also configure the line length limit used for reformatting Python
code examples in docstrings. The default is a special value, `dynamic`, which
instructs the formatter to respect the line length limit setting for the
surrounding Python code. The `dynamic` setting ensures that even when code
examples are found inside indented docstrings, the line length limit configured
for the surrounding Python code will not be exceeded. Users may also configure
a fixed line length limit for code examples in docstrings.

For example, this configuration shows how to enable docstring code formatting
with a fixed line length limit:

[pyproject.toml](https://docs.astral.sh/ruff/formatter/#__tabbed_2_1)[ruff.toml](https://docs.astral.sh/ruff/formatter/#__tabbed_2_2)

```
[tool.ruff.format]
docstring-code-format = true
docstring-code-line-length = 20

```

```
[format]
docstring-code-format = true
docstring-code-line-length = 20

```

With the above configuration, this code:

```
def f(x):
    '''
    Something about `f`. And an example:

    .. code-block:: python

        foo, bar, quux = this_is_a_long_line(lion, hippo, lemur, bear)
    '''
    pass

```

... will be reformatted (assuming the rest of the options are set
to their defaults) as:

```
def f(x):
    """
    Something about `f`. And an example:

    .. code-block:: python

        (
            foo,
            bar,
            quux,
        ) = this_is_a_long_line(
            lion,
            hippo,
            lemur,
            bear,
        )
    """
    pass

```

## [Format suppression](https://docs.astral.sh/ruff/formatter/\#format-suppression)

Like Black, Ruff supports `# fmt: on`, `# fmt: off`, and `# fmt: skip` pragma comments, which can
be used to temporarily disable formatting for a given code block.

`# fmt: on` and `# fmt: off` comments are enforced at the statement level:

```
# fmt: off
not_formatted=3
also_not_formatted=4
# fmt: on

```

As such, adding `# fmt: on` and `# fmt: off` comments within expressions will have no effect. In
the following example, both list entries will be formatted, despite the `# fmt: off`:

```
[\
    # fmt: off\
    '1',\
    # fmt: on\
    '2',\
]

```

Instead, apply the `# fmt: off` comment to the entire statement:

```
# fmt: off
[\
    '1',\
    '2',\
]
# fmt: on

```

Like Black, Ruff will _also_ recognize [YAPF](https://github.com/google/yapf)'s `# yapf: disable` and `# yapf: enable` pragma
comments, which are treated equivalently to `# fmt: off` and `# fmt: on`, respectively.

`# fmt: skip` comments suppress formatting for a preceding statement, case header, decorator,
function definition, or class definition:

```
if True:
    pass
elif False: # fmt: skip
    pass

@Test
@Test2 # fmt: skip
def test(): ...

a = [1, 2, 3, 4, 5] # fmt: skip

def test(a, b, c, d, e, f) -> int: # fmt: skip
    pass

```

As such, adding an `# fmt: skip` comment at the end of an expression will have no effect. In
the following example, the list entry `'1'` will be formatted, despite the `# fmt: skip`:

```
a = call(
    [\
        '1',  # fmt: skip\
        '2',\
    ],
    b
)

```

Instead, apply the `# fmt: skip` comment to the entire statement:

```
a = call(
  [\
    '1',\
    '2',\
  ],
  b
)  # fmt: skip

```

## [Conflicting lint rules](https://docs.astral.sh/ruff/formatter/\#conflicting-lint-rules)

Ruff's formatter is designed to be used alongside the linter. However, the linter includes
some rules that, when enabled, can cause conflicts with the formatter, leading to unexpected
behavior. When configured appropriately, the goal of Ruff's formatter-linter compatibility is
such that running the formatter should never introduce new lint errors.

When using Ruff as a formatter, we recommend avoiding the following lint rules:

- [`tab-indentation`](https://docs.astral.sh/ruff/rules/tab-indentation/) ( `W191`)
- [`indentation-with-invalid-multiple`](https://docs.astral.sh/ruff/rules/indentation-with-invalid-multiple/) ( `E111`)
- [`indentation-with-invalid-multiple-comment`](https://docs.astral.sh/ruff/rules/indentation-with-invalid-multiple-comment/) ( `E114`)
- [`over-indented`](https://docs.astral.sh/ruff/rules/over-indented/) ( `E117`)
- [`docstring-tab-indentation`](https://docs.astral.sh/ruff/rules/docstring-tab-indentation/) ( `D206`)
- [`triple-single-quotes`](https://docs.astral.sh/ruff/rules/triple-single-quotes/) ( `D300`)
- [`bad-quotes-inline-string`](https://docs.astral.sh/ruff/rules/bad-quotes-inline-string/) ( `Q000`)
- [`bad-quotes-multiline-string`](https://docs.astral.sh/ruff/rules/bad-quotes-multiline-string/) ( `Q001`)
- [`bad-quotes-docstring`](https://docs.astral.sh/ruff/rules/bad-quotes-docstring/) ( `Q002`)
- [`avoidable-escaped-quote`](https://docs.astral.sh/ruff/rules/avoidable-escaped-quote/) ( `Q003`)
- [`missing-trailing-comma`](https://docs.astral.sh/ruff/rules/missing-trailing-comma/) ( `COM812`)
- [`prohibited-trailing-comma`](https://docs.astral.sh/ruff/rules/prohibited-trailing-comma/) ( `COM819`)
- [`multi-line-implicit-string-concatenation`](https://docs.astral.sh/ruff/rules/multi-line-implicit-string-concatenation/) ( `ISC002`) if used without `ISC001` and `flake8-implicit-str-concat.allow-multiline = false`

While the [`line-too-long`](https://docs.astral.sh/ruff/rules/line-too-long/) ( `E501`) rule _can_ be used alongside the
formatter, the formatter only makes a best-effort attempt to wrap lines at the configured
[`line-length`](https://docs.astral.sh/ruff/settings/#line-length). As such, formatted code _may_ exceed the line length,
leading to [`line-too-long`](https://docs.astral.sh/ruff/rules/line-too-long/) ( `E501`) errors.

None of the above are included in Ruff's default configuration. However, if you've enabled
any of these rules or their parent categories (like `Q`), we recommend disabling them via the
linter's [`lint.ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore) setting.

Similarly, we recommend avoiding the following isort settings, which are incompatible with the
formatter's treatment of import statements when set to non-default values:

- [`force-single-line`](https://docs.astral.sh/ruff/settings/#lint_isort_force-single-line)
- [`force-wrap-aliases`](https://docs.astral.sh/ruff/settings/#lint_isort_force-wrap-aliases)
- [`lines-after-imports`](https://docs.astral.sh/ruff/settings/#lint_isort_lines-after-imports)
- [`lines-between-types`](https://docs.astral.sh/ruff/settings/#lint_isort_lines-between-types)
- [`split-on-trailing-comma`](https://docs.astral.sh/ruff/settings/#lint_isort_split-on-trailing-comma)

If you've configured any of these settings to take on non-default values, we recommend removing
them from your Ruff configuration.

When an incompatible lint rule or setting is enabled, `ruff format` will emit a warning. If your
`ruff format` is free of warnings, you're good to go!

## [Exit codes](https://docs.astral.sh/ruff/formatter/\#exit-codes)

`ruff format` exits with the following status codes:

- `0` if Ruff terminates successfully, regardless of whether any files were formatted.
- `2` if Ruff terminates abnormally due to invalid configuration, invalid CLI options, or an
internal error.

Meanwhile, `ruff format --check` exits with the following status codes:

- `0` if Ruff terminates successfully, and no files would be formatted if `--check` were not
specified.
- `1` if Ruff terminates successfully, and one or more files would be formatted if `--check` were
not specified.
- `2` if Ruff terminates abnormally due to invalid configuration, invalid CLI options, or an
internal error.

## [Style Guide](https://docs.astral.sh/ruff/formatter/\#style-guide)

The formatter is designed to be a drop-in replacement for [Black](https://github.com/psf/black).
This section documents the areas where the Ruff formatter goes beyond Black in terms of code style.

### [Intentional deviations](https://docs.astral.sh/ruff/formatter/\#intentional-deviations)

While the Ruff formatter aims to be a drop-in replacement for Black, it does differ from Black
in a few known ways. Some of these differences emerge from conscious attempts to improve upon
Black's code style, while others fall out of differences in the underlying implementations.

For a complete enumeration of these intentional deviations, see [_Known deviations_](https://docs.astral.sh/ruff/formatter/black/).

Unintentional deviations from Black are tracked in the [issue tracker](https://github.com/astral-sh/ruff/issues?q=is%3Aopen+is%3Aissue+label%3Aformatter).
If you've identified a new deviation, please [file an issue](https://github.com/astral-sh/ruff/issues/new).

### [Preview style](https://docs.astral.sh/ruff/formatter/\#preview-style)

Similar to [Black](https://black.readthedocs.io/en/stable/the_black_code_style/future_style.html#preview-style), Ruff implements formatting changes
under the [`preview`](https://docs.astral.sh/ruff/settings/#format_preview) flag, promoting them to stable through minor releases, in accordance with our [versioning policy](https://github.com/astral-sh/ruff/discussions/6998#discussioncomment-7016766).

### [F-string formatting](https://docs.astral.sh/ruff/formatter/\#f-string-formatting)

_Stabilized in Ruff 0.9.0_

Unlike Black, Ruff formats the expression parts of f-strings which are the parts inside the curly
braces `{...}`. This is a [known deviation](https://docs.astral.sh/ruff/formatter/black/#f-strings) from Black.

Ruff employs several heuristics to determine how an f-string should be formatted which are detailed
below.

#### [Quotes](https://docs.astral.sh/ruff/formatter/\#quotes)

Ruff will use the [configured quote style](https://docs.astral.sh/ruff/settings/#format_quote-style) for the f-string expression unless doing so would result in
invalid syntax for the target Python version or requires more backslash escapes than the original
expression. Specifically, Ruff will preserve the original quote style for the following cases:

When the target Python version is < 3.12 and a [self-documenting f-string](https://realpython.com/python-f-strings/#self-documenting-expressions-for-debugging) contains a string
literal with the [configured quote style](https://docs.astral.sh/ruff/settings/#format_quote-style):

```
# format.quote-style = "double"

f'{10 + len("hello")=}'
# This f-string cannot be formatted as follows when targeting Python < 3.12
f"{10 + len("hello")=}"

```

When the target Python version is < 3.12 and an f-string contains any triple-quoted string, byte
or f-string literal that contains the [configured quote style](https://docs.astral.sh/ruff/settings/#format_quote-style):

```
# format.quote-style = "double"

f'{"""nested " """}'
# This f-string cannot be formatted as follows when targeting Python < 3.12
f"{'''nested " '''}"

```

For all target Python versions, when a [self-documenting f-string](https://realpython.com/python-f-strings/#self-documenting-expressions-for-debugging) contains an expression between
the curly braces ( `{...}`) with a format specifier containing the [configured quote style](https://docs.astral.sh/ruff/settings/#format_quote-style):

```
# format.quote-style = "double"

f'{1=:"foo}'
# This f-string cannot be formatted as follows for all target Python versions
f"{1=:"foo}"

```

For nested f-strings, Ruff alternates quote styles, starting with the [configured quote style](https://docs.astral.sh/ruff/settings/#format_quote-style) for the
outermost f-string. For example, consider the following f-string:

```
# format.quote-style = "double"

f"outer f-string {f"nested f-string {f"another nested f-string"} end"} end"

```

Ruff formats it as:

```
f"outer f-string {f'nested f-string {f"another nested f-string"} end'} end"

```

#### [Line breaks](https://docs.astral.sh/ruff/formatter/\#line-breaks)

Starting with Python 3.12 ( [PEP 701](https://peps.python.org/pep-0701/)), the expression parts of an f-string can
span multiple lines. Ruff needs to decide when to introduce a line break in an f-string expression.
This depends on the semantic content of the expression parts of an f-string - for example,
introducing a line break in the middle of a natural-language sentence is undesirable. Since Ruff
doesn't have enough information to make that decision, it adopts a heuristic similar to [Prettier](https://prettier.io/docs/en/next/rationale.html#template-literals):
it will only split the expression parts of an f-string across multiple lines if there was already a line break
within any of the expression parts.

For example, the following code:

```
f"this f-string has a multiline expression {
  ['red', 'green', 'blue', 'yellow',]} and does not fit within the line length"

```

... is formatted as:

```
# The list expression is split across multiple lines because of the trailing comma
f"this f-string has a multiline expression {
    [\
        'red',\
        'green',\
        'blue',\
        'yellow',\
    ]
} and does not fit within the line length"

```

But, the following will not be split across multiple lines even though it exceeds the line length:

```
f"this f-string has a multiline expression {['red', 'green', 'blue', 'yellow']} and does not fit within the line length"

```

If you want Ruff to split an f-string across multiple lines, ensure there's a linebreak somewhere within the
`{...}` parts of an f-string.

## [Sorting imports](https://docs.astral.sh/ruff/formatter/\#sorting-imports)

Currently, the Ruff formatter does not sort imports. In order to both sort imports and format,
call the Ruff linter and then the formatter:

```
ruff check --select I --fix
ruff format

```

A unified command for both linting and formatting is [planned](https://github.com/astral-sh/ruff/issues/8232).
