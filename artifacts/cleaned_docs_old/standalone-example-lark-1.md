---
title: Standalone Example (Lark)
description: How to generate and run a standalone JSON parser with Lark, including command examples and links to the runnable example.
source_url: https://lark-parser.readthedocs.io/en/stable/examples/standalone/index.html
---

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

![Thumbnail of the standalone JSON parser example](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_json_parser_main_thumb.png)

See also: Standalone Parser — https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html#sphx-glr-examples-standalone-json-parser-main-py
