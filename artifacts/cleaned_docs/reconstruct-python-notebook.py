"""
Reconstruct Python

Demonstrates how Lark's experimental text-reconstruction feature can recreate
functional Python code from its parse-tree, using just the correct grammar and
a small formatter.

This script loads Lark's official Python grammar, parses its own source,
reconstructs the text using Reconstructor plus a lightweight post-processor
that handles indentation and spacing, and verifies that the parse trees before
and after reconstruction are identical.
"""

# --- Imports ---
from lark import Token, Lark
from lark.reconstruct import Reconstructor
from lark.indenter import PythonIndenter


# --- Build the official Python parser from Lark's packaged grammar ---
# Using the LALR parser with PythonIndenter to emit _INDENT/_DEDENT tokens.
# maybe_placeholders=False is necessary for Reconstructor to function properly.
python_parser3 = Lark.open_from_package(
    'lark',
    'python.lark',
    ['grammars'],
    parser='lalr',
    postlex=PythonIndenter(),
    start='file_input',
    maybe_placeholders=False  # Necessary for reconstructor
)


# --- Whitespace/spacing configuration for the post-processor ---
# Insert spaces around certain punctuation to produce readable Python code.
SPACE_AFTER = set(',+-*/~@<>="|:')
SPACE_BEFORE = (SPACE_AFTER - set(',:')) | set("'")


def special(sym):
    """Wrap special indentation/newline symbols as Token('SPECIAL', name)."""
    return Token('SPECIAL', sym.name)


# --- Reconstructor post-processor ---
# Handles emitted items from Reconstructor, applying indentation actions and
# inserting spaces where needed to recreate well-formatted Python source.

def postproc(items):
    stack = ['\n']  # Tracks current indentation prefix; start with a newline
    actions = []
    last_was_whitespace = True
    for item in items:
        if isinstance(item, Token) and item.type == 'SPECIAL':
            actions.append(item.value)
        else:
            if actions:
                # We expect a _NEWLINE followed by zero or more { _INDENT | _DEDENT }
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


# --- Convenience wrapper around Lark's Reconstructor ---
class PythonReconstructor:
    def __init__(self, parser):
        # Map indentation/newline terminals to our special handler
        self._recons = Reconstructor(parser, {
            '_NEWLINE': special,
            '_DEDENT': special,
            '_INDENT': special,
        })

    def reconstruct(self, tree):
        return self._recons.reconstruct(tree, postproc)


# --- Self-test: parse and reconstruct this very file ---
# Parses the current file, reconstructs its text, then re-parses and verifies
# the trees are identical. Prints both trees and the reconstructed output.

def test():
    python_reconstructor = PythonReconstructor(python_parser3)

    self_contents = open(__file__).read()

    tree = python_parser3.parse(self_contents + '\n')
    output = python_reconstructor.reconstruct(tree)

    tree_new = python_parser3.parse(output)
    print(tree.pretty())
    print(tree_new.pretty())
    # assert tree.pretty() == tree_new.pretty()
    assert tree == tree_new

    print(output)


if __name__ == '__main__':
    test()
