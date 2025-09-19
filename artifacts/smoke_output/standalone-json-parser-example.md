---
title: Standalone example
description: Instructions to create and run a standalone JSON parser using Lark, including commands to generate a standalone parser and run it, with a link to the source.
source_url: https://github.com/lark-parser/lark/blob/acfe33d943a1310f3ca26145eb2896bc5c4955c9/docs/examples/standalone/index.rst
---

# Standalone example

To initialize, change directory to this folder and run the following commands to create a standalone parser for a JSON grammar and run it.

To generate the standalone parser using the provided shell script:

```bash
./create_standalone.sh

```

Or generate the standalone parser directly with Python:

```bash
python -m lark.tools.standalone json.lark > json_parser.py

```

Run the generated parser (or the provided main script) like this:

```bash
python json_parser_main.py <path-to.json>

```


![](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_json_parser_main_thumb.png)

## Standalone Parser

For more details and the runnable example, see the Standalone Parser documentation:

- Standalone Parser: https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html#sphx-glr-examples-standalone-json-parser-main-py
- Edit on GitHub: https://github.com/lark-parser/lark/blob/acfe33d943a1310f3ca26145eb2896bc5c4955c9/docs/examples/standalone/index.rst

