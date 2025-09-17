---
title: How to Develop Lark - Guide
description: Contributing guide for the Lark parser project, including code style, running tests with unittest, tox, pytest, and setup.py.
source_url: https://lark-parser.readthedocs.io/en/stable/how_to_develop.html
---

# How to Develop Lark - Guide

There are many ways you can help the project:

- Help solve issues
- Improve the documentation
- Write new grammars for Lark’s library
- Write a blog post introducing Lark to your audience
- Port Lark to another language
- Help with code development

If you’re interested in taking one of these on, contact us on [Gitter](https://gitter.im/lark-parser/Lobby) or [GitHub Discussions](https://github.com/lark-parser/lark/discussions), and we will provide more details and assist you in the process.

## Code Style

Lark does not follow a predefined code style. We accept any code style that makes sense, as long as it’s Pythonic and easy to read.

## Unit Tests

Lark comes with an extensive set of tests. Many of the tests will run several times, once for each parser configuration.

To run the tests, go to the Lark project root and run:

```bash
python -m tests
```

or

```bash
pypy -m tests
```

For a list of supported interpreters, consult the `tox.ini` file.

You can also run a single unittest using its class and method name, for example:

```bash
# Syntax: python -m tests <TestClass>.<test_method>
python -m tests TestLalrBasic.test_keep_all_tokens
```

### tox

To run all unit tests with tox, install tox and all supported Python interpreters (see `tox.ini`). Then run:

```bash
tox
```

For example, to run tests only for Python 2.7:

```bash
tox -e py27
```

### pytest

You can also run the tests using pytest:

```bash
pytest tests
```

### Using setup.py

Another way to run the tests is using setup.py:

```bash
python setup.py test
```
