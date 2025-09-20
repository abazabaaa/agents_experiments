"""
Turtle DSL
===========

Implements a LOGO-like toy language for Python's turtle, with an interpreter.
This example uses Lark to parse a small DSL and then drives the turtle
module accordingly.
"""

# Standard imports
try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

import turtle

from lark import Lark, Transformer, v_args

# Grammar definition (must use raw triple-single-quotes for multiline grammars)
turtle_grammar = r'''
    start: instruction+

    instruction: MOVEMENT NUMBER            -> movement
               | "c" COLOR [COLOR]          -> change_color
               | "fill" code_block          -> fill
               | "repeat" NUMBER code_block -> repeat

    code_block: "{" instruction+ "}"

    MOVEMENT: "f"|"b"|"l"|"r"
    COLOR: LETTER+

    %import common.LETTER
    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
'''

parser = Lark(turtle_grammar)

# Transformer placeholder (not used by the rest of the example, provided for structure)
@v_args(inline=True)
class _PlaceholderTransformer(Transformer):
    pass


def run_instruction(t):
    if t.data == 'change_color':
        turtle.color(*t.children)   # We just pass the color names as-is

    elif t.data == 'movement':
        name, number = t.children
        { 'f': turtle.fd,
          'b': turtle.bk,
          'l': turtle.lt,
          'r': turtle.rt, }[name](int(number))

    elif t.data == 'repeat':
        count, block = t.children
        for i in range(int(count)):
            run_instruction(block)

    elif t.data == 'fill':
        turtle.begin_fill()
        run_instruction(t.children[0])
        turtle.end_fill()

    elif t.data == 'code_block':
        for cmd in t.children:
            run_instruction(cmd)
    else:
        raise SyntaxError('Unknown instruction: %s' % t.data)


def run_turtle(program):
    parse_tree = parser.parse(program)
    for inst in parse_tree.children:
        run_instruction(inst)


def main():
    while True:
        code = input('> ')
        try:
            run_turtle(code)
        except Exception as e:
            print(e)


def test():
    text = """
        c red yellow
        fill { repeat 36 {
            f200 l170
        }}
    """
    run_turtle(text)


if __name__ == '__main__':
    # test()
    main()
