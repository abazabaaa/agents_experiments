"""
Example: Grammar composition in Lark.

This example shows how to do grammar composition in Lark, by creating a new
file format that allows both CSV and JSON to co-exist.

1) It expects a "storage.lark" grammar that imports both "csv.lark" and
   "json.lark", allowing them to be used one after the other.

2) The transformers for each imported grammar are merged into a single
   transformer, using prefixes (csv=..., json=...) so their methods live
   in separate namespaces and don't collide.
"""

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

storage_transformer = merge_transformers(
    Storage(),
    csv=CsvTreeToPandasDict(),
    json=JsonTreeToJson(),
)

parser = Lark.open("storage.lark", rel_to=__file__)

def main():
    # Parse a JSON string (using json.dumps) and transform it
    json_tree = parser.parse(dumps({"test": "a", "dict": { "list": [1, 1.2] }}))
    res = storage_transformer.transform(json_tree)
    print("Just JSON: ", res)

    # Parse a combined CSV+JSON text file and transform it
    csv_path = __dir__ / 'combined_csv_and_json.txt'
    csv_text = open(csv_path).read()
    csv_json_tree = parser.parse(csv_text)
    res = storage_transformer.transform(csv_json_tree)
    print("JSON + CSV: ", dumps(res, indent=2))


if __name__ == '__main__':
    main()
