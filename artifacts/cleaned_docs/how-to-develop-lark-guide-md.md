---
title: How to develop Lark - Guide
description: Contributor guide for the Lark parsing library, covering ways to help, code style, and how to run the test suite with Python, tox, and pytest.
source_url: https://lark-parser.readthedocs.io/en/stable/how_to_develop.html
---

# How to develop Lark - Guide

There are many ways you can help the project:

- Help solve issues
- Improve the documentation
- Write new grammars for Lark’s library
- Write a blog post introducing Lark to your audience
- Port Lark to another language
- Help with code development

If you’re interested in taking one of these on, contact us on Gitter (https://gitter.im/lark-parser/Lobby) or GitHub Discussion (https://github.com/lark-parser/lark/discussions), and we will provide more details and assist you in the process.

## Code Style

Lark does not follow a predefined code style. We accept any code style that makes sense, as long as it’s Pythonic and easy to read.

## Unit Tests

Lark comes with an extensive set of tests. Many of the tests will run several times, once for each parser configuration.

To run the tests, go to the Lark project root and run:

```sh
python -m tests
```

or

```sh
pypy -m tests
```

For a list of supported interpreters, consult the tox.ini file.

You can also run a single unittest using its class and method name, for example:

```sh
##   test_package test_class_name.test_function_name
python -m tests TestLalrBasic.test_keep_all_tokens
```

### tox

To run all unit tests with tox, install tox and Python 2.7 up to the latest Python interpreter supported (consult tox.ini). Then run the command tox at the project root (where the main setup.py file is).

For example, to only run the unit tests for Python 2.7:

```sh
tox -e py27
```

### pytest

You can also run the tests using pytest:

```sh
pytest tests
```

### Using setup.py

Another way to run the tests is using setup.py:

```sh
python setup.py test
```
