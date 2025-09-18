---
title: Transform a Forest
description: Demonstrates subclassing TreeForestTransformer to directly transform an Earley SPPF (forest) and customize ambiguity handling in Lark.
source_url: https://lark-parser.readthedocs.io/en/stable/examples/advanced/tree_forest_transformer.html
---

# Transform a Forest

This example shows how to subclass TreeForestTransformer to directly transform a Shared Packed Parse Forest (SPPF) produced by Lark's Earley parser and how to control ambiguity handling.

## Example code

```python
from lark import Lark
from lark.parsers.earley_forest import TreeForestTransformer, handles_ambiguity, Discard

class CustomTransformer(TreeForestTransformer):

    @handles_ambiguity
    def sentence(self, trees):
        return next(tree for tree in trees if tree.data == 'simple')

    def simple(self, children):
        children.append('.')
        return self.tree_class('simple', children)

    def adj(self, children):
        return Discard

    def __default_token__(self, token):
        return token.capitalize()

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

parser = Lark(grammar, start='sentence', ambiguity='forest')
sentence = 'fruit flies like bananas'
forest = parser.parse(sentence)

tree = CustomTransformer(resolve_ambiguity=False).transform(forest)
print(tree.pretty())

# Output:
#
# simple
#   noun  Flies
#   verb  Like
#   noun  Bananas
#   .
#
```

## Downloads

- Download Python source: https://lark-parser.readthedocs.io/en/stable/_downloads/9d7d9d95319f4514ab7247f8eb86ddf0/tree_forest_transformer.py
- Download Jupyter notebook: https://lark-parser.readthedocs.io/en/stable/_downloads/2d7086e8ce7628b916237820c20847e4/tree_forest_transformer.ipynb

## See also

- Custom lexer: https://lark-parser.readthedocs.io/en/stable/examples/advanced/custom_lexer.html
- Simple JSON Parser: https://lark-parser.readthedocs.io/en/stable/examples/advanced/_json_parser.html
