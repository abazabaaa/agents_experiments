---
title: Reconstruct a JSON with Lark's Reconstructor
source_url: https://lark-parser.readthedocs.io/en/stable/_downloads/e6911b819cf4afa1ca68b5be22630e13/reconstruct_json.py
description: Demonstrates Lark’s experimental text-reconstruction feature to rebuild valid JSON from a parse tree using Reconstructor.
---

Reconstruct a JSON

Demonstrates the experimental text-reconstruction feature.

The Reconstructor takes a parse tree (already filtered from punctuation) and reconstructs it into correct text that can be parsed again. It can be useful for creating hooks to alter data before handing it to other parsers, or to generate sample text from scratch.

Code example

```python
"""
Reconstruct a JSON
==================

Demonstrates the experimental text-reconstruction feature

The Reconstructor takes a parse tree (already filtered from punctuation, of course),
and reconstructs it into correct text, that can be parsed correctly.
It can be useful for creating "hooks" to alter data before handing it to other parsers. You can also use it to generate samples from scratch.
"""

import json

from lark import Lark
from lark.reconstruct import Reconstructor

from _json_parser import json_grammar

test_json = '''
    {
        "empty_object" : {},
        "empty_array"  : [],
        "booleans"     : { "YES" : true, "NO" : false },
        "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ],
        "strings"      : [ "This", [ "And" , "That", "And a \\"b" ] ],
        "nothing"      : null
    }
'''

def test_earley():

    json_parser = Lark(json_grammar, maybe_placeholders=False)
    tree = json_parser.parse(test_json)

    new_json = Reconstructor(json_parser).reconstruct(tree)
    print(new_json)
    print(json.loads(new_json) == json.loads(test_json))

def test_lalr():

    json_parser = Lark(json_grammar, parser='lalr', maybe_placeholders=False)
    tree = json_parser.parse(test_json)

    new_json = Reconstructor(json_parser).reconstruct(tree)
    print(new_json)
    print(json.loads(new_json) == json.loads(test_json))

if __name__ == "__main__":
    test_earley()
    test_lalr()
```
