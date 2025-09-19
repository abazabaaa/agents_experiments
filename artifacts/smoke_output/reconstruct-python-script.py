"""
Reconstruct Python

Demonstrates how Lark's experimental text-reconstruction feature can recreate
functional Python code from its parse-tree, using just the correct grammar and
a small formatter.

This module is a converted version of a Jupyter notebook. The original notebook
metadata and cell contents are preserved in the header comment below for
traceability.
"""

# ---------------------------------------------------------------------------
# Original notebook metadata and cells (for traceability)
# ---------------------------------------------------------------------------
# {
#   "cells": [
#     {
#       "cell_type": "markdown",
#       "metadata": {},
#       "source": [
#         "\n# Reconstruct Python\n\nDemonstrates how Lark's experimental text-reconstruction feature can recreate\nfunctional Python code from its parse-tree, using just the correct grammar and\na small formatter.\n"
#       ]
#     },
#     {
#       "cell_type": "code",
#       "execution_count": null,
#       "metadata": {
#         "collapsed": false
#       },
#       "outputs": [],
#       "source": [
#         "from lark import Token, Lark\nfrom lark.reconstruct import Reconstructor\nfrom lark.indenter import PythonIndenter\n\n# Official Python grammar by Lark\npython_parser3 = Lark.open_from_package('lark', 'python.lark', ['grammars'],\n                                        parser='lalr', postlex=PythonIndenter(), start='file_input',\n                                        maybe_placeholders=False    # Necessary for reconstructor\n                                        )\n\nSPACE_AFTER = set(',+-*/~@<>=\"|:')\nSPACE_BEFORE = (SPACE_AFTER - set(',:')) | set('\\\'')\n\n\ndef special(sym):\n    return Token('SPECIAL', sym.name)\n\ndef postproc(items):\n    stack = ['\\n']\n    actions = []\n    last_was_whitespace = True\n    for item in items:\n        if isinstance(item, Token) and item.type == 'SPECIAL':\n            actions.append(item.value)\n        else:\n            if actions:\n                assert actions[0] == '_NEWLINE' and '_NEWLINE' not in actions[1:], actions\n\n                for a in actions[1:]:\n                    if a == '_INDENT':\n                        stack.append(stack[-1] + ' ' * 4)\n                    else:\n                        assert a == '_DEDENT'\n                        stack.pop()\n                actions.clear()\n                yield stack[-1]\n                last_was_whitespace = True\n            if not last_was_whitespace:\n                if item[0] in SPACE_BEFORE:\n                    yield ' '\n            yield item\n            last_was_whitespace = item[-1].isspace()\n            if not last_was_whitespace:\n                if item[-1] in SPACE_AFTER:\n                    yield ' '\n                    last_was_whitespace = True\n    yield \"\\n\"\n\n\nclass PythonReconstructor:\n    def __init__(self, parser):\n        self._recons = Reconstructor(parser, {'_NEWLINE': special, '_DEDENT': special, '_INDENT': special})\n\n    def reconstruct(self, tree):\n        return self._recons.reconstruct(tree, postproc)\n\n\ndef test():\n    python_reconstructor = PythonReconstructor(python_parser3)\n\n    self_contents = open(__file__).read()\n\n    tree = python_parser3.parse(self_contents+'\\n')\n    output = python_reconstructor.reconstruct(tree)\n\n    tree_new = python_parser3.parse(output)\n    print(tree.pretty())\n    print(tree_new.pretty())\n    # assert tree.pretty() == tree_new.pretty()\n    assert tree == tree_new\n\n    print(output)\n\n\nif __name__ == '__main__':\n    test()"
#       ]
#     }
#   ],
#   "metadata": {
#     "kernelspec": {
#       "display_name": "Python 3",
#       "language": "python",
#       "name": "python3"
#     },
#     "language_info": {
#       "codemirror_mode": {
#         "name": "ipython",
#         "version": 3
#       },
#       "file_extension": ".py",
#       "mimetype": "text/x-python",
#       "name": "python",
#       "nbconvert_exporter": "python",
#       "pygments_lexer": "ipython3",
#       "version": "3.7.17"
#     }
#   },
#   "nbformat": 4,
#   "nbformat_minor": 0
# }
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Section: Imports
# ---------------------------------------------------------------------------
from lark import Token, Lark, Transformer, v_args
from lark.reconstruct import Reconstructor
from lark.indenter import PythonIndenter

# ---------------------------------------------------------------------------
# Section: Parser initialization
# ---------------------------------------------------------------------------
# Official Python grammar provided by the installed 'lark' package. We load it
# via Lark.open_from_package to use the bundled 'python.lark' grammar and the
# PythonIndenter postlex which is required for parsing indentation-sensitive
# Python source.
python_parser3 = Lark.open_from_package(
    'lark',
    'python.lark',
    ['grammars'],
    parser='lalr',
    postlex=PythonIndenter(),
    start='file_input',
    maybe_placeholders=False,  # Necessary for reconstructor
)

# ---------------------------------------------------------------------------
# Section: Formatting helpers
# ---------------------------------------------------------------------------
# Characters that should be followed / preceded by spaces when reconstructing
SPACE_AFTER = set(',+-*/~@<>="|:')
# Include single-quote as a character that may need a preceding space
SPACE_BEFORE = (SPACE_AFTER - set(',:')) | set("'")


def special(sym):
    """Convert a special placeholder token (like _INDENT) to a Token used
    by the Reconstructor post-processing step."""
    return Token('SPECIAL', sym.name)


def postproc(items):
    """Post-process the sequence of tokens/items produced by the
    reconstructor to inject actual whitespace/indentation strings.

    The reconstructor yields placeholders for newline/indent/dedent which we
    convert into actual strings using a stack-based indentation tracker.
    """
    stack = ['\n']
    actions = []
    last_was_whitespace = True
    for item in items:
        if isinstance(item, Token) and item.type == 'SPECIAL':
            actions.append(item.value)
        else:
            if actions:
                # The first special should be _NEWLINE. Subsequent specials are
                # INDENT/DEDENT markers.
                assert actions[0] == '_NEWLINE' and '_NEWLINE' not in actions[1:], actions

                for a in actions[1:]:
                    if a == '_INDENT':
                        stack.append(stack[-1] + ' ' * 4)
                    else:
                        assert a == '_DEDENT'
                        stack.pop()
                actions.clear()
                yield stack[-1]
                last_was_whitespace = True
            if not last_was_whitespace:
                if item[0] in SPACE_BEFORE:
                    yield ' '
            yield item
            last_was_whitespace = item[-1].isspace()
            if not last_was_whitespace:
                if item[-1] in SPACE_AFTER:
                    yield ' '
                    last_was_whitespace = True
    yield "\n"


# ---------------------------------------------------------------------------
# Section: Reconstructor wrapper
# ---------------------------------------------------------------------------
class PythonReconstructor:
    """Wrapper around Lark's Reconstructor for Python source.

    It maps the placeholder names (_NEWLINE/_INDENT/_DEDENT) to the special
    Token objects handled by the postproc function above.
    """

    def __init__(self, parser):
        self._recons = Reconstructor(
            parser,
            {'_NEWLINE': special, '_DEDENT': special, '_INDENT': special},
        )

    def reconstruct(self, tree):
        return self._recons.reconstruct(tree, postproc)


# ---------------------------------------------------------------------------
# Section: Test / Example usage
# ---------------------------------------------------------------------------
def test():
    """Parse this file and attempt to reconstruct it from the parse-tree.

    The test reads the current file (__file__), parses it with the python
    grammar, reconstructs source from the tree, and parses the reconstructed
    source again to check round-trip fidelity.
    """
    python_reconstructor = PythonReconstructor(python_parser3)

    # Read the current source
    self_contents = open(__file__).read()

    # Parse and reconstruct
    tree = python_parser3.parse(self_contents + '\n')
    output = python_reconstructor.reconstruct(tree)

    # Parse the reconstructed output to ensure it yields the same tree
    tree_new = python_parser3.parse(output)
    print(tree.pretty())
    print(tree_new.pretty())
    # The pretty representations are not guaranteed identical across all
    # grammar/provider combos, so compare the trees directly.
    assert tree == tree_new

    # Emit the reconstructed source (for inspection)
    print(output)


if __name__ == '__main__':
    test()
