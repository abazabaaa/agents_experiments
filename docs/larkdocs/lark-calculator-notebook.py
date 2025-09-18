'''Basic calculator

A simple example of a REPL calculator.
This example shows how to write a basic calculator with variables.

Converted from the original Jupyter notebook example into a standalone
Python script that demonstrates Lark parser functionality.
'''

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------
from lark import Lark, Transformer, v_args

# Python 2 compatibility for input()
try:
    input = raw_input  # type: ignore[name-defined]
except NameError:
    pass

# ------------------------------------------------------------
# Grammar Definition (kept exactly as in the notebook)
# Note: using a raw triple-quoted string preserves all grammar characters
# ------------------------------------------------------------
CALC_GRAMMAR = r'''
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
'''

# ------------------------------------------------------------
# Transformer
# - Keeps method names matching rule aliases (e.g., -> add, -> sub, etc.)
# - @v_args(inline=True) preserves the original call signatures
# ------------------------------------------------------------
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


# ------------------------------------------------------------
# Parser setup and convenience handle
# ------------------------------------------------------------
calc_parser = Lark(CALC_GRAMMAR, parser='lalr', transformer=CalculateTree())
calc = calc_parser.parse


# ------------------------------------------------------------
# REPL Entry Point
# ------------------------------------------------------------
def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))


# ------------------------------------------------------------
# Simple tests (preserved from the notebook)
# ------------------------------------------------------------
def test():
    print(calc("a = 1+2"))
    print(calc("1+a*-3"))


if __name__ == '__main__':
    # test()
    main()
