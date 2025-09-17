# Parsing Indentation
#
# This script demonstrates how to parse indentation (a "whitespace-significant"
# language) using Lark's Indenter. Because indentation is context-sensitive, we
# use a post-lexing stage to manufacture INDENT/DEDENT tokens.
#
# Important: The Indenter relies on NL_type to match the spaces/tabs that follow
# a newline, so the _NL token below is defined to capture the newline along with
# the following indentation.
#
# Requires: pip install lark

from lark import Lark
from lark.indenter import Indenter

# Grammar for a simple indented tree language:
# - A tree is a NAME followed by a newline.
# - It may have an indented block with one or more nested trees.
# - We ignore inline whitespace, and declare the special INDENT/DEDENT tokens
#   that will be produced by the postlex Indenter.
# - _NL matches one or more newlines, including the spaces/tabs that follow
#   the newline, which the Indenter uses to compute indentation levels.
tree_grammar = r"""
    ?start: _NL* tree

    tree: NAME _NL [_INDENT tree+ _DEDENT]

    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE

    _NL: /(\r?\n[\t ]*)+/
"""

# Configure the Indenter to work with the tokens used by the grammar above.
class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

# Build the parser using LALR with the post-lexing Indenter stage.
parser = Lark(tree_grammar, parser='lalr', postlex=TreeIndenter())

# Example input: a simple indented tree structure
# a
# ├── b
# └── c
#     ├── d
#     └── e
# └── f
#     └── g
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
    # Parse and pretty-print the resulting tree
    print(parser.parse(test_tree).pretty())


if __name__ == '__main__':
    test()
