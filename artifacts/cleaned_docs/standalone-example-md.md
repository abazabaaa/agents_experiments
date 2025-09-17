---
title: Standalone example
description: Generate a standalone Python parser from a Lark grammar and run the JSON example.
source_url: https://lark-parser.readthedocs.io/en/stable/examples/standalone/
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

![JSON parser example thumbnail](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_json_parser_main_thumb.png)

## See also

- Standalone Parser: https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html
