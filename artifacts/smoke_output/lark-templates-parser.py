"""
Lark Templates Example

This script is a converted and cleaned-up version of a Jupyter notebook demonstrating
Lark "templates" usage for cleaner grammars.

Notes on conversion:
- Markdown cells converted to comment blocks
- Code cells preserved and organized into logical sections
- Minor typos fixed (e.g. _seperated -> _separated)
- Imports include commonly used Lark helpers for completeness

The grammar is kept as a module-level constant using a raw triple-quoted string,
so grammar syntax is preserved verbatim (aside from the typo fix).
"""

# Standard imports
from lark import Lark, Transformer, v_args


# -----------------------------------------------------------------------------
# Templates
#
# This example shows how to use Lark's templates to achieve cleaner grammars
# -----------------------------------------------------------------------------

GRAMMAR = r'''
start: list | dict

list: "[" _separated{atom, ","} "]"
dict: "{" _separated{key_value, ","} "}"
key_value: atom ":" atom

_separated{x, sep}: x (sep x)*  // Define a sequence of 'x sep x sep x ...'

atom: NUMBER | ESCAPED_STRING

%import common (NUMBER, ESCAPED_STRING, WS)
%ignore WS
'''


# -----------------------------------------------------------------------------
# Main execution
# -----------------------------------------------------------------------------

def main():
    """Create a parser from the grammar and run a few example parses."""
    parser = Lark(GRAMMAR)

    # Example inputs from the original notebook
    examples = [
        '[1, "a", 2]',
        '{"a": 2, "b": 6}'
    ]

    for ex in examples:
        print('Input :', ex)
        print('Parse :', parser.parse(ex))
        print()


if __name__ == '__main__':
    main()
