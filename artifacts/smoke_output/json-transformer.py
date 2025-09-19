---
title: JsonTreeToJson Transformer Module
description: Cleaned and typed Python module that defines a Lark Transformer to convert parse trees produced by json.lark into native Python objects.
source_url: null
---

```python
"""Transformer for evaluating json.lark

This module provides JsonTreeToJson, a Lark Transformer that converts
parse-tree nodes produced by a json.lark grammar into native Python
objects (str, float, list, dict, None, bool).
"""

from typing import Any

from lark import Transformer, v_args


class JsonTreeToJson(Transformer):
    """
    Transformer for evaluating json.lark parse trees into Python objects.

    Methods correspond to grammar rules:
    - string: unquote string tokens and unescape embedded quotes
    - array, pair, object, number, null, true, false: map to Python types
    """

    @v_args(inline=True)
    def string(self, s: str) -> str:
        # s is a quoted JSON string token, e.g. '"text"'
        # Remove surrounding quotes and unescape escaped double quotes.
        return s[1:-1].replace('\\"', '"')

    array = list
    pair = tuple
    object = dict
    # number is wrapped using v_args to produce an inline float conversion
    number = v_args(inline=True)(float)  # type: ignore

    def null(self, _: Any) -> None:
        return None

    def true(self, _: Any) -> bool:
        return True

    def false(self, _: Any) -> bool:
        return False
```
