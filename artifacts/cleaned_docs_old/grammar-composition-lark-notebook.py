#!/usr/bin/env python3
#
# Grammar Composition (Lark)
#
# This example shows how to compose grammars in Lark to create a file format
# that allows both CSV and JSON to co-exist.
#
# Overview
# - We define a grammar file `storage.lark` that imports both `csv.lark` and
#   `json.lark`, and allows them to be used one after the other.
#   In the generated parse tree, rules and terminals from imported grammars are
#   automatically prefixed (e.g., `json__` or `csv__`). This creates an implicit
#   namespace so that symbols from both grammars coexist without collisions.
#
# - We then merge their respective transformers (which are unaware of each other)
#   into a single base transformer using `merge_transformers`.
#   The methods of each transformer are renamed to the appropriate namespace
#   using the given prefix (e.g., `json__foo`, `csv__bar`). This enables full
#   reuse: each transformer can be written for its grammar alone, and still work
#   when imported or composed with others.
#
# Files expected alongside this script:
# - storage.lark            (imports csv.lark and json.lark)
# - csv.lark                (CSV grammar)
# - json.lark               (JSON grammar)
# - eval_csv.py             (exports class: CsvTreeToPandasDict)
# - eval_json.py            (exports class: JsonTreeToJson)
# - combined_csv_and_json.txt (sample input containing JSON followed by CSV)
#
# Runtime dependencies:
# - lark-parser
#
# This script parses two inputs:
# 1) A JSON-only string.
# 2) A combined file (`combined_csv_and_json.txt`) that contains JSON + CSV.

from pathlib import Path
from json import dumps

from lark import Lark
from lark.visitors import Transformer, merge_transformers

# Local transformers for the CSV and JSON grammars.
# Each should implement methods that match their grammar's rule names.
from eval_csv import CsvTreeToPandasDict
from eval_json import JsonTreeToJson

# Directory of this script (used for locating grammar and input files)
__dir__ = Path(__file__).parent


# Base transformer that receives the composed parse tree
# and simply returns the children as-is for the start rule.
class Storage(Transformer):
    def start(self, children):
        return children


# Merge transformers:
# - Prefix 'csv' maps methods to names like 'csv__*' to match imported CSV rules.
# - Prefix 'json' maps methods to names like 'json__*' to match imported JSON rules.
storage_transformer = merge_transformers(
    Storage(),
    csv=CsvTreeToPandasDict(),
    json=JsonTreeToJson(),
)

# Load the composed grammar. Lark will resolve `storage.lark` relative to this file.
parser = Lark.open("storage.lark", rel_to=__file__)


def main():
    # Example 1: Just JSON
    json_input = {"test": "a", "dict": {"list": [1, 1.2]}}
    json_tree = parser.parse(dumps(json_input))
    res = storage_transformer.transform(json_tree)
    print("Just JSON:", res)

    # Example 2: JSON + CSV combined in one file
    combined_path = __dir__ / "combined_csv_and_json.txt"
    with combined_path.open("r", encoding="utf-8") as f:
        csv_json_text = f.read()

    csv_json_tree = parser.parse(csv_json_text)
    res = storage_transformer.transform(csv_json_tree)
    print("JSON + CSV:")
    print(dumps(res, indent=2))


if __name__ == "__main__":
    main()
