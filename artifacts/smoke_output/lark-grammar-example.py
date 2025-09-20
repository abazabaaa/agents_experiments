r'''Lark Grammar example

Reference implementation of the Lark grammar (using LALR(1)).

This script parses a collection of grammar files using the Lark grammar
(including lark.lark from the installed lark package) to ensure they
parse successfully.
'''

# Standard imports
import lark
from lark import Lark, Transformer, v_args
from pathlib import Path

# (No explicit grammar constants in this example)

@v_args(inline=True)  # Preserve decorator exactly as required
class ExampleTransformer(Transformer):
    """Placeholder transformer used as an example.

    Implement transformation methods here if needed.
    """
    pass


# Paths and parser setup
examples_path = Path(__file__).parent
lark_path = Path(lark.__file__).parent

parser = Lark.open(lark_path / 'grammars/lark.lark', rel_to=__file__, parser="lalr")

grammar_files = [
    examples_path / 'advanced/python2.lark',
    examples_path / 'relative-imports/multiples.lark',
    examples_path / 'relative-imports/multiple2.lark',
    examples_path / 'relative-imports/multiple3.lark',
    examples_path / 'tests/no_newline_at_end.lark',
    examples_path / 'tests/negative_priority.lark',
    examples_path / 'standalone/json.lark',
    lark_path / 'grammars/common.lark',
    lark_path / 'grammars/lark.lark',
    lark_path / 'grammars/unicode.lark',
    lark_path / 'grammars/python.lark',
]


def test():
    for grammar_file in grammar_files:
        # Read the grammar file content and parse it
        content = open(grammar_file).read()
        tree = parser.parse(content)
    print('All grammars parsed successfully')


if __name__ == '__main__':
    test()
