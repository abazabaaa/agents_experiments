---
title: CsvTreeToPandasDict Transformer
description: Cleaned and PEP8-compliant Transformer for converting a Lark parse tree (from csv.lark) into a dictionary suitable for pandas.
source_url: "csv.lark Transformer snippet (original source not provided)"
---

# CsvTreeToPandasDict Transformer

This module provides a small Lark Transformer that converts a parsed CSV tree (from csv.lark) into a dictionary keyed by column headers, where each value is a list of column values. The original semantics are preserved.

```python
"""Transformer for evaluating csv.lark.

This module contains a Transformer subclass that maps token types to Python types
and converts a parsed CSV tree into a dictionary of columns suitable for
constructing a pandas.DataFrame.
"""

from typing import Any, Dict, List

from lark import Transformer


class CsvTreeToPandasDict(Transformer):
    """Transformer that converts a CSV parse tree into a dict of columns.

    Token-to-type mappings are kept as class attributes to allow Lark to apply
    automatic type conversion when building the tree.
    """

    INT = int
    FLOAT = float
    SIGNED_FLOAT = float
    WORD = str
    NON_SEPARATOR_STRING = str

    def row(self, children: List[Any]) -> List[Any]:
        """Return a row as a list of values.

        The `children` argument is the list of parsed elements for the row.
        """
        return children

    def start(self, children: List[Any]) -> Dict[str, List[Any]]:
        """Convert parsed header + rows into a dict of columns.

        The first element of `children` is expected to be the header (a Tree
        whose `.children` attribute contains the column names). The remaining
        elements are rows (lists of values).
        """
        data: Dict[str, List[Any]] = {}

        header: List[str] = [str(h) for h in children[0].children]
        for heading in header:
            data[heading] = []

        for row in children[1:]:
            if len(row) != len(header):
                raise ValueError(f"Row length {len(row)} != header length {len(header)}")
            for i, element in enumerate(row):
                data[header[i]].append(element)

        return data
```
