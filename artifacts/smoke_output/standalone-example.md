---
title: Standalone example
description: How to create and run a standalone parser for a Lark grammar (JSON example).
source_url: https://lark-parser.readthedocs.io/en/stable/examples/standalone
---

[Home](https://lark-parser.readthedocs.io/en/stable/index.html) · [Examples for Lark](https://lark-parser.readthedocs.io/en/stable/examples/index.html) · Standalone example

# Standalone example

To initialize, cd to this folder, and run:

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

![json parser thumbnail](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_json_parser_main_thumb.png)

See the standalone parser example page:

- [Standalone Parser](https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html#sphx-glr-examples-standalone-json-parser-main-py)

