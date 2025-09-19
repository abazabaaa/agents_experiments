---
title: "Parsing Indentation"
description: "Demonstration of parsing indentation using Lark's Indenter class. Shows how to manufacture INDENT/DEDENT tokens with a postlex stage and includes a runnable Python example."
source_url: "" 
---

# Parsing Indentation

A demonstration of parsing indentation (a "whitespace significant" language) and the usage of the Indenter class.

Since indentation is context-sensitive, a postlex stage is introduced to manufacture INDENT/DEDENT tokens.

It is crucial for the indenter that the NL_type matches the spaces (and tabs) after the newline.

## Grammar (Lark)

The exact grammar used by the example (preserved verbatim):

```lark
    ?start: _NL* tree

    tree: NAME _NL [_INDENT tree+ _DEDENT]

    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE

    _NL: /(\r?\n[\t ]*)+/
```

## Python example

The following Python script demonstrates using the grammar above with Lark and a custom Indenter. All code is preserved and normalized; the grammar string inside the Python code is identical to the grammar shown above.

```python
from lark import Lark
from lark.indenter import Indenter

tree_grammar = r"""
    ?start: _NL* tree

    tree: NAME _NL [_INDENT tree+ _DEDENT]

    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE

    _NL: /(\r?\n[\t ]*)+/
"""

class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

parser = Lark(tree_grammar, parser='lalr', postlex=TreeIndenter())

test_tree = """
a
    b
    c
        d
        e
    f
        g
"""

def test():
    print(parser.parse(test_tree).pretty())

if __name__ == '__main__':
    test()
```
