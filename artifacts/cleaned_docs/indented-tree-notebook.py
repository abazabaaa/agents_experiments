"""
Parsing Indentation

A demonstration of parsing indentation ("whitespace significant" language)
and the usage of the Indenter class.

Since indentation is context-sensitive, a postlex stage is introduced to
manufacture INDENT/DEDENT tokens.

It is crucial for the indenter that the NL_type matches
the spaces (and tabs) after the newline.
"""

# --- Imports ---
from lark import Lark
from lark.indenter import Indenter


# --- Grammar Definition ---
# Note:
# - The _NL token matches a newline followed by any spaces/tabs.
# - _INDENT and _DEDENT are declared and will be injected by the postlex Indenter.
TREE_GRAMMAR = r"""
    ?start: _NL* tree

    tree: NAME _NL [_INDENT tree+ _DEDENT]

    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE

    _NL: /(\r?\n[\t ]*)+/
"""


# --- Indentation Post-lexer (Indenter) ---
class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8


# --- Parser Instance ---
# LALR parser with a postlex stage that injects _INDENT/_DEDENT based on indentation.
parser = Lark(TREE_GRAMMAR, parser='lalr', postlex=TreeIndenter())


# --- Example Input ---
# An indented tree structure to demonstrate INDENT/DEDENT handling.
test_tree = """
a
    b
    c
        d
        e
    f
        g
"""


# --- Test Runner ---
def test():
    """Parse the example tree and print its pretty representation."""
    print(parser.parse(test_tree).pretty())


if __name__ == '__main__':
    test()
