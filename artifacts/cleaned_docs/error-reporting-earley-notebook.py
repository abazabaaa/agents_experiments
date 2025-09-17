"""
Example-Driven Error Reporting (Earley)

A standalone Python script converted from the provided Jupyter notebook.
Demonstrates example-driven error reporting with Lark's Earley parser.
(See also: error_reporting_lalr.py)
"""

# Imports
from lark import Lark, UnexpectedInput


# ------------------------------------------------------------
# JSON Grammar (inlined from the json_parser example)
# ------------------------------------------------------------
# Note: Using a raw triple-quoted string preserves Lark grammar syntax exactly.
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


# ------------------------------------------------------------
# Build the Earley parser for JSON
# ------------------------------------------------------------
# The notebook targets Earley-specific error reporting features (use_accepts=True),
# so we explicitly choose the Earley parser here.
json_parser = Lark(json_grammar, parser='earley')


# ------------------------------------------------------------
# Error Types and Formatting
# ------------------------------------------------------------
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


# ------------------------------------------------------------
# Parsing with Example-Driven Error Classification (Earley)
# ------------------------------------------------------------
# When parsing fails, we try to classify the error by matching it against
# a set of example inputs for each error type. This uses Earley-specific
# "accepts" information (use_accepts=True).

def parse(json_text):
    try:
        return json_parser.parse(json_text)
    except UnexpectedInput as u:
        exc_class = u.match_examples(json_parser.parse, {
            JsonMissingOpening: ['{"foo": ]}',
                                 '{"foor": }}',
                                 '{"foo": }'],
            JsonMissingClosing: ['{"foo": [}',
                                 '{',
                                 '{"a": 1',
                                 '[1'],
            JsonMissingComma: ['[1 2]',
                               '[false 1]',
                               '["b" 1]',
                               '{"a":true 1:4}',
                               '{"a":1 1:4}',
                               '{"a":"b" 1:4}'],
            JsonTrailingComma: ['[,]',
                                '[1,]',
                                '[1,2,]',
                                '{"foo":1,}',
                                '{"foo":false,"bar":true,}']
        }, use_accepts=True)
        if not exc_class:
            # If we couldn't match a specific error type, re-raise the original exception
            raise
        # Raise a friendlier error message with context
        raise exc_class(u.get_context(json_text), u.line, u.column)


# ------------------------------------------------------------
# Minimal smoke tests from the notebook
# ------------------------------------------------------------

def test():
    try:
        parse('{"example1": "value"')
    except JsonMissingClosing as e:
        print(e)

    try:
        parse('{"example2": ] ')
    except JsonMissingOpening as e:
        print(e)


if __name__ == '__main__':
    test()
