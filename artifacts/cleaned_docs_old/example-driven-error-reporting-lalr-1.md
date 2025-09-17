---
title: Example-Driven Error Reporting (LALR)
description: Demonstrates example-driven error reporting with Lark's LALR parser by mapping UnexpectedInput to custom syntax errors using match_examples.
source_url: https://lark-parser.readthedocs.io/en/stable/_downloads/2cc75b757e7515472722c8c02d4fe4e4/error_reporting_lalr.py
language: python
---

# Example-Driven Error Reporting (LALR)

A demonstration of example-driven error reporting with the LALR parser.
See also: error_reporting_earley.py

```python
"""
Example-Driven Error Reporting
==============================

A demonstration of example-driven error reporting with the LALR parser
(See also: error_reporting_earley.py)
"""
from lark import Lark, UnexpectedInput

from _json_parser import json_grammar   # Using the grammar from the json_parser example

json_parser = Lark(json_grammar, parser='lalr')

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

def parse(json_text):
    try:
        j = json_parser.parse(json_text)
    except UnexpectedInput as u:
        exc_class = u.match_examples(
            json_parser.parse,
            {
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
            },
            use_accepts=True,
        )
        if not exc_class:
            raise
        raise exc_class(u.get_context(json_text), u.line, u.column)

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
```
