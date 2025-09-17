---
title: How To Use Lark - Guide
source_url: https://lark-parser.readthedocs.io/en/stable/how_to_use.html
description: Recommended workflow, debugging tips, strict mode, and tools for using the Lark parsing library.
---

# How To Use Lark - Guide

## Work process

This is the recommended process for working with Lark:

1. Collect or create input samples that demonstrate key features or behaviors in the language you’re trying to parse.
2. Write a grammar. Aim for an intuitive structure that mirrors how you would explain your language to another person.
3. Try your grammar in Lark against each input sample. Make sure the resulting parse trees make sense.
4. Use Lark’s grammar features to shape the tree: get rid of superfluous rules by inlining them, and use aliases when specific cases need clarification. See: https://lark-parser.readthedocs.io/en/stable/tree_construction.html

You can perform steps 1–4 repeatedly, gradually growing your grammar to include more sentences.

5. Create a transformer to evaluate the parse tree into a structure you’ll be comfortable working with. This may include evaluating literals, merging branches, or converting the entire tree into your own set of AST classes.

Of course, some specific use-cases may deviate from this process. Feel free to suggest these cases, and they can be added to this page.

## Getting started

- Browse the examples to find a template that suits your purposes: https://github.com/lark-parser/lark/tree/master/examples
- Read the tutorials to understand how everything works (links on the main page): https://lark-parser.readthedocs.io/en/stable/index.html
- Use the Cheatsheet (PDF) for quick reference: https://lark-parser.readthedocs.io/en/latest/_static/lark_cheatsheet.pdf
- Use the reference pages for in-depth explanations (links on the main page): https://lark-parser.readthedocs.io/en/stable/index.html

## Debug

Grammars may contain non-obvious bugs, usually caused by rules or terminals interfering with each other in subtle ways. When debugging a misbehaving grammar, the following methodology is recommended:

1. Create a copy of the grammar, so you can change the parser/grammar without worries.
2. Find the minimal input that creates the error.
3. Slowly remove rules from the grammar, while making sure the error still occurs.

Usually, by the time you get to a minimal grammar, the problem becomes clear. If it doesn’t, feel free to ask on Gitter, or open an issue. Post a reproducing code sample with the minimal grammar and input, and the community will help.

### Regex collisions

A likely source of bugs occurs when two regexes in a grammar can match the same input. If both terminals have the same priority, most lexers will arbitrarily choose the first one that matches, which isn’t always the desired one. (A notable exception is the `dynamic_complete` lexer, which always tries all variations, at a performance cost.)

These collisions can be hard to notice, and their effects can be difficult to debug.

To help, Lark can utilize an external library called `interegular`. If installed, Lark uses it to check for collisions and warn about conflicts it can find:

```python
import logging
from lark import Lark, logger

logger.setLevel(logging.WARN)

collision_grammar = '''
start: A | B
A: /a+/
B: /[ab]+/
'''
p = Lark(collision_grammar, parser='lalr')

# Output:
# Collision between Terminals B and A. The lexer will choose between them arbitrarily
# Example Collision: a
```

Install interegular for Lark: `pip install 'lark[interegular]'`.

Notes:
- Interegular currently only runs when the lexer is `basic` or `contextual`.
- Some advanced regex features (lookahead/lookbehind) may prevent interegular from detecting collisions.

### Shift/Reduce collisions

By default Lark automatically resolves Shift/Reduce conflicts as Shift and emits debug messages. When users pass `debug=True`, those notifications are written as warnings. To get the messages printed you have to configure the logger beforehand. For example:

```python
import logging
from lark import Lark, logger

logger.setLevel(logging.DEBUG)

collision_grammar = '''
start: as as
as: a*
a: "a"
'''
p = Lark(collision_grammar, parser='lalr', debug=True)
# Shift/Reduce conflict for terminal A: (resolving as shift)
#  * <as : >
# Shift/Reduce conflict for terminal A: (resolving as shift)
#  * <as : __as_star_0>
```

### Strict-Mode

Lark, by default, accepts grammars with unresolved Shift/Reduce collisions (resolved to shift) and regex collisions. Strict-mode allows users to validate that their grammars don’t contain these collisions.

- When Lark is initialized with `strict=True`, it raises an exception on any Shift/Reduce or regex collision.
- If `interegular` isn’t installed, an exception is thrown.
- Users must resolve collisions manually: adjust rule priorities for Shift/Reduce conflicts; change regexes so they no longer both match the same input for regex collisions.

Strict-mode currently applies only to LALR.

```python
from lark import Lark

collision_grammar = '''
start: as as
as: a*
a: "a"
'''
p = Lark(collision_grammar, parser='lalr', strict=True)

# Traceback (most recent call last):
#   ...
# lark.exceptions.GrammarError: Shift/Reduce conflict for terminal A. [strict-mode]
```

## Tools

### Stand-alone parser

Lark can generate a stand-alone LALR(1) parser from a grammar. The resulting module provides the same interface as Lark, but with a fixed grammar and reduced functionality.

Run using:

```bash
python -m lark.tools.standalone
```

For a play-by-play, read the tutorial: http://blog.erezsh.com/create-a-stand-alone-lalr1-parser-in-python/

### Import Nearley.js grammars

It is possible to import Nearley grammars into Lark. The JavaScript code is translated using Js2Py. See the tools page for more information: https://lark-parser.readthedocs.io/en/stable/tools.html
