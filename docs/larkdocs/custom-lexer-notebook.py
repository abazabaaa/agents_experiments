"""Custom lexer

Demonstrates using a custom lexer to parse a non-textual stream of data.

You can use a custom lexer to tokenize text when the lexers offered by Lark
are too slow, or not flexible enough.

You can also use it (as shown in this example) to tokenize streams of objects.

Converted from Jupyter notebook:
https://lark-parser.readthedocs.io/en/stable/_downloads/5811ce5e933efd9af1ae8e52d16a3a4f/custom_lexer.ipynb
"""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from lark import Lark, Transformer, v_args
from lark.lexer import Lexer, Token


# -----------------------------------------------------------------------------
# Custom lexer implementation
# -----------------------------------------------------------------------------
class TypeLexer(Lexer):
    def __init__(self, lexer_conf):
        # No configuration needed for this example
        pass

    def lex(self, data):
        # Tokenize a sequence of Python objects by their type
        for obj in data:
            if isinstance(obj, int):
                yield Token('INT', obj)
            elif isinstance(obj, (type(''), type(u''))):
                yield Token('STR', obj)
            else:
                raise TypeError(obj)


# -----------------------------------------------------------------------------
# Lark grammar (kept exactly as in the notebook)
# -----------------------------------------------------------------------------
GRAMMAR = r'''
        start: data_item+
        data_item: STR INT*

        %declare STR INT
        '''


# -----------------------------------------------------------------------------
# Build the parser with the custom lexer
# -----------------------------------------------------------------------------
parser = Lark(GRAMMAR, parser='lalr', lexer=TypeLexer)


# -----------------------------------------------------------------------------
# Transformer to convert parse tree to a Python dict
# -----------------------------------------------------------------------------
class ParseToDict(Transformer):
    @v_args(inline=True)
    def data_item(self, name, *numbers):
        return name.value, [n.value for n in numbers]

    start = dict


# -----------------------------------------------------------------------------
# Test/demo
# -----------------------------------------------------------------------------
def test():
    # Example input stream mixing strings and integers
    data = ['alice', 1, 27, 3, 'bob', 4, 'carrie', 'dan', 8, 6]

    print(data)

    tree = parser.parse(data)
    res = ParseToDict().transform(tree)

    print('-->')
    print(res)  # prints {'alice': [1, 27, 3], 'bob': [4], 'carrie': [], 'dan': [8, 6]}


if __name__ == '__main__':
    test()
