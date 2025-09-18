"""
Simple JSON Parser

The code is short and clear, and outperforms every other parser (that's written in Python).
For an explanation, check out the JSON parser tutorial at /docs/json_tutorial.md

(this is here for use by the other examples)
"""

# Imports required for building and transforming the parse tree
from lark import Lark, Transformer, v_args


# -----------------------------------------------------------------------------
# Lark grammar definition for JSON (kept exactly as in the notebook)
# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# Transformer: Converts the parse tree into native Python objects
# -----------------------------------------------------------------------------
class TreeToJson(Transformer):
    # Keep decorator and behavior exactly as in the notebook
    @v_args(inline=True)
    def string(self, s):
        # Remove the surrounding quotes and unescape embedded quotes
        return s[1:-1].replace('\\"', '"')

    # These rules map directly to Python builtins for structure assembly
    array = list
    pair = tuple
    object = dict

    # Parse numbers as floats (inline to receive the single token directly)
    number = v_args(inline=True)(float)

    # JSON literals
    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


# -----------------------------------------------------------------------------
# Create the JSON parser with Lark, using the LALR algorithm
# (Preserving the exact configuration and comments from the notebook)
# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# Main: Demonstrate parser functionality with example inputs
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import sys

    # If a JSON string is provided via command line, parse it directly
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
        result = json_parser.parse(text)
        print(result)
    else:
        # Otherwise, run a few sample parses to showcase functionality
        examples = [
            '42',
            '"hello, \\"world\\""',
            '["a", 1, true, null, {"x": -3.14}]',
            '{"a": 1, "b": [2, 3], "ok": false}'
        ]

        for i, ex in enumerate(examples, 1):
            print(f'Example {i}: {ex}')
            print('Parsed:', json_parser.parse(ex))
            print('-' * 40)
