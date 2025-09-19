"""
Parsing Indentation

A demonstration of parsing indentation ("whitespace significant" language)
and the usage of the Indenter class.

Since indentation is context-sensitive, a postlex stage is introduced to
manufacture INDENT/DEDENT tokens.

It is crucial for the indenter that the NL_type matches
the spaces (and tabs) after the newline.

This script is a transformation of a Jupyter notebook example into a
standalone Python module. Reviewer feedback was applied: fixed the
_regex in the tree_grammar's _NL rule by removing an extraneous escaped slash.

Reviewer feedback (preserved here as a comment):
# Grammar regex syntax error in tree_grammar: the _NL rule ended with an
# unexpected escaped slash ("_NL: /(\r?\n[\t ]*)+\/"), which would make
# the Lark grammar invalid. This has been corrected to
# "_NL: /(\r?\n[\t ]*)+/".
"""

# Section: Imports
from lark import Lark, Transformer, v_args
from lark.indenter import Indenter

# Section: Example: Parsing Indentation using Lark and Indenter

# Grammar definition (preserved as a raw triple-quoted string)
# Note: The _NL regex was corrected per reviewer feedback (removed trailing \\). 
# Preserve all other grammar content and directives exactly.
tree_grammar = r'''
    ?start: _NL* tree

    tree: NAME _NL [_INDENT tree+ _DEDENT]

    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE

    _NL: /(\r?\n[\t ]*)+/
'''


class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8


# Create the parser with the Indenter as postlex stage
parser = Lark(tree_grammar, parser='lalr', postlex=TreeIndenter())

# Test input (preserved from the original notebook)
test_tree = """
a
    b
    c
        d
        e
    f
        g
"""


def test():
    # Parse and print a pretty representation of the parse tree
    print(parser.parse(test_tree).pretty())


if __name__ == '__main__':
    test()
