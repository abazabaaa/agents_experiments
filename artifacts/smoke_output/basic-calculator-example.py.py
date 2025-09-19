---
title: "Basic calculator"
description: "A simple REPL calculator example implemented with Lark (Python)."
source_url: "https://example.com/lark-examples/basic-calculator"
---

# Basic calculator

A simple example of a REPL calculator

This example shows how to write a basic calculator with variables.

Note: The script includes a Python 2 compatibility fallback for input (raw_input). See the code below for the explicit fallback.

```python
"""
Basic calculator
================

A simple example of a REPL calculator

This example shows how to write a basic calculator with variables.
"""
from lark import Lark, Transformer, v_args

try:
    input = raw_input   # For Python 2: raw_input fallback
except NameError:
    pass

calc_grammar = """
    ?start: sum
          | NAME "=" sum    -> assign_var

    ?sum: product
        | sum "+" product   -> add
        | sum "-" product   -> sub

    ?product: atom
        | product "*" atom  -> mul
        | product "/" atom  -> div

    ?atom: NUMBER           -> number
         | "-" atom         -> neg
         | NAME             -> var
         | "(" sum ")"

    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
"""

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float

    def __init__(self):
        self.vars = {}

    def assign_var(self, name, value):
        self.vars[name] = value
        return value

    def var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception("Variable not found: %s" % name)

calc_parser = Lark(calc_grammar, parser='lalr', transformer=CalculateTree())
calc = calc_parser.parse

def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))

def test():
    print(calc("a = 1+2"))
    print(calc("1+a*-3"))

if __name__ == '__main__':
    # test()
    main()
```

## Summary of changes

- Added YAML front-matter (title, description, source_url).
- Converted the document heading to a consistent Markdown H1.
- Kept the full Python example inside a ```python code block and preserved the grammar string exactly.
- Updated the Python 2 compatibility line comment to explicitly mention the raw_input fallback.
- Added a short note about the Python 2 fallback above the code example.
