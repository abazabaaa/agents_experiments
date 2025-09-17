---
title: Lark Templates Example (Python)
description: Demonstrates using Lark's templates to write cleaner grammars, including a parameterized _seperated template used within a list and dict grammar.
source_url: https://lark-parser.readthedocs.io/en/stable/_downloads/d3b43c711b7f9a6aeee99f79cf861539/templates.py
---

# Templates

This example shows how to use Lark's templates to achieve cleaner grammars.

## Python Example

```python
"""
Templates
=========

This example shows how to use Lark's templates to achieve cleaner grammars

"""
from lark import Lark

grammar = r"""
start: list | dict

list: "[" _seperated{atom, ","} "]"
dict: "{" _seperated{key_value, ","} "}"
key_value: atom ":" atom

_seperated{x, sep}: x (sep x)*  // Define a sequence of 'x sep x sep x ...'

atom: NUMBER | ESCAPED_STRING

%import common (NUMBER, ESCAPED_STRING, WS)
%ignore WS
"""

parser = Lark(grammar)

print(parser.parse('[1, "a", 2]'))
print(parser.parse('{"a": 2, "b": 6}'))
```
