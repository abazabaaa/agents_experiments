---
title: Standalone example (Lark)
original_url: https://lark-parser.readthedocs.io/en/stable/examples/standalone
summary: How to generate and run a standalone Lark parser from a grammar file.
---

# Standalone example

This example shows how to generate a standalone parser from a Lark grammar and run it.

To initialize, cd to this folder, and run:

```bash
./create_standalone.sh
```

Or generate the parser directly with Python:

```bash
python -m lark.tools.standalone json.lark > json_parser.py
```

Then run the example script:

```bash
python json_parser_main.py <path-to.json>
```

Screenshot/thumbnail:

![Standalone JSON parser thumbnail](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_json_parser_main_thumb.png)

Related example and details:
- Standalone Parser: https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html
