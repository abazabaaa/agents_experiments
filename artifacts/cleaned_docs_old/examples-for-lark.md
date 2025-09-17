---
title: Examples for Lark
source_url: https://lark-parser.readthedocs.io/en/stable/examples/index.html
description: Gallery and instructions for running beginner and advanced Lark parser examples, grammar composition, example grammars, and a standalone example.
---

# Examples for Lark

How to run the examples:

After cloning the repo, open a terminal in the project root and run:

```bash
python -m examples.<name_of_example>
```

For example, to parse all the Python files in your local standard library:

```bash
python -m examples.advanced.python_parser
```

## Beginner Examples

- [Parsing Indentation](https://lark-parser.readthedocs.io/en/stable/examples/indented_tree.html#sphx-glr-examples-indented-tree-py)
- [Lark Grammar](https://lark-parser.readthedocs.io/en/stable/examples/lark_grammar.html#sphx-glr-examples-lark-grammar-py)
- [Handling Ambiguity](https://lark-parser.readthedocs.io/en/stable/examples/fruitflies.html#sphx-glr-examples-fruitflies-py)
- [Basic calculator](https://lark-parser.readthedocs.io/en/stable/examples/calc.html#sphx-glr-examples-calc-py)
- [Turtle DSL](https://lark-parser.readthedocs.io/en/stable/examples/turtle_dsl.html#sphx-glr-examples-turtle-dsl-py)
- [Simple JSON Parser](https://lark-parser.readthedocs.io/en/stable/examples/json_parser.html#sphx-glr-examples-json-parser-py)

## Advanced Examples

- [LALR’s contextual lexer](https://lark-parser.readthedocs.io/en/stable/examples/advanced/conf_lalr.html#sphx-glr-examples-advanced-conf-lalr-py)
- [Templates](https://lark-parser.readthedocs.io/en/stable/examples/advanced/templates.html#sphx-glr-examples-advanced-templates-py)
- [Earley’s dynamic lexer](https://lark-parser.readthedocs.io/en/stable/examples/advanced/conf_earley.html#sphx-glr-examples-advanced-conf-earley-py)
- [Error handling using an interactive parser](https://lark-parser.readthedocs.io/en/stable/examples/advanced/error_handling.html#sphx-glr-examples-advanced-error-handling-py)
- [Reconstruct a JSON](https://lark-parser.readthedocs.io/en/stable/examples/advanced/reconstruct_json.html#sphx-glr-examples-advanced-reconstruct-json-py)
- [Custom lexer](https://lark-parser.readthedocs.io/en/stable/examples/advanced/custom_lexer.html#sphx-glr-examples-advanced-custom-lexer-py)
- [Transform a Forest](https://lark-parser.readthedocs.io/en/stable/examples/advanced/tree_forest_transformer.html#sphx-glr-examples-advanced-tree-forest-transformer-py)
- [Simple JSON Parser (advanced)](https://lark-parser.readthedocs.io/en/stable/examples/advanced/_json_parser.html#sphx-glr-examples-advanced-json-parser-py)
- [Custom SPPF Prioritizer](https://lark-parser.readthedocs.io/en/stable/examples/advanced/prioritizer.html#sphx-glr-examples-advanced-prioritizer-py)
- [Python 3 to Python 2 converter (tree templates)](https://lark-parser.readthedocs.io/en/stable/examples/advanced/py3to2.html#sphx-glr-examples-advanced-py3to2-py)
- [Grammar-complete Python Parser](https://lark-parser.readthedocs.io/en/stable/examples/advanced/python_parser.html#sphx-glr-examples-advanced-python-parser-py)
- [Creating an AST from the parse tree](https://lark-parser.readthedocs.io/en/stable/examples/advanced/create_ast.html#sphx-glr-examples-advanced-create-ast-py)
- [Example-Driven Error Reporting (Earley)](https://lark-parser.readthedocs.io/en/stable/examples/advanced/error_reporting_earley.html#sphx-glr-examples-advanced-error-reporting-earley-py)
- [Example-Driven Error Reporting (LALR)](https://lark-parser.readthedocs.io/en/stable/examples/advanced/error_reporting_lalr.html#sphx-glr-examples-advanced-error-reporting-lalr-py)
- [Reconstruct Python](https://lark-parser.readthedocs.io/en/stable/examples/advanced/reconstruct_python.html#sphx-glr-examples-advanced-reconstruct-python-py)
- [Using lexer dynamic_complete](https://lark-parser.readthedocs.io/en/stable/examples/advanced/dynamic_complete.html#sphx-glr-examples-advanced-dynamic-complete-py)
- [Syntax Highlighting](https://lark-parser.readthedocs.io/en/stable/examples/advanced/qscintilla_json.html#sphx-glr-examples-advanced-qscintilla-json-py)

## Grammar Composition

This example shows how to do grammar composition in Lark, by creating a new file format that allows both CSV and JSON to co-exist.

By using namespaces, Lark grammars and their transformers can be fully reused—they don’t need to care if their grammar is used directly, imported, or who is doing the importing.

See main.py for more details: https://github.com/lark-parser/lark/blob/master/examples/composition/main.py

- Transformer for evaluating json.lark (thumbnail): https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_eval_json_thumb.png
- Transformer for evaluating csv.lark (thumbnail): https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_eval_csv_thumb.png
- [Grammar Composition (example page)](https://lark-parser.readthedocs.io/en/stable/examples/composition/main.html#sphx-glr-examples-composition-main-py)

## Example Grammars

A collection of Lark grammars taken from real-world projects.

- Verilog — https://github.com/lark-parser/lark/blob/master/examples/grammars/verilog.lark (source: https://github.com/circuitgraph/circuitgraph/blob/main/circuitgraph/parsing/verilog.lark)

## Standalone example

To initialize, cd to the standalone folder and run:

```bash
./create_standalone.sh
```

Or:

```bash
python -m lark.tools.standalone json.lark > json_parser.py
```

Then run using:

```bash
python json_parser_main.py <path-to.json>
```

- [Standalone Parser](https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html#sphx-glr-examples-standalone-json-parser-main-py)

## Downloads

- Download all examples in Python source code: https://lark-parser.readthedocs.io/en/stable/_downloads/bc82bea3a5dd7bdba60b65220891d9e5/examples_python.zip
- Download all examples in Jupyter notebooks: https://lark-parser.readthedocs.io/en/stable/_downloads/fb625db3c50d423b1b7881136ffdeec8/examples_jupyter.zip

Gallery generated by Sphinx-Gallery: https://sphinx-gallery.github.io/
