---
title: Handling Ambiguity (Fruit Flies Example)
description: Demonstrates how to obtain explicit ambiguity results using Lark's Earley parser. Includes a minimal grammar and Python code that produces an ambiguous parse for the sentence "fruit flies like bananas".
source_url: https://lark-parser.readthedocs.io/en/stable/examples/fruitflies.html
---

# Handling Ambiguity

A demonstration of ambiguity.

This example shows how to get explicit ambiguity from Lark’s Earley parser.

## Python code

```python
import sys
from lark import Lark, tree

grammar = """
    sentence: noun verb noun        -> simple
            | noun verb "like" noun -> comparative

    noun: adj? NOUN
    verb: VERB
    adj: ADJ

    NOUN: "flies" | "bananas" | "fruit"
    VERB: "like" | "flies"
    ADJ: "fruit"

    %import common.WS
    %ignore WS
"""

parser = Lark(grammar, start='sentence', ambiguity='explicit')

sentence = 'fruit flies like bananas'

def make_png(filename):
    tree.pydot__tree_to_png( parser.parse(sentence), filename)

def make_dot(filename):
    tree.pydot__tree_to_dot( parser.parse(sentence), filename)

if __name__ == '__main__':
    print(parser.parse(sentence).pretty())
    # make_png(sys.argv[1])
    # make_dot(sys.argv[1])

# Output:
#
# _ambig
#   comparative
#     noun  fruit
#     verb  flies
#     noun  bananas
#   simple
#     noun
#       fruit
#       flies
#     verb  like
#     noun  bananas
#
# (or view a nicer version at "./fruitflies.png")
```

## Downloads

- Download Python source code: fruitflies.py — https://lark-parser.readthedocs.io/en/stable/_downloads/b0239cee17ba033b2ccfffe66491b86e/fruitflies.py
- Download Jupyter notebook: fruitflies.ipynb — https://lark-parser.readthedocs.io/en/stable/_downloads/9ebc86868010e2fc400ecf1ef8a5aa4a/fruitflies.ipynb

## See also

- Previous: Lark Grammar — https://lark-parser.readthedocs.io/en/stable/examples/lark_grammar.html
- Next: Basic calculator — https://lark-parser.readthedocs.io/en/stable/examples/calc.html
