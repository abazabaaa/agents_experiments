"""
Example-Driven Error Reporting (LALR)

A demonstration of example-driven error reporting with the LALR parser.
(See also: error_reporting_earley.py)

Converted from the Jupyter notebook: error_reporting_lalr.ipynb
This standalone script inlines the JSON grammar and shows how to classify
syntax errors into helpful, user-facing messages using Lark's
UnexpectedInput.match_examples.
"""

# ------------------------------
# Imports
# ------------------------------
from lark import Lark, UnexpectedInput


# ------------------------------
# JSON Grammar (inlined from the json_parser example)
# Kept as a raw triple-quoted string to preserve exact grammar syntax
# ------------------------------
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


# ------------------------------
# Parser construction (LALR)
# ------------------------------
json_parser = Lark(JSON_GRAMMAR, parser='lalr')


# ------------------------------
# Error classes with friendly messages
# ------------------------------
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


# ------------------------------
# Parsing with example-driven error classification
# ------------------------------

def parse(json_text):
    try:
        j = json_parser.parse(json_text)
        return j
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
            raise
        raise exc_class(u.get_context(json_text), u.line, u.column)


# ------------------------------
# Minimal tests (from the notebook)
# ------------------------------

def test():
    try:
        parse('{"example1": "value"')
    except JsonMissingClosing as e:
        print(e)

    try:
        parse('{"example2": ] ')
    except JsonMissingOpening as e:
        print(e)


# ------------------------------
# Main
# ------------------------------
if __name__ == '__main__':
    test()
