"""
Lark example: Grammar Composition

This module demonstrates composing multiple grammars (CSV and JSON) into a
single "storage" format and merging their Transformers so the resulting
transformer can evaluate both JSON and CSV in the combined parse tree.
"""

# Standard imports
from pathlib import Path
from json import dumps
from lark import Lark, v_args
from lark.visitors import Transformer, merge_transformers

# Local transformer classes (expected to be provided alongside this module)
from eval_csv import CsvTreeToPandasDict
from eval_json import JsonTreeToJson

# Directory of this file
__dir__ = Path(__file__).parent

# Simple wrapper transformer for the composed grammar
class Storage(Transformer):
    def start(self, children):
        return children

# Merge the separate transformers into a single transformer with namespaces
storage_transformer = merge_transformers(
    Storage(),
    csv=CsvTreeToPandasDict(),
    json=JsonTreeToJson(),
)

# Load the composed grammar (storage.lark should import csv.lark and json.lark)
parser = Lark.open("storage.lark", rel_to=__file__)


def main():
    # Parse a plain JSON input
    json_tree = parser.parse(dumps({"test": "a", "dict": {"list": [1, 1.2]}}))
    res = storage_transformer.transform(json_tree)
    print("Just JSON: ", res)

    # Parse a combined CSV+JSON example file
    csv_json_tree = parser.parse(open(__dir__ / 'combined_csv_and_json.txt').read())
    res = storage_transformer.transform(csv_json_tree)
    print("JSON + CSV: ", dumps(res, indent=2))


if __name__ == '__main__':
    main()
