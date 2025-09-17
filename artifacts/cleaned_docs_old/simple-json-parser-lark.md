---
title: Simple JSON Parser (Lark)
description: A concise, fast JSON parser implemented with Lark, using an LALR grammar and a Transformer to produce Python data structures.
source_url: https://lark-parser.readthedocs.io/en/stable/_downloads/6d1927842b20958cbf08c916e786d2d0/_json_parser.py
---

# Simple JSON Parser

The code below implements a short and clear JSON parser using Lark. It outperforms many other Python-written parsers. For an explanation, see the JSON parser tutorial at /docs/json_tutorial.md.

```python
from lark import Lark, Transformer, v_args

json_grammar = r"""
    ?start: value

    ?value: object
          | array
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    array  : "[" [value ("," value)*] "]"
    object : "{" [pair ("," pair)*] "}"
    pair   : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS

    %ignore WS
"""

class TreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[1:-1].replace('\"', '"')

    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

# Create the JSON parser with Lark, using the LALR algorithm
json_parser = Lark(
    json_grammar,
    parser='lalr',
    # Using the basic lexer isn't required, and isn't usually recommended.
    # But it's good enough for JSON, and it's slightly faster.
    lexer='basic',
    # Disabling propagate_positions and placeholders slightly improves speed
    propagate_positions=False,
    maybe_placeholders=False,
    # Using an internal transformer is faster and more memory efficient
    transformer=TreeToJson()
)
```
