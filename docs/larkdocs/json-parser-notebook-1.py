"""
Simple JSON Parser (Lark example)

The code is short and clear, and outperforms every other parser (that's
written in Python). For an explanation, check out the JSON parser tutorial at
/docs/json_tutorial.md

This standalone script was converted from the original Jupyter notebook. It:
- defines the JSON grammar (kept verbatim) as a raw triple-quoted string,
- implements a Transformer that turns the parse tree into Python objects,
- shows both Earley (commented) and LALR parser configurations,
- includes a small test and a CLI entry point.
"""

# ---------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------
import sys

from lark import Lark, Transformer, v_args


# ---------------------------------------------------------------------
# JSON grammar (kept exactly as in the notebook)
# ---------------------------------------------------------------------
JSON_GRAMMAR = r'''
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

# Keep the original variable name from the notebook for reference
json_grammar = JSON_GRAMMAR


# ---------------------------------------------------------------------
# Transformer: Convert parse tree to Python objects
# ---------------------------------------------------------------------
class TreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[1:-1].replace('\"', '"')

    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


# ---------------------------------------------------------------------
# Parser construction
# ---------------------------------------------------------------------
# Create the JSON parser with Lark, using the Earley algorithm
# json_parser = Lark(JSON_GRAMMAR, parser='earley', lexer='basic')
# def parse(x):
#     return TreeToJson().transform(json_parser.parse(x))

# Create the JSON parser with Lark, using the LALR algorithm
json_parser = Lark(
    JSON_GRAMMAR,
    parser='lalr',
    # Using the basic lexer isn't required, and isn't usually recommended.
    # But, it's good enough for JSON, and it's slightly faster.
    lexer='basic',
    # Disabling propagate_positions and placeholders slightly improves speed
    propagate_positions=False,
    maybe_placeholders=False,
    # Using an internal transformer is faster and more memory efficient
    transformer=TreeToJson(),
)
parse = json_parser.parse


# ---------------------------------------------------------------------
# Test helper
# ---------------------------------------------------------------------
def test():
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

    j = parse(test_json)
    print(j)
    import json
    assert j == json.loads(test_json)


# ---------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------
if __name__ == '__main__':
    # test()
    with open(sys.argv[1]) as f:
        print(parse(f.read()))
