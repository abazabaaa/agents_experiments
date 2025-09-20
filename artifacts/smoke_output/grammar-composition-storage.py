"""
Example: Grammar Composition with Lark

This module demonstrates how to compose grammars (CSV + JSON) and merge their
transformers into a single storage transformer that can handle both formats.

This script is a direct conversion of the provided notebook example.
"""

# Standard imports
from pathlib import Path
from lark import Lark, v_args
from json import dumps
from lark.visitors import Transformer, merge_transformers

# Local transformer imports (from the example)
from eval_csv import CsvTreeToPandasDict
from eval_json import JsonTreeToJson

# Directory of this file
__dir__ = Path(__file__).parent


class Storage(Transformer):
    def start(self, children):
        return children


# Merge the storage transformer with the CSV and JSON transformers,
# namespacing them as 'csv' and 'json' respectively (as in the example).
storage_transformer = merge_transformers(
    Storage(), csv=CsvTreeToPandasDict(), json=JsonTreeToJson()
)

# Load the composed grammar file. The example expects a 'storage.lark' file
# that imports the csv and json grammars.
parser = Lark.open("storage.lark", rel_to=__file__)


def main():
    # Parse a JSON string (using json.dumps to produce the source).
    json_tree = parser.parse(dumps({"test": "a", "dict": {"list": [1, 1.2]}}))
    res = storage_transformer.transform(json_tree)
    print("Just JSON: ", res)

    # Parse a combined CSV+JSON file (example file expected next to this script).
    combined_path = __dir__ / 'combined_csv_and_json.txt'
    csv_json_tree = parser.parse(combined_path.read_text())
    res = storage_transformer.transform(csv_json_tree)
    print("JSON + CSV: ", dumps(res, indent=2))


if __name__ == '__main__':
    main()
