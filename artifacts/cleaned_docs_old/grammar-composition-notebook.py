# Grammar Composition
#
# This example shows how to do grammar composition in Lark, by creating a new
# file format that allows both CSV and JSON to co-exist.
#
# 1) We define a grammar file "storage.lark", which imports both "csv.lark" and
#    "json.lark", and allows them to be used one after the other.
#
#    In the generated tree, each imported rule/terminal is automatically
#    prefixed (with "json__" or "csv__"), which creates an implicit namespace
#    and allows them to coexist without collisions.
#
# 2) We merge their respective transformers (unaware of each other) into a new
#    base transformer. The resulting transformer can evaluate both JSON and CSV
#    in the parse tree.
#
#    The methods of each transformer are renamed into their appropriate
#    namespace, using the given prefix. This approach allows full re-use: the
#    transformers don't need to care if their grammar is used directly, or
#    being imported, or who is doing the importing.
#
# Note: This script expects the following files/modules alongside it:
#   - storage.lark (which imports csv.lark and json.lark)
#   - eval_csv.py defining CsvTreeToPandasDict
#   - eval_json.py defining JsonTreeToJson
#   - combined_csv_and_json.txt (example input combining CSV and JSON)

from pathlib import Path
from lark import Lark
from json import dumps
from lark.visitors import Transformer, merge_transformers

from eval_csv import CsvTreeToPandasDict
from eval_json import JsonTreeToJson

__dir__ = Path(__file__).parent

class Storage(Transformer):
    def start(self, children):
        return children

# Merge independent transformers under separate namespaces, matching the
# prefixes introduced by the imported grammars inside storage.lark
storage_transformer = merge_transformers(
    Storage(),
    csv=CsvTreeToPandasDict(),
    json=JsonTreeToJson(),
)

# Load the composed grammar which imports json.lark and csv.lark
parser = Lark.open("storage.lark", rel_to=__file__)

def main():
    # Parse a pure JSON input and evaluate it via the merged transformer
    json_tree = parser.parse(dumps({"test": "a", "dict": {"list": [1, 1.2]}}))
    res = storage_transformer.transform(json_tree)
    print("Just JSON: ", res)

    # Parse a combined CSV + JSON input and evaluate it
    csv_json_text = open(__dir__ / "combined_csv_and_json.txt").read()
    csv_json_tree = parser.parse(csv_json_text)
    res = storage_transformer.transform(csv_json_tree)
    print("JSON + CSV: ", dumps(res, indent=2))


if __name__ == "__main__":
    main()
