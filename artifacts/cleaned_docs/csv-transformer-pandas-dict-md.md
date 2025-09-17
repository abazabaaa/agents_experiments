---
title: CsvTreeToPandasDict Transformer for CSV evaluation
description: Python Transformer that converts parse trees from csv.lark into a dictionary suitable for use with Pandas.
source_url: https://lark-parser.readthedocs.io/en/stable/_downloads/47174f1088585b541b7296c461639c79/eval_csv.py
---

# CsvTreeToPandasDict Transformer

The following Python module defines a Lark Transformer that evaluates parse trees produced by csv.lark and converts them into a dictionary keyed by CSV header names.

```python
"Transformer for evaluating csv.lark"

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
