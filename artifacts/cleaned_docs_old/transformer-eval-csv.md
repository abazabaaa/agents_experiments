---
title: Transformer for evaluating csv.lark
source_url: https://lark-parser.readthedocs.io/en/stable/examples/composition/eval_csv.html
description: Example Transformer that converts a parsed CSV tree (from csv.lark) into a pandas-friendly dictionary structure.
related:
  - https://lark-parser.readthedocs.io/en/stable/examples/composition/index.html
  - https://lark-parser.readthedocs.io/en/stable/examples/composition/eval_json.html
  - https://lark-parser.readthedocs.io/en/stable/examples/composition/main.html
resources:
  python_source: https://lark-parser.readthedocs.io/en/stable/_downloads/47174f1088585b541b7296c461639c79/eval_csv.py
  notebook: https://lark-parser.readthedocs.io/en/stable/_downloads/de026e34f2e30342f31740044e683d7b/eval_csv.ipynb
---

# Transformer for evaluating csv.lark

This example shows a Lark Transformer that converts the parse tree produced by `csv.lark` into a dictionary of columns suitable for constructing a pandas DataFrame.

## Code

```python
from lark import Transformer

class CsvTreeToPandasDict(Transformer):
    INT = int
    FLOAT = float
    SIGNED_FLOAT = float
    WORD = str
    NON_SEPARATOR_STRING = str

    def row(self, children):
        return children

    def start(self, children):
        data = {}

        header = children[0].children
        for heading in header:
            data[heading] = []

        for row in children[1:]:
            for i, element in enumerate(row):
                data[header[i]].append(element)

        return data
```

## Downloads

- Download Python source code: https://lark-parser.readthedocs.io/en/stable/_downloads/47174f1088585b541b7296c461639c79/eval_csv.py
- Download Jupyter notebook: https://lark-parser.readthedocs.io/en/stable/_downloads/de026e34f2e30342f31740044e683d7b/eval_csv.ipynb

Generated with Sphinx-Gallery: https://sphinx-gallery.github.io/
