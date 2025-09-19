---
title: "LALR’s contextual lexer"
description: "Example demonstrating LALR's contextual lexer by parsing a toy configuration language. Preserves original grammar and runnable Python example."
source_url: "https://github.com/lark-parser/lark/blob/acfe33d943a1310f3ca26145eb2896bc5c4955c9/docs/examples/advanced/conf_lalr.rst"
---

# LALR’s contextual lexer

This example demonstrates the power of LALR’s contextual lexer by parsing a toy configuration language.

The terminals `NAME` and `VALUE` overlap. They can match the same input. A basic lexer would arbitrarily choose one over the other, based on priority, which would lead to a (confusing) parse error. However, due to the unambiguous structure of the grammar, Lark’s LALR(1) algorithm knows which one of them to expect at each point during the parse. The lexer then only matches the tokens that the parser expects. The result is a correct parse, something that is impossible with a regular lexer.

Another approach is to use the Earley algorithm. It will handle more cases than the contextual lexer, but at the cost of performance. See `examples/conf_earley.py` for an example of that approach.

## Example

```python
from lark import Lark

parser = Lark(r"""
        start: _NL? section+
        section: "[" NAME "]" _NL item+
        item: NAME "=" VALUE? _NL

        NAME: /\w/+ 
        VALUE: /./+

        %import common.NEWLINE -> _NL
        %import common.WS_INLINE
        %ignore WS_INLINE
    """, parser="lalr")

sample_conf = """
[bla]
a=Hello
this="that",4
empty=
"""

print(parser.parse(sample_conf).pretty())

```

**Total running time of the script:** (0 minutes 0.000 seconds)

## Download

- [Download Python source code: conf_lalr.py](https://lark-parser.readthedocs.io/en/stable/_downloads/3ed7cc698fc366fe253eac6ecf76ee3e/conf_lalr.py)
- [Download Jupyter notebook: conf_lalr.ipynb](https://lark-parser.readthedocs.io/en/stable/_downloads/9e5ca2d2f34acae5a9391bd4b16a935f/conf_lalr.ipynb)

## Related

- Home: https://lark-parser.readthedocs.io/en/stable/index.html
- Examples for Lark: https://lark-parser.readthedocs.io/en/stable/examples/index.html
- Advanced Examples: https://lark-parser.readthedocs.io/en/stable/examples/advanced/index.html
- Edit on GitHub: https://github.com/lark-parser/lark/blob/acfe33d943a1310f3ca26145eb2896bc5c4955c9/docs/examples/advanced/conf_lalr.rst

