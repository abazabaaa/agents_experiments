---
title: Standalone Example (Lark)
original_url: https://lark-parser.readthedocs.io/en/stable/examples/standalone
summary: Instructions for generating and running a standalone JSON parser with Lark, using either a helper script or the lark.tools.standalone module.
---

# Standalone Example

This example shows how to generate and run a standalone JSON parser with Lark.

## Setup

From the example directory, initialize the standalone parser using one of the following methods:

- Using the shell script:

```bash
./create_standalone.sh
```

- Using the Python module directly:

```bash
python -m lark.tools.standalone json.lark > json_parser.py
```

## Run

Execute the generated parser on a JSON file:

```bash
python json_parser_main.py <path-to.json>
```

## Demo

Image preview:

![](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_json_parser_main_thumb.png)

Detailed walkthrough:
- Standalone Parser: https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html#sphx-glr-examples-standalone-json-parser-main-py
