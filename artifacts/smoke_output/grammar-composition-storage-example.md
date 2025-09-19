---
title: "Grammar Composition (Lark) — Storage Example"
description: "Example showing grammar composition in Lark: combining CSV and JSON grammars, merging transformers, and parsing combined files. Preserves original code and paths; demonstrates how to use Lark.open with rel_to and merge_transformers to combine separate grammar evaluators."
source_url: "N/A"
---

# Grammar Composition

This example shows how to do grammar composition in Lark, by creating a new
file format that allows both CSV and JSON to co-exist.

1) We define `storage.lark`, which imports both `csv.lark` and `json.lark`,
   and allows them to be used one after the other.

   In the generated tree, each imported rule/terminal is automatically prefixed (with ``json__`` or ``csv__``),
   which creates an implicit namespace and allows them to coexist without collisions.

2) We merge their respective transformers (unaware of each other) into a new base transformer.
   The resulting transformer can evaluate both JSON and CSV in the parse tree.

   The methods of each transformer are renamed into their appropriate namespace, using the given prefix.
   This approach allows full re-use: the transformers don't need to care if their grammar is used directly,
   or being imported, or who is doing the importing.

## Files required (relative to this script)

- storage.lark (grammar file) — opened with Lark.open(..., rel_to=__file__)
- combined_csv_and_json.txt (sample file containing CSV + JSON sequences)
- eval_csv.py (provides CsvTreeToPandasDict)
- eval_json.py (provides JsonTreeToJson)

Ensure these files are located in the same directory as this script, or adjust paths accordingly.

## Notes on relative paths

- The grammar `storage.lark` is loaded via `Lark.open("storage.lark", rel_to=__file__)`, which resolves the grammar path relative to the script file.
- The sample input `combined_csv_and_json.txt` is read using `__dir__ / 'combined_csv_and_json.txt'`, where `__dir__ = Path(__file__).parent`.

## Python script (preserved exactly)

```python
"""
Grammar Composition
===================

This example shows how to do grammar composition in Lark, by creating a new
file format that allows both CSV and JSON to co-exist.

1) We define ``storage.lark``, which imports both ``csv.lark`` and ``json.lark``,
  and allows them to be used one after the other.

  In the generated tree, each imported rule/terminal is automatically prefixed (with ``json__`` or ``csv__),
  which creates an implicit namespace and allows them to coexist without collisions.

2) We merge their respective transformers (unaware of each other) into a new base transformer.
   The resulting transformer can evaluate both JSON and CSV in the parse tree.

  The methods of each transformer are renamed into their appropriate namespace, using the given prefix.
  This approach allows full re-use: the transformers don't need to care if their grammar is used directly,
  or being imported, or who is doing the importing.

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

storage_transformer = merge_transformers(Storage(), csv=CsvTreeToPandasDict(), json=JsonTreeToJson())

parser = Lark.open("storage.lark", rel_to=__file__)

def main():
    json_tree = parser.parse(dumps({"test": "a", "dict": { "list": [1, 1.2] }}))
    res = storage_transformer.transform(json_tree)
    print("Just JSON: ", res)

    csv_json_tree = parser.parse(open(__dir__ / 'combined_csv_and_json.txt').read())
    res = storage_transformer.transform(csv_json_tree)
    print("JSON + CSV: ", dumps(res, indent=2))

if __name__ == "__main__":
    main()
```

## How to run

1. Install dependencies (if not already):
   - pip install lark-parser
2. Place `storage.lark`, `combined_csv_and_json.txt`, `eval_csv.py`, and `eval_json.py` in the same directory as this script.
3. Run the script with Python (it uses __file__ to resolve relative paths):
   - python path/to/this_script.py

Note: This markdown preserves the original behavior and paths. It does not execute any code.
