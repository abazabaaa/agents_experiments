"""
Error handling using an interactive parser (LALR)

This standalone script demonstrates Lark's interactive error handling using a
JSON parser. When the parser encounters an UnexpectedToken, we use the
interactive parser to either skip or insert tokens and continue parsing.

The example input intentionally contains mistakes (missing/extra commas), and
the error handler recovers by either skipping stray commas or inserting a
missing comma before a number.

Run this file to see the recovery in action.
"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------
from lark import Lark, Transformer, v_args, Token
import json


# ------------------------------------------------------------
# Grammar Definition (Lark) — kept as a raw triple-quoted string
# Notes:
# - We define COMMA explicitly so error handling can test for e.token.type == 'COMMA'
# - SIGNED_NUMBER comes from Lark's common terminals and is used in the demo
# ------------------------------------------------------------
JSON_GRAMMAR = r'''
?start: value

?value: object
      | array
      | string
      | SIGNED_NUMBER      -> number
      | "true"             -> true
      | "false"            -> false
      | "null"             -> null

array  : "[" [value (COMMA value)*] "]"
object : "{" [pair (COMMA pair)*] "}"
pair   : string ":" value

string : ESCAPED_STRING

COMMA  : ","

%import common.ESCAPED_STRING
%import common.SIGNED_NUMBER
%import common.WS
%ignore WS
'''


# ------------------------------------------------------------
# Transformer — produces native Python values from the parse tree
# ------------------------------------------------------------
@v_args(inline=True)
class TreeToJson(Transformer):
    def string(self, s):
        # Convert ESCAPED_STRING token (including quotes) into a Python str
        return json.loads(s)

    def number(self, n):
        # Convert numbers to float to match the example's printed output
        return float(n)

    def array(self, *items):
        return list(items)

    def pair(self, k, v):
        return (k, v)

    def object(self, *pairs):
        return dict(pairs)

    def true(self):
        return True

    def false(self):
        return False

    def null(self):
        return None


# ------------------------------------------------------------
# Parser Construction — LALR parser with transformer
# ------------------------------------------------------------
json_parser = Lark(JSON_GRAMMAR, parser='lalr', transformer=TreeToJson())


# ------------------------------------------------------------
# Error handling using an interactive parser
# (Converted directly from the notebook's code cell)
# ------------------------------------------------------------

def ignore_errors(e):
    if e.token.type == 'COMMA':
        # Skip comma
        return True
    elif e.token.type == 'SIGNED_NUMBER':
        # Try to feed a comma and retry the number
        e.interactive_parser.feed_token(Token('COMMA', ','))
        e.interactive_parser.feed_token(e.token)
        return True

    # Unhandled error. Will stop parse and raise exception
    return False


# ------------------------------------------------------------
# Main execution — demonstrates recovery from malformed JSON array
# ------------------------------------------------------------

def main():
    # Intentionally malformed: missing commas and extra commas
    s = "[0 1, 2,, 3,,, 4, 5 6 ]"
    res = json_parser.parse(s, on_error=ignore_errors)
    print(res)      # prints [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]


if __name__ == '__main__':
    main()
