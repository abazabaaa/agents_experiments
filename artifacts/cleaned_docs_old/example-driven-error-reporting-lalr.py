# Example-Driven Error Reporting
# A demonstration of example-driven error reporting with the LALR parser
# (See also: error_reporting_earley.py)
#
# This script demonstrates example-driven error reporting with Lark's LALR parser.
# The JSON grammar is embedded so the script is standalone (no external _json_parser import).

from lark import Lark, UnexpectedInput

# JSON grammar (adapted from Lark's json example)
json_grammar = r"""
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
"""

# Build a LALR parser for the JSON grammar
json_parser = Lark(json_grammar, parser='lalr')


# Custom exception hierarchy for clearer, example-driven error messages
class JsonSyntaxError(SyntaxError):
    def __str__(self):
        context, line, column = self.args
        return '%s at line %s, column %s.\n\n%s' % (self.label, line, column, context)

class JsonMissingValue(JsonSyntaxError):
    label = 'Missing Value'

class JsonMissingOpening(JsonSyntaxError):
    label = 'Missing Opening'

class JsonMissingClosing(JsonSyntaxError):
    label = 'Missing Closing'

class JsonMissingComma(JsonSyntaxError):
    label = 'Missing Comma'

class JsonTrailingComma(JsonSyntaxError):
    label = 'Trailing Comma'


def parse(json_text: str):
    """Parse JSON text, and raise specialized syntax errors when possible.

    Uses UnexpectedInput.match_examples to classify the parsing error by
    matching it against a set of representative example snippets.
    """
    try:
        return json_parser.parse(json_text)
    except UnexpectedInput as u:
        # Map representative examples to error classes. Lark will try to match
        # the current failure to one of these patterns.
        exc_class = u.match_examples(json_parser.parse, {
            JsonMissingOpening: [
                '{"foo": ]}',
                '{"foor": }}',
                '{"foo": }',
            ],
            JsonMissingClosing: [
                '{"foo": [}',
                '{',
                '{"a": 1',
                '[1',
            ],
            JsonMissingComma: [
                '[1 2]',
                '[false 1]',
                '["b" 1]',
                '{"a":true 1:4}',
                '{"a":1 1:4}',
                '{"a":"b" 1:4}',
            ],
            JsonTrailingComma: [
                '[,]',
                '[1,]',
                '[1,2,]',
                '{"foo":1,}',
                '{"foo":false,"bar":true,}',
            ],
            # JsonMissingValue is defined but not used here; you can add
            # examples and map to it if desired.
        }, use_accepts=True)

        if not exc_class:
            # Couldn't classify the error; re-raise the original exception
            raise

        # Raise a clearer, domain-specific exception with context
        raise exc_class(u.get_context(json_text), u.line, u.column)


def test():
    """Simple demonstration showing two error cases and their messages."""
    try:
        # Missing closing brace
        parse('{"example1": "value"')
    except JsonMissingClosing as e:
        print(e)

    try:
        # A stray closing bracket without a matching opening structure
        parse('{"example2": ] ')
    except JsonMissingOpening as e:
        print(e)


if __name__ == '__main__':
    test()
