---
title: Custom lexer
description: Demonstrates using a custom lexer to parse a non-textual stream of data with Lark. Includes a cleaned, Python 3–compatible example.
source_url: https://lark-parser.readthedocs.io/en/latest/examples/custom_lexer.html
---

# Custom lexer

Demonstrates using a custom lexer to parse a non-textual stream of data.

You can use a custom lexer to tokenize text when the lexers offered by Lark
are too slow, or not flexible enough.

You can also use it (as shown in this example) to tokenize streams of objects.

## Example (Python)

```python
from lark import Lark, Transformer, v_args
from lark.lexer import Lexer, Token

class TypeLexer(Lexer):
    def __init__(self, lexer_conf: object) -> None:
        super().__init__(lexer_conf)
        self.lexer_conf = lexer_conf

    def lex(self, data):
        for obj in data:
            if isinstance(obj, int):
                yield Token('INT', obj)
            elif isinstance(obj, str):
                yield Token('STR', obj)
            else:
                raise TypeError(obj)

parser = Lark("""
        start: data_item+
        data_item: STR INT*

        %declare STR INT
        """, parser='lalr', lexer=TypeLexer)

class ParseToDict(Transformer):
    @v_args(inline=True)
    def data_item(self, name, *numbers):
        return name.value, [n.value for n in numbers]

    start = dict

def test():
    data = ['alice', 1, 27, 3, 'bob', 4, 'carrie', 'dan', 8, 6]

    print(data)

    tree = parser.parse(data)
    res = ParseToDict().transform(tree)

    print('-->')
    print(res) # prints {'alice': [1, 27, 3], 'bob': [4], 'carrie': [], 'dan': [8, 6]}

if __name__ == '__main__':
    test()
```

## Grammar (Lark)

The grammar used by the example parser (preserved exactly):

```lark
        start: data_item+
        data_item: STR INT*

        %declare STR INT
```

## Notes

- Fixed Python 3 compatibility by replacing the old unicode/type(u'') check with isinstance(obj, str).
- Annotated TypeLexer.__init__ with a proper signature and ensured the base class initializer is called.
- The Lark grammar inside the Python string literal is preserved exactly as in the original example.

Summary: Cleaned and formatted the example for inclusion in markdown docs, removed extraneous blank lines, updated the lexer for Python 3, and added brief front-matter and a separate grammar block for clarity.
