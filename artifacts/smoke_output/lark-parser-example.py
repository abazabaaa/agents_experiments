'''Lark Grammar

A reference implementation of the Lark grammar (using LALR(1))

Converted from a Jupyter notebook. Original notebook metadata is preserved in
the comment below.

Original notebook metadata:
{
  "kernelspec": {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
  },
  "language_info": {
    "codemirror_mode": {
      "name": "ipython",
      "version": 3
    },
    "file_extension": ".py",
    "mimetype": "text/x-python",
    "name": "python",
    "nbconvert_exporter": "python",
    "pygments_lexer": "ipython3",
    "version": "3.7.17"
  },
  "nbformat": 4,
  "nbformat_minor": 0
}

This script preserves the original notebook structure as a linear Python
module. It demonstrates parsing the Lark grammar files using LALR(1).
'''

# Section: Imports (from original notebook code cell)
import json
from pathlib import Path
import lark
from lark import Lark, Transformer, v_args
import sys

# Section: Paths and parser initialization
# examples_path: directory containing this script
examples_path = Path(__file__).parent
# lark_path: directory containing the installed lark package
lark_path = Path(lark.__file__).parent

# Use Lark.open to load the lark grammar (handles 'import' directives, etc.).
# rel_to is set to this file so relative includes are resolved correctly.
parser = Lark.open(lark_path / 'grammars/lark.lark', rel_to=__file__, parser="lalr")

# Section: List of grammar files to parse (preserve original ordering)
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

# Section: Test function (parses each grammar file using the loaded parser)
def test():
    """Parse each grammar file using the loaded lark grammar parser.

    This uses Path.read_text() to safely read file contents (no explicit open/close
    required). Errors are reported with the filename for easier debugging.
    """
    for grammar_file in grammar_files:
        p = Path(grammar_file)
        try:
            text = p.read_text()
        except FileNotFoundError:
            print(f"File not found: {p!s}", file=sys.stderr)
            continue
        except Exception as e:
            print(f"Error reading {p!s}: {e}", file=sys.stderr)
            continue

        try:
            # Parse the grammar file contents using the previously opened parser
            tree = parser.parse(text)
        except Exception as e:
            print(f"Failed to parse {p!s}: {e}", file=sys.stderr)
            raise
        else:
            print(f"Parsed successfully: {p!s}")

    print("All available grammars parsed successfully")


if __name__ == '__main__':
    test()
