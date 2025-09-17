#!/usr/bin/env python3
"""
Turtle DSL — a LOGO-like toy language for Python's turtle, with interpreter.

This script is a standalone version of the Lark example notebook
`turtle_dsl.ipynb`. It defines a small DSL using a Lark grammar and interprets
its parse tree to drive Python's turtle module.

Notebook sections were converted into commented sections below, while keeping:
- Lark grammar intact inside a triple-quoted raw string
- Parse-tree handling code and execution logic
- Example program and an interactive REPL
"""

# --- Imports ---
import turtle
from lark import Lark

# Python 2 compatibility for input (harmless on Python 3)
try:
    input = raw_input  # type: ignore[name-defined]
except NameError:
    pass

# --- Grammar Definition (from the notebook; kept verbatim) ---
TURTLE_GRAMMAR = r"""
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
"""

# --- Parser Initialization ---
parser = Lark(TURTLE_GRAMMAR)

# --- Interpreter Helpers ---
def run_instruction(t):
    """Execute a single instruction node from the parse tree."""
    if t.data == 'change_color':
        turtle.color(*t.children)   # Pass the color names as-is

    elif t.data == 'movement':
        name, number = t.children
        {
            'f': turtle.fd,
            'b': turtle.bk,
            'l': turtle.lt,
            'r': turtle.rt,
        }[name](int(number))

    elif t.data == 'repeat':
        count, block = t.children
        for _ in range(int(count)):
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
    """Parse the program text and execute it using the interpreter above."""
    parse_tree = parser.parse(program)
    for inst in parse_tree.children:
        run_instruction(inst)


# --- Example Program (from the notebook) ---
def test():
    text = """
        c red yellow
        fill { repeat 36 {
            f200 l170
        }}
    """
    run_turtle(text)


# --- Interactive REPL ---
def main():
    # Type commands like: f100, l90, c red blue, fill { f100 l90 f100 l90 }, etc.
    # Press Ctrl+C or send EOF (Ctrl+D/Ctrl+Z) to exit.
    while True:
        try:
            code = input('> ')
        except (EOFError, KeyboardInterrupt):
            print()  # newline on exit
            break
        try:
            run_turtle(code)
        except Exception as e:
            print(e)


# --- Entry Point ---
if __name__ == '__main__':
    # Uncomment to run the example instead of the REPL
    # test()
    main()
