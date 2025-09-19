"""
Reconstruct a JSON

This module was converted from a Jupyter notebook JSON provided by the user.
Source: user-provided notebook JSON
Original notebook metadata: {'cells': 2}

Demonstrates the experimental text-reconstruction feature of Lark.
The Reconstructor takes a parse tree (already filtered from punctuation, of course),
and reconstructs it into correct text, that can be parsed correctly.
It can be useful for creating "hooks" to alter data before handing it to other parsers. You can also use it to generate samples from scratch.
"""

# Section: Imports
import json

from lark import Lark
from lark.reconstruct import Reconstructor

# The grammar is provided by an external module in the original notebook.
# Keep the import as in the original notebook to preserve behavior.
from _json_parser import json_grammar

# Section: Test JSON
test_json = '''
    {
        "empty_object" : {},
        "empty_array"  : [],
        "booleans"     : { "YES" : true, "NO" : false },
        "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ],
        "strings"      : [ "This", [ "And" , "That", "And a \"b" ] ],
        "nothing"      : null
    }
'''


# Section: Tests (Earley)
def test_earley():

    json_parser = Lark(json_grammar, maybe_placeholders=False)
    tree = json_parser.parse(test_json)

    new_json = Reconstructor(json_parser).reconstruct(tree)
    print (new_json)
    print (json.loads(new_json) == json.loads(test_json))


# Section: Tests (LALR)
def test_lalr():

    json_parser = Lark(json_grammar, parser='lalr', maybe_placeholders=False)
    tree = json_parser.parse(test_json)

    new_json = Reconstructor(json_parser).reconstruct(tree)
    print (new_json)
    print (json.loads(new_json) == json.loads(test_json))


# Execution guard
if __name__ == '__main__':
    test_earley()
    test_lalr()
