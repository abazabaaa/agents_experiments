#!/usr/bin/env python3
# Templates
# This example shows how to use Lark's templates to achieve cleaner grammars.
# It defines a reusable template rule for separated lists, and uses it to
# parse either a JSON-like list or dictionary.

from lark import Lark

# Grammar using a template rule `_seperated{x, sep}` to avoid repetition.
# The template is instantiated for lists (items separated by ",") and for
# dictionaries (key_value pairs separated by ",").
#
# Note: The misspelling `_seperated` mirrors the original example.
# It still works as a rule name.
grammar = r"""
start: list | dict

list: "[" _seperated{atom, ","} "]"
dict: "{" _seperated{key_value, ","} "}"
key_value: atom ":" atom

_seperated{x, sep}: x (sep x)*  // Define a sequence of 'x sep x sep x ...'

atom: NUMBER | ESCAPED_STRING

%import common (NUMBER, ESCAPED_STRING, WS)
%ignore WS
"""

parser = Lark(grammar)

# Demo parses
print(parser.parse('[1, "a", 2]'))
print(parser.parse('{"a": 2, "b": 6}'))
