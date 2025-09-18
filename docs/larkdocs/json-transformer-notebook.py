"""
Lark example: Evaluate JSON using a Transformer

This script is adapted from the notebook "Transformer for evaluating json.lark".
It demonstrates how to:
- define a JSON grammar in Lark
- use a Transformer to convert the parse tree into native Python values

The Transformer implementation is preserved from the notebook cell.
"""

# Imports
from lark import Lark, Transformer, v_args


# ---------------------------------------------------------------------------
# Grammar definition (equivalent to json.lark)
# ---------------------------------------------------------------------------
JSON_GRAMMAR = r'''
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


# ---------------------------------------------------------------------------
# Notebook markdown cell:
#   "Transformer for evaluating json.lark"
# (Converted to a section comment.)
# ---------------------------------------------------------------------------
class JsonTreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        # Keep the exact behavior from the notebook: strip quotes and unescape \"
        return s[1:-1].replace('\\"', '"')

    # Map parse tree nodes directly to Python types/constructors
    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

    # Terminals converted to Python primitives
    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


# ---------------------------------------------------------------------------
# Helper: Build the Lark parser for the JSON grammar
# ---------------------------------------------------------------------------
def build_parser():
    return Lark(JSON_GRAMMAR, start='value', parser='lalr')


def parse_and_eval(text, parser=None, transformer=None):
    parser = parser or build_parser()
    transformer = transformer or JsonTreeToJson()
    tree = parser.parse(text)
    return transformer.transform(tree)


# ---------------------------------------------------------------------------
# Main demonstration and simple tests
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    parser = build_parser()
    transformer = JsonTreeToJson()

    # Example inputs to demonstrate functionality
    examples = [
        'null',
        'true',
        'false',
        '"Hello, world!"',
        '"He said: \\"hi\\""',
        '[]',
        '{}',
        '[1, 2, 3.5, null, true, false]',
        '{"a": 1, "b": [2, 3, 4], "c": false, "d": null, "e": "x"}',
        '[ {"k": "v"}, 123, true, null, ["x", "y"] ]',
    ]

    print('--- Demonstration ---')
    for text in examples:
        result = transformer.transform(parser.parse(text))
        print(f'Input:  {text}')
        print(f'Result: {result}')
        print('---')

    # Simple correctness checks (note: numbers become float per the Transformer)
    tests = [
        ('null', None),
        ('true', True),
        ('false', False),
        ('"x"', 'x'),
        ('1', 1.0),
        ('3.5', 3.5),
        ('[]', []),
        ('{}', {}),
        ('[1,2,"a"]', [1.0, 2.0, 'a']),
        ('{"a": 1, "b": "c"}', {'a': 1.0, 'b': 'c'}),
        ('"He said: \\"hi\\""', 'He said: "hi"'),
    ]

    for text, expected in tests:
        got = parse_and_eval(text, parser, transformer)
        assert got == expected, f'Expected {expected!r}, got {got!r} for {text!r}'

    print('All tests passed.')
