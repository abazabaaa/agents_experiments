---
title: Lark Grammar - Reference Implementation (LALR(1))
description: A small Python script that loads Lark's built-in grammar and verifies that several example grammars parse successfully using the LALR(1) parser.
source_url: https://lark-parser.readthedocs.io/en/stable/_downloads/b9abd703bb1b061d8ae5f6ab1b9393e8/lark_grammar.py
---

# Lark Grammar

A reference implementation of the Lark grammar (using LALR(1)).

## Python Source

```python
"""
Lark Grammar
============

A reference implementation of the Lark grammar (using LALR(1))
"""
import lark
from pathlib import Path

examples_path = Path(__file__).parent
lark_path = Path(lark.__file__).parent

parser = lark.Lark.open(lark_path / 'grammars/lark.lark', rel_to=__file__, parser="lalr")

grammar_files = [\
    examples_path / 'advanced/python2.lark',\
    examples_path / 'relative-imports/multiples.lark',\
    examples_path / 'relative-imports/multiple2.lark',\
    examples_path / 'relative-imports/multiple3.lark',\
    examples_path / 'tests/no_newline_at_end.lark',\
    examples_path / 'tests/negative_priority.lark',\
    examples_path / 'standalone/json.lark',\
    lark_path / 'grammars/common.lark',\
    lark_path / 'grammars/lark.lark',\
    lark_path / 'grammars/unicode.lark',\
    lark_path / 'grammars/python.lark',\
]

def test():
    for grammar_file in grammar_files:
        tree = parser.parse(open(grammar_file).read())
    print("All grammars parsed successfully")

if __name__ == '__main__':
    test()

```
