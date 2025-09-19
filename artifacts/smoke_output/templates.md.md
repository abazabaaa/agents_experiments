---
title: "Templates"
description: "Example showing how to use Lark's templates to achieve cleaner grammars."
source_url: "N/A"
---

# Templates

This example shows how to use Lark's templates to achieve cleaner grammars.

The full, runnable Python example is shown below. The embedded grammar is kept as a raw string (r"""...""") so it can be used directly with Lark.

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

The grammar alone (exactly as embedded above) is provided here for quick reference:

```lark
start: list | dict

list: "[" _separated{atom, ","} "]"
dict: "{" _separated{key_value, ","} "}"
key_value: atom ":" atom

_separated{x, sep}: x (sep x)*  // Define a sequence of 'x sep x sep x ...'

atom: NUMBER | ESCAPED_STRING

%import common (NUMBER, ESCAPED_STRING, WS)
%ignore WS
```

Notes:
- Fixed a minor typo in the template name: `_seperated` -> `_separated` so the identifier is consistent.
- The grammar comments (// ...) and template syntax are preserved exactly. 
- Use the Python block above to run the example directly with Lark.
