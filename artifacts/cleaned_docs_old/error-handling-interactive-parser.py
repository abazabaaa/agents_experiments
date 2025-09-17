# Error handling using an interactive parser
#
# This example demonstrates error handling using an interactive parser in LALR.
#
# When the parser encounters an UnexpectedToken exception, it creates an
# interactive parser with the current parse-state, and lets you control how
# to proceed step-by-step. When you've achieved the correct parse-state,
# you can resume the run by returning True.
#
# This standalone script includes a minimal JSON parser built with Lark (LALR),
# so it doesn't depend on an external _json_parser module.

from ast import literal_eval
from lark import Lark, Transformer, Token

# Build a minimal JSON grammar using LALR.
# We define COMMA and use SIGNED_NUMBER so the error handler can
# detect and manipulate these specific token types.
json_grammar = r"""
?start: value

?value: object
      | array
      | string
      | SIGNED_NUMBER -> number
      | "true"        -> true
      | "false"       -> false
      | "null"        -> null

string : ESCAPED_STRING
array  : "[" [value (COMMA value)*] "]"
object : "{" [pair (COMMA pair)*] "}"
pair   : string ":" value

COMMA  : ","

%import common.ESCAPED_STRING
%import common.SIGNED_NUMBER
%import common.WS
%ignore WS
"""

class ToPython(Transformer):
    # Convert tokens/trees into Python values
    def string(self, s):
        # Properly unescape JSON strings
        return literal_eval(s[0])

    def number(self, n):
        # Return floats to match the example output
        return float(n[0])

    def array(self, items):
        # items looks like [value, COMMA, value, COMMA, ...]
        # Keep only the values (even indices)
        return items[::2] if items else []

    def pair(self, items):
        # items = [key, ':', value]
        return (items[0], items[-1])

    def object(self, items):
        return dict(items)

    def true(self, _):
        return True

    def false(self, _):
        return False

    def null(self, _):
        return None

# The JSON parser object used by the demo below
json_parser = Lark(
    json_grammar,
    parser="lalr",
    start="start",
    transformer=ToPython(),
)

# Error handler demonstrating interactive parsing:
# - If we see a stray COMMA, skip it.
# - If we see a number where a COMMA is expected, inject a COMMA and then re-feed the number.
# Return True to resume the parse; return False to stop and raise the exception.
def ignore_errors(e):
    if e.token.type == 'COMMA':
        # Skip extra commas
        return True
    elif e.token.type == 'SIGNED_NUMBER':
        # Insert a missing comma, then retry the number
        e.interactive_parser.feed_token(Token('COMMA', ','))
        e.interactive_parser.feed_token(e.token)
        return True

    # Unhandled error. Will stop parse and raise exception
    return False


def main():
    s = "[0 1, 2,, 3,,, 4, 5 6 ]"
    res = json_parser.parse(s, on_error=ignore_errors)
    print(res)  # Expected: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]


if __name__ == "__main__":
    main()
