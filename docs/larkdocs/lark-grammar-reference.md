---
title: Lark Grammar
description: A reference implementation of the Lark grammar (using LALR(1)) that parses Lark's own grammar files and validates several example grammars.
source_url: https://lark-parser.readthedocs.io/en/stable/examples/lark_grammar.html
---

# Lark Grammar

A reference implementation of the Lark grammar (using LALR(1)).

## Example code

```python
import lark
from pathlib import Path

examples_path = Path(__file__).parent
lark_path = Path(lark.__file__).parent

parser = lark.Lark.open(lark_path / 'grammars/lark.lark', rel_to=__file__, parser="lalr")

grammar_files = [\
    examples_path / 'advanced/python2.lark',\
    examples_path / 'relative-imports/multiples.lark',\
    examples_path / 'relative-imports/multiple2.lark',\
    examples_path / 'relative-imports/multiple3.lark',\
    examples_path / 'tests/no_newline_at_end.lark',\
    examples_path / 'tests/negative_priority.lark',\
    examples_path / 'standalone/json.lark',\
    lark_path / 'grammars/common.lark',\
    lark_path / 'grammars/lark.lark',\
    lark_path / 'grammars/unicode.lark',\
    lark_path / 'grammars/python.lark',\
]

def test():
    for grammar_file in grammar_files:
        tree = parser.parse(open(grammar_file).read())
    print("All grammars parsed successfully")

if __name__ == '__main__':
    test()

```

Total running time of the script: (0 minutes 0.000 seconds)

## Downloads

- Download Python source code: lark_grammar.py: https://lark-parser.readthedocs.io/en/stable/_downloads/b9abd703bb1b061d8ae5f6ab1b9393e8/lark_grammar.py
- Download Jupyter notebook: lark_grammar.ipynb: https://lark-parser.readthedocs.io/en/stable/_downloads/2f68c21f7729a47e57d3ae345753e407/lark_grammar.ipynb

## See also

- Parsing Indentation (previous): https://lark-parser.readthedocs.io/en/stable/examples/indented_tree.html
- Handling Ambiguity (next): https://lark-parser.readthedocs.io/en/stable/examples/fruitflies.html
- Edit on GitHub: https://github.com/lark-parser/lark/blob/acfe33d943a1310f3ca26145eb2896bc5c4955c9/docs/examples/lark_grammar.rst
