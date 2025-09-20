"""
Custom lexer
============

Demonstrates using a custom lexer to parse a non-textual stream of data

You can use a custom lexer to tokenize text when the lexers offered by Lark
are too slow, or not flexible enough.

You can also use it (as shown in this example) to tokenize streams of objects.
"""

# Standard imports first
from lark import Lark, Transformer, v_args
from lark.lexer import Lexer, Token

# Grammar definitions as constants
GRAMMAR = r'''
        start: data_item+
        data_item: STR INT*

        %declare STR INT
        '''

# Transformer classes
@v_args(inline=True)
class ParseToDict(Transformer):
    def data_item(self, name, *numbers):
        return name.value, [n.value for n in numbers]

    start = dict

# Custom lexer implementation
class TypeLexer(Lexer):
    def __init__(self, lexer_conf):
        # lexer_conf is provided by Lark but not used in this simple example
        pass

    def lex(self, data):
        for obj in data:
            if isinstance(obj, int):
                yield Token('INT', obj)
            elif isinstance(obj, (type(''), type(u''))):
                yield Token('STR', obj)
            else:
                raise TypeError(obj)

# Main parser setup
parser = Lark(GRAMMAR, parser='lalr', lexer=TypeLexer)

# Main execution
def test():
    data = ['alice', 1, 27, 3, 'bob', 4, 'carrie', 'dan', 8, 6]

    print(data)

    tree = parser.parse(data)
    res = ParseToDict().transform(tree)

    print('-->')
    print(res) # prints {'alice': [1, 27, 3], 'bob': [4], 'carrie': [], 'dan': [8, 6]}

if __name__ == '__main__':
    test()
