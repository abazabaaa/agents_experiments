---
title: Lark Templates Example
description: Demonstrates using Lark's template feature to create cleaner grammars with a separated list/dict pattern.
source_url: https://lark-parser.readthedocs.io/en/stable/_downloads/d3b43c711b7f9a6aeee99f79cf861539/templates.py
---

# Templates

This example shows how to use Lark's templates to achieve cleaner grammars.

```python
from lark import Lark

grammar = r"""
start: list | dict

list: "[" _separated{atom, ","} "]"
dict: "{" _separated{key_value, ","} "}"
key_value: atom ":" atom

_separated{x, sep}: x (sep x)*  // Define a sequence of 'x sep x sep x ...'

atom: NUMBER | ESCAPED_STRING

%import common (NUMBER, ESCAPED_STRING, WS)
%ignore WS
"""

parser = Lark(grammar)

print(parser.parse('[1, "a", 2]'))
print(parser.parse('{"a": 2, "b": 6}'))
```
