---
title: Grammar Composition
description: Demonstrates composing Lark grammars (CSV and JSON) using namespaces so grammars and transformers can be fully reused.
source_url: https://lark-parser.readthedocs.io/en/stable/examples/composition
---

# Grammar Composition

This example shows how to do grammar composition in Lark by creating a new file format that allows both CSV and JSON to co-exist.

By using namespaces, Lark grammars and their transformers can be fully reused—they don’t need to care if their grammar is used directly, being imported, or who is doing the importing.

See main.py for more details:
- https://github.com/lark-parser/lark/blob/master/examples/composition/main.py

## Examples

### Evaluating JSON (Transformer)

![JSON transformer thumbnail](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_eval_json_thumb.png)

File: `sphx_glr_examples_composition_eval_json.py`

Transformer for evaluating json.lark:
- https://lark-parser.readthedocs.io/en/stable/examples/composition/eval_json.html

### Evaluating CSV (Transformer)

![CSV transformer thumbnail](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_eval_csv_thumb.png)

File: `sphx_glr_examples_composition_eval_csv.py`

Transformer for evaluating csv.lark:
- https://lark-parser.readthedocs.io/en/stable/examples/composition/eval_csv.html

### Composition Demo

![Composition main thumbnail](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_main_thumb.png)

Grammar Composition example page:
- https://lark-parser.readthedocs.io/en/stable/examples/composition/main.html#sphx-glr-examples-composition-main-py
