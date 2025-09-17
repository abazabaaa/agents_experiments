---
title: Handling Ambiguity (Lark Fruit Flies Example)
description: Demonstrates extracting explicit ambiguity from Lark’s Earley parser using the classic “fruit flies like bananas” sentence.
source_url: https://lark-parser.readthedocs.io/en/stable/examples/fruitflies.html
related:
  - https://lark-parser.readthedocs.io/en/stable/examples/index.html
  - https://lark-parser.readthedocs.io/en/stable/examples/calc.html
  - https://lark-parser.readthedocs.io/en/stable/examples/lark_grammar.html
resources:
  python_source: https://lark-parser.readthedocs.io/en/stable/_downloads/b0239cee17ba033b2ccfffe66491b86e/fruitflies.py
  notebook: https://lark-parser.readthedocs.io/en/stable/_downloads/9ebc86868010e2fc400ecf1ef8a5aa4a/fruitflies.ipynb
---

# Handling Ambiguity

A demonstration of ambiguity in Lark’s Earley parser, showing how to get explicit ambiguity.

Note: You can download the full example code at the original page: https://lark-parser.readthedocs.io/en/stable/examples/fruitflies.html#sphx-glr-download-examples-fruitflies-py

## Example

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
    tree.pydot__tree_to_png(parser.parse(sentence), filename)

def make_dot(filename):
    tree.pydot__tree_to_dot(parser.parse(sentence), filename)

if __name__ == '__main__':
    print(parser.parse(sentence).pretty())
    # make_png(sys.argv[1])
    # make_dot(sys.argv[1])
```

### Sample Output

```
_ambig
  comparative
    noun  fruit
    verb  flies
    noun  bananas
  simple
    noun
      fruit
      flies
    verb  like
    noun  bananas

(or view a nicer version at "./fruitflies.png")
```

## Downloads

- Python source: https://lark-parser.readthedocs.io/en/stable/_downloads/b0239cee17ba033b2ccfffe66491b86e/fruitflies.py
- Jupyter notebook: https://lark-parser.readthedocs.io/en/stable/_downloads/9ebc86868010e2fc400ecf1ef8a5aa4a/fruitflies.ipynb

## See Also

- Examples index: https://lark-parser.readthedocs.io/en/stable/examples/index.html
- Previous: Lark Grammar — https://lark-parser.readthedocs.io/en/stable/examples/lark_grammar.html
- Next: Basic calculator — https://lark-parser.readthedocs.io/en/stable/examples/calc.html
