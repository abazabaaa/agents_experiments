---
title: Parsing Indentation
description: Demonstrates parsing indentation (whitespace-significant languages) in Lark using the Indenter postlex stage to produce INDENT/DEDENT tokens.
source_url: https://lark-parser.readthedocs.io/en/stable/examples/indented_tree.html
---

# Parsing Indentation

A demonstration of parsing indentation (whitespace-significant language) and the usage of the Indenter class.

Since indentation is context-sensitive, a postlex stage is introduced to manufacture INDENT/DEDENT tokens.

It is crucial for the indenter that the `NL_type` matches the spaces (and tabs) after the newline.

## Example

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

## Downloads

- Download Python source code: indented_tree.py — https://lark-parser.readthedocs.io/en/stable/_downloads/7cc2abf4fecd3796ed4ad6d455bda349/indented_tree.py
- Download Jupyter notebook: indented_tree.ipynb — https://lark-parser.readthedocs.io/en/stable/_downloads/4b6a9b4fb62278f5d7a70e5b2900ff58/indented_tree.ipynb
