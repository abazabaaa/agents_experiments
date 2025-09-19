"""
Example-Driven Error Reporting

A demonstration of example-driven error reporting with the Earley parser
(See also: error_reporting_lalr.py)

This file was converted from a Jupyter notebook. Markdown cells were
preserved as module documentation and section comments. Code cells were
kept in their original order and logic. The JSON grammar is imported
from the example module `_json_parser` (so that module must be available
on PYTHONPATH for this script to run).
"""

# Imports
from lark import Lark, UnexpectedInput, Transformer, v_args

# Using the grammar from the json_parser example
from _json_parser import json_grammar

# Build the parser
json_parser = Lark(json_grammar)


# Exception classes for example-driven error reporting
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


# Parse function that uses example-driven error matching
def parse(json_text):
    try:
        j = json_parser.parse(json_text)
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


# Simple tests reproduced from the notebook
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
