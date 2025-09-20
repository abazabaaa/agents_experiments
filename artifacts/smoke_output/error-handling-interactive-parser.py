"""
Example: Error handling using an interactive parser (from Lark docs)

This module demonstrates how to use an interactive LALR parser to handle
UnexpectedToken exceptions. When the parser encounters an error it will call
an on_error handler with an exception object exposing an interactive_parser
that can be used to feed tokens to resume parsing.
"""

# Error handling using an interactive parser
#
# This example demonstrates error handling using an interactive parser in LALR
#
# When the parser encounters an UnexpectedToken exception, it creates an
# interactive parser with the current parse-state, and lets you control how
# to proceed step-by-step. When you've achieved the correct parse-state,
# you can resume the run by returning True.

from lark import Token

from _json_parser import json_parser


def ignore_errors(e):
    """Error handler passed as on_error to json_parser.parse.

    The handler receives an exception-like object `e` with attributes:
      - token: the offending Token
      - interactive_parser: a parser instance in the current state, which
        allows feeding tokens via feed_token()

    Return True to continue parsing after attempting to fix the error, or
    False to stop and re-raise the exception.
    """
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


def main():
    s = "[0 1, 2,, 3,,, 4, 5 6 ]"
    res = json_parser.parse(s, on_error=ignore_errors)
    print(res)      # prints [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]


if __name__ == '__main__':
    main()
