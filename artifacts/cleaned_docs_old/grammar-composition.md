---
title: Grammar Composition (Lark Examples)
original_url: https://lark-parser.readthedocs.io/en/stable/examples/composition
summary: Demonstrates composing grammars in Lark to combine CSV and JSON, reusing grammars and transformers via namespaces. Links to example code and rendered gallery items.
---

# Grammar Composition

This example shows how to do grammar composition in Lark, by creating a new file format that allows both CSV and JSON to co-exist.

By using namespaces, Lark grammars and their transformers can be fully reused — they don’t need to care if their grammar is used directly, being imported, or who is doing the importing.

See main.py for more details:
- https://github.com/lark-parser/lark/blob/master/examples/composition/main.py

Gallery thumbnails:

- Transformer for evaluating json.lark
  - Image: https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_eval_json_thumb.png
  - Source: sphx_glr_examples_composition_eval_json.py

- Transformer for evaluating csv.lark
  - Image: https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_eval_csv_thumb.png
  - Source: sphx_glr_examples_composition_eval_csv.py

- Grammar Composition example page
  - Image: https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_main_thumb.png
  - Link: https://lark-parser.readthedocs.io/en/stable/examples/composition/main.html#sphx-glr-examples-composition-main-py
