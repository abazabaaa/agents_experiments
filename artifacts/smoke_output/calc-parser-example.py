"""
# Basic calculator

A simple example of a REPL calculator

This example shows how to write a basic calculator with variables.

This script was converted from a Jupyter notebook. The original notebook
markdown and important comments have been preserved here in this module
level docstring. The code below is a cleaned, standalone Python 3 script
that demonstrates usage of Lark for a simple calculator grammar with
variables. Tests from the notebook are kept in the script but left
commented out (see the if __name__ == '__main__' block).
"""

# Imports
from lark import Lark, Transformer, v_args

# Grammar definition
# Note: Preserved exactly as in the notebook, kept in a triple-quoted raw string
calc_grammar = r'''
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

# Transformer class
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


# Create parser and helper function
calc_parser = Lark(calc_grammar, parser='lalr', transformer=CalculateTree())
calc = calc_parser.parse


# Main REPL
def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        try:
            print(calc(s))
        except Exception as e:
            print('Error:', e)


# Tests (kept from the notebook). They are left as a function and their
# invocation is commented out to match the notebook behavior.
def test():
    print(calc("a = 1+2"))
    print(calc("1+a*-3"))


if __name__ == '__main__':
    # test()
    main()
