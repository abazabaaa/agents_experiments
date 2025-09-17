---
title: Features
description: Overview of Lark's main and extra features, including Earley and LALR parsers, grammar capabilities, tooling, and ecosystem integrations.
source_url: https://lark-parser.readthedocs.io/en/stable/features.html
---

# Features

## Main Features

- Earley parser, capable of parsing any context-free grammar
  - Implements SPPF, for efficient parsing and storing of ambiguous grammars.
- LALR(1) parser, limited in power of expression, but very efficient in space and performance (O(n)).
  - Implements a parse-aware lexer that provides a better power of expression than traditional LALR implementations (such as PLY).
- EBNF-inspired grammar, with extra features (See: [Grammar Reference](https://lark-parser.readthedocs.io/en/stable/grammar.html))
- Builds a parse tree (AST) automatically based on the grammar
- Stand-alone parser generator — create a small independent parser to embed in your project ([read more](https://lark-parser.readthedocs.io/en/stable/tools.html#stand-alone-parser))
- Flexible error handling by using an interactive parser interface (LALR only)
- Automatic line & column tracking (for both tokens and matched rules)
- Automatic terminal collision resolution
- Warns on regex collisions using the optional `interegular` library ([read more](https://lark-parser.readthedocs.io/en/stable/how_to_use.html#regex-collisions))
- Grammar composition — import terminals and rules from other grammars (see [example](https://github.com/lark-parser/lark/tree/master/examples/composition))
- Standard library of terminals (strings, numbers, names, etc.)
- Unicode fully supported
- Extensive test suite
- Type annotations (MyPy support)
- Pure-Python implementation

[Read more about the parsers](https://lark-parser.readthedocs.io/en/stable/parsers.html)

## Extra Features

- Support for external regex module ([see here](https://lark-parser.readthedocs.io/en/stable/classes.html#using-unicode-character-classes-with-regex))
- Import grammars from Nearley.js ([read more](https://lark-parser.readthedocs.io/en/stable/tools.html#importing-grammars-from-nearleyjs))
- CYK parser
- Visualize your parse trees as dot or png files ([see example](https://github.com/lark-parser/lark/blob/master/examples/fruitflies.py))
- Automatic reconstruction of input from parse tree (see [example](https://github.com/lark-parser/lark/blob/master/examples/advanced/reconstruct_json.py) and [another example](https://github.com/lark-parser/lark/blob/master/examples/advanced/reconstruct_python.py))
- Use Lark grammars in [Julia](https://github.com/jamesrhester/Lerche.jl) and [JavaScript](https://github.com/lark-parser/Lark.js).
