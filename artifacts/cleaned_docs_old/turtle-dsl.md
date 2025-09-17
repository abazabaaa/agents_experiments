---
title: Turtle DSL (Lark + Python turtle)
description: A LOGO-like toy language implemented with Lark for parsing and Python’s turtle for drawing. Includes grammar, interpreter, and examples.
source_url: https://lark-parser.readthedocs.io/en/stable/_downloads/9cadc23f6b1e9e52f35d3cb0a28053b0/turtle_dsl.py
language: python
---

# Turtle DSL

Implements a LOGO-like toy language for Python’s turtle, with an interpreter using Lark.

## Overview

This example defines a small DSL for turtle graphics with the following commands:
- f N: forward N
- b N: back N
- l N: left N degrees
- r N: right N degrees
- c COLOR [OUTLINE]: set fill and optional outline color
- fill { ... }: fill the enclosed block
- repeat N { ... }: repeat the block N times

## Code

```python
"""
Turtle DSL
==========

Implements a LOGO-like toy language for Python’s turtle, with interpreter.
"""

try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

import turtle

from lark import Lark

turtle_grammar = """
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

parser = Lark(turtle_grammar)

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
```

## Usage

- Interactive mode: run the script and enter DSL commands at the prompt.
- Example program (same as test function):

```text
c red yellow
fill { repeat 36 {
    f200 l170
}}
```

This will draw a colorful, filled spiral-like pattern.

## Notes

- Requires lark and a GUI-capable environment for turtle graphics.
- COLOR tokens accept letter names (e.g., "red", "blue").
- Python 2 compatibility shim included for input().
