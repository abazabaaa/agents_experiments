"""
Reconstruct a JSON (standalone script)

This script demonstrates Lark's experimental text-reconstruction feature.

The Reconstructor takes a parse tree (already filtered from punctuation, of course),
and reconstructs it into correct text that can be parsed correctly again.
It can be useful for creating hooks to alter data before handing it to other parsers,
or to generate valid samples from scratch.

Converted from the Lark documentation notebook: reconstruct_json.ipynb
(Original used: from _json_parser import json_grammar; here we inline the grammar.)
"""

# --- Imports ---------------------------------------------------------------
import json

from lark import Lark, Transformer, v_args  # Transformer/v_args imported for completeness
from lark.reconstruct import Reconstructor


# --- Lark JSON grammar (module-level constant) ----------------------------
# Preserved as a triple-quoted raw string, with exact grammar syntax.
json_grammar = r'''
    ?start: value

    ?value: object
          | array
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    array  : "[" [value ("," value)*] "]"
    object : "{" [pair ("," pair)*] "}"
    pair   : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
'''


# --- Example input (from the original notebook) ---------------------------
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


# --- Tests: Parse + Reconstruct using Earley and LALR ---------------------
def test_earley():
    """Parse and reconstruct using the default (Earley) parser."""
    json_parser = Lark(json_grammar, maybe_placeholders=False)
    tree = json_parser.parse(test_json)

    new_json = Reconstructor(json_parser).reconstruct(tree)
    print(new_json)
    print(json.loads(new_json) == json.loads(test_json))


def test_lalr():
    """Parse and reconstruct using the LALR parser."""
    json_parser = Lark(json_grammar, parser='lalr', maybe_placeholders=False)
    tree = json_parser.parse(test_json)

    new_json = Reconstructor(json_parser).reconstruct(tree)
    print(new_json)
    print(json.loads(new_json) == json.loads(test_json))


# --- Main execution -------------------------------------------------------
if __name__ == '__main__':
    # Run both variants to demonstrate compatibility
    test_earley()
    test_lalr()
