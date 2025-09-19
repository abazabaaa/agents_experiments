---
title: "Grammar Composition"
description: "Example showing grammar composition in Lark, reusing grammars and transformers via namespaces to allow CSV and JSON to co-exist."
source_url: https://github.com/lark-parser/lark/blob/acfe33d943a1310f3ca26145eb2896bc5c4955c9/docs/examples/composition/index.rst
---

# Grammar Composition [](https://lark-parser.readthedocs.io/en/stable/examples/composition/#grammar-composition "Permalink to this heading")

This example shows how to do grammar composition in Lark, by creating a new
file format that allows both CSV and JSON to co-exist.

We show how, by using namespaces, Lark grammars and their transformers can be fully reused -
they don’t need to care if their grammar is used directly, or being imported, or who is doing the importing.

See [main.py](https://github.com/lark-parser/lark/blob/master/examples/composition/main.py) for more details.

[Edit on GitHub](https://github.com/lark-parser/lark/blob/acfe33d943a1310f3ca26145eb2896bc5c4955c9/docs/examples/composition/index.rst)

---

![](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_eval_json_thumb.png)

sphx\_glr\_examples\_composition\_eval\_json.py

Transformer for evaluating json.lark

![](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_eval_csv_thumb.png)

sphx\_glr\_examples\_composition\_eval\_csv.py

Transformer for evaluating csv.lark

![](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_main_thumb.png)

[Grammar Composition](https://lark-parser.readthedocs.io/en/stable/examples/composition/main.html#sphx-glr-examples-composition-main-py)
