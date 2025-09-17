---
title: Turtle DSL Example (Lark + Python Turtle)
description: A LOGO-like toy language implemented using Lark to control Python's turtle graphics, including grammar, parser, and interpreter.
source_url: https://lark-parser.readthedocs.io/en/stable/_downloads/9cadc23f6b1e9e52f35d3cb0a28053b0/turtle_dsl.py
---

# Turtle DSL

Implements a LOGO-like toy language for Python’s turtle, with an interpreter.

## Overview

This example uses Lark to define a simple DSL to control Python's turtle graphics. It includes:
- A grammar for commands (movement, color changes, fill blocks, and repeat blocks)
- An interpreter that walks the parse tree and invokes turtle commands
- An interactive REPL (`main`) and a demo (`test`)

## Code

```python
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

- Run the script to start a simple REPL and enter commands like:
  - c red
  - f100 r90 f100
  - fill { repeat 36 { f200 l170 } }
- Uncomment the `test()` call to run the demo pattern.

## Grammar Highlights

- Movements: f (forward), b (back), l (left), r (right) followed by a number.
- Color: c <fg_color> [bg_color]
- Fill block: fill { ... }
- Repeat: repeat N { ... }
