"""
Standalone Parser Example

This script is a conversion of a Jupyter notebook demonstrating the use of a
standalone Lark parser (pre-generated) for JSON. It preserves the original
Transformer class and usage from the notebook and provides a safe main guard.

Usage:
    python standalone_parser.py input.json

Notes:
- The original notebook imported a pre-generated standalone parser named
  Lark_StandAlone from a module called `json_parser`. This script keeps that
  import; ensure `json_parser.py` (the Lark-generated standalone parser file)
  is available on the PYTHONPATH.
- The Transformer and v_args used here are those provided by the standalone
  module (as in the original notebook). We also import Lark from the lark
  package in case you want to use the runtime parser directly.
"""

# Original notebook metadata (kept as comment):
# {"kernelspec": {"display_name": "Python 3","language": "python","name": "python3"}, "language_info": {"file_extension": ".py","name": "python","version": "3.7.17"}}

# ---------------------------------------------------------------------------
# Standalone Parser
#
# This example demonstrates how to generate and use the standalone parser,
# using the JSON example.
#
# See README.md for more details.
# ---------------------------------------------------------------------------

import sys

# The original notebook imported Lark_StandAlone, Transformer, and v_args
# from a module named `json_parser`. We preserve that import exactly so the
# behavior remains identical to the notebook. Ensure json_parser.py is present.
from json_parser import Lark_StandAlone, Transformer, v_args

# It's also useful to have the runtime Lark available; import it here if
# needed separately.
from lark import Lark  # optional: runtime parser if you want to re-create parser

# Preserve the decorator usage from the notebook
inline_args = v_args(inline=True)

class TreeToJson(Transformer):
    @inline_args
    def string(self, s):
        # The original notebook used slicing and replacement to unescape quotes
        return s[1:-1].replace('\\"', '"')

    # Keep the original method/attribute bindings exactly as in the notebook
    array = list
    pair = tuple
    object = dict
    number = inline_args(float)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


# Instantiate the pre-generated standalone parser with the Transformer
parser = Lark_StandAlone(transformer=TreeToJson())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python standalone_parser.py <input.json>', file=sys.stderr)
        sys.exit(2)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        data = f.read()
    # Print the parsed JSON structure (as produced by the Transformer)
    print(parser.parse(data))