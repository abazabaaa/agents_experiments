---
title: Lark Example — Basic Calculator
description: A simple REPL calculator using Lark with variables and basic arithmetic operations.
source_url: https://lark-parser.readthedocs.io/en/stable/examples/calc.html
---

# Basic calculator

A simple example of a REPL calculator with variables.

## Example code

```python
from lark import Lark, Transformer, v_args

try:
    input = raw_input   # For Python2 compatibility
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

## Downloads

- Download Python source code: calc.py — https://lark-parser.readthedocs.io/en/stable/_downloads/50b59008a60a728670b293084a6fe042/calc.py
- Download Jupyter notebook: calc.ipynb — https://lark-parser.readthedocs.io/en/stable/_downloads/63680f346bf793a45964b4e687bde3d9/calc.ipynb
