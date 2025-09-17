---
title: Lark Standalone Parser (JSON) Example
description: Demonstrates generating and using a standalone parser with Lark's standalone mode, using the JSON example with a simple Transformer and CLI usage.
source_url: https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html
---

# Standalone Parser

This example demonstrates how to generate and use the standalone parser, using the JSON example.

See README.md for more details.

## Python example

```python
import sys

from json_parser import Lark_StandAlone, Transformer, v_args

inline_args = v_args(inline=True)

class TreeToJson(Transformer):
    @inline_args
    def string(self, s):
        return s[1:-1].replace('\"', '"')

    array = list
    pair = tuple
    object = dict
    number = inline_args(float)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

parser = Lark_StandAlone(transformer=TreeToJson())

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        print(parser.parse(f.read()))
```

## Downloads

- Download Python source code: json_parser_main.py
  - https://lark-parser.readthedocs.io/en/stable/_downloads/55c526745700131cb7096e508b392be7/json_parser_main.py
- Download Jupyter notebook: json_parser_main.ipynb
  - https://lark-parser.readthedocs.io/en/stable/_downloads/222c07e0396620c7fabb1da7fda69ca9/json_parser_main.ipynb

## Runtime

Total running time of the script: 0 minutes 0.000 seconds

## See also

- Previous: Standalone example
  - https://lark-parser.readthedocs.io/en/stable/examples/standalone/index.html
- Next: Grammar Reference
  - https://lark-parser.readthedocs.io/en/stable/grammar.html
- Edit on GitHub
  - https://github.com/lark-parser/lark/blob/acfe33d943a1310f3ca26145eb2896bc5c4955c9/docs/examples/standalone/json_parser_main.rst
