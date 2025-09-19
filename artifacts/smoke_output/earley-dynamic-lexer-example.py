# Reviewer feedback applied:
# - Fix regex token patterns by moving quantifiers inside delimiters (NAME: /\w+/ and VALUE: /.+/).
# - Separate inline comments with spacing.
# - Preserve the rest of the content.
#
# Original notebook JSON (for provenance):
# {...}

"""
Earley's dynamic lexer example converted from a Jupyter notebook to a
standalone Python script demonstrating a simple INI-like parser using Lark.

This script preserves the original Lark grammar as a module-level raw
triple-quoted string, keeps grammar syntax exact, and retains test cases.
"""

# Section: Imports
from lark import Lark, Transformer, v_args

# Section: Grammar definition
GRAMMAR = r'''
start: _NL? section+
section: "[" NAME "]" _NL item+
item: NAME "=" VALUE? _NL

NAME: /\w+/  # token for names
VALUE: /.+/  # token for values (at least one char)

%import common.NEWLINE -> _NL
%import common.WS_INLINE
%ignore WS_INLINE
'''

# Section: Parser instantiation
parser = Lark(GRAMMAR, parser="earley")

# Section: (Optional) Transformer / Visitor placeholders
# The original notebook did not include Transformer/Visitor classes, but
# imports are preserved above. If you want to transform the parse tree,
# define Transformer/Visitor classes here and use parser.parse with
# transformer=YourTransformer() as needed.

# Section: Tests / Example usage
def test():
    sample_conf = """
[bla]

a=Hello
this="that",4
empty=
"""

    tree = parser.parse(sample_conf)
    print(tree.pretty())

if __name__ == '__main__':
    test()
