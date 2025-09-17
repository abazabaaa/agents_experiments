---
title: Templates (Lark Advanced Example)
description: Example showing how to use Lark's templates to create cleaner grammars by parameterizing repeated patterns.
source_url: https://lark-parser.readthedocs.io/en/stable/examples/advanced/templates.html
---

# Templates

This example shows how to use Lark's templates to achieve cleaner grammars.

## Code

```python
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

Total running time of the script: 0 minutes 0.000 seconds

## Downloads

- Download Python source code: templates.py
  https://lark-parser.readthedocs.io/en/stable/_downloads/d3b43c711b7f9a6aeee99f79cf861539/templates.py

- Download Jupyter notebook: templates.ipynb
  https://lark-parser.readthedocs.io/en/stable/_downloads/6619e43bab1bed7430fa709940e67aa2/templates.ipynb
