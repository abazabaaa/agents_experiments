"""Earley’s dynamic lexer example

Demonstrates Earley’s dynamic lexer on a toy configuration language.

Using a dynamic lexer and letting the Earley parser resolve lexing ambiguity.
"""

from lark import Lark, Transformer, v_args

CONF_GRAMMAR = r'''
        start: _NL? section+
        section: "[" NAME "]" _NL item+
        item: NAME "=" VALUE? _NL

        NAME: /\w/+
        VALUE: /./+

        %import common.NEWLINE -> _NL
        %import common.WS_INLINE
        %ignore WS_INLINE
    '''

parser = Lark(CONF_GRAMMAR, parser="earley")


def main():
    sample_conf = """
[bla]


a=Hello
this="that",4
empty=
"""

    r = parser.parse(sample_conf)
    print(r.pretty())


if __name__ == '__main__':
    main()
