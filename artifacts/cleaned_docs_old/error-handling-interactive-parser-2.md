---
title: Error handling using an interactive parser (Lark)
source_url: https://lark-parser.readthedocs.io/en/stable/_downloads/3a11fd47a1fb670a6759747d618a244e/error_handling.py
description: Demonstrates handling UnexpectedToken errors with Lark’s LALR interactive parser by skipping or injecting tokens, then resuming parsing.
language: python
---

# Error handling using an interactive parser

This example demonstrates error handling using an interactive parser in LALR.

When the parser encounters an UnexpectedToken exception, it creates an interactive parser with the current parse state and lets you control how to proceed step-by-step. When you've achieved the correct parse state, you can resume the run by returning True.

```python
"""
Error handling using an interactive parser
==========================================

This example demonstrates error handling using an interactive parser in LALR

When the parser encounters an UnexpectedToken exception, it creates a
an interactive parser with the current parse-state, and lets you control how
to proceed step-by-step. When you've achieved the correct parse-state,
you can resume the run by returning True.
"""

from lark import Token

from _json_parser import json_parser

def ignore_errors(e):
    if e.token.type == 'COMMA':
        # Skip comma
        return True
    elif e.token.type == 'SIGNED_NUMBER':
        # Try to feed a comma and retry the number
        e.interactive_parser.feed_token(Token('COMMA', ','))
        e.interactive_parser.feed_token(e.token)
        return True

    # Unhandled error. Will stop parse and raise exception
    return False

def main():
    s = "[0 1, 2,, 3,,, 4, 5 6 ]"
    res = json_parser.parse(s, on_error=ignore_errors)
    print(res)      # prints [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

main()
```
