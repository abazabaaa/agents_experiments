---
title: Lark Standalone Example
source_url: https://lark-parser.readthedocs.io/en/stable/examples/standalone/index.html
description: How to generate and run a standalone JSON parser using Lark's standalone tool.
---

# Standalone example

This example shows how to generate a standalone Python parser from a Lark grammar and run it on a JSON file.

## Setup

From the example directory, run one of the following commands to create the standalone parser:

```bash
./create_standalone.sh
```

Or generate it directly with Python:

```bash
python -m lark.tools.standalone json.lark > json_parser.py
```

## Run the parser

```bash
python json_parser_main.py <path-to.json>
```

## Example

Image preview of the example run:

![Standalone JSON parser example](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_json_parser_main_thumb.png)

See the full example and code: https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html
