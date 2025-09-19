---
title: "Standalone example — Lark documentation"
description: "Instructions and examples for creating and running a standalone parser with Lark. Includes commands to generate a standalone Python parser from a .lark grammar and how to run the generated parser."
source_url: "https://lark-parser.readthedocs.io/en/stable/examples/standalone"
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


![Standalone parser thumbnail](https://lark-parser.readthedocs.io/en/stable/_images/sphx_glr_json_parser_main_thumb.png)

## Links

- Home: https://lark-parser.readthedocs.io/en/stable/index.html
- Examples for Lark: https://lark-parser.readthedocs.io/en/stable/examples/index.html
- Edit on GitHub: https://github.com/lark-parser/lark/blob/acfe33d943a1310f3ca26145eb2896bc5c4955c9/docs/examples/standalone/index.rst
- Standalone Parser (example page): https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html#sphx-glr-examples-standalone-json-parser-main-py

## Navigation

- Previous: Example Grammars — https://lark-parser.readthedocs.io/en/stable/examples/grammars/index.html
- Next: Standalone Parser — https://lark-parser.readthedocs.io/en/stable/examples/standalone/json_parser_main.html


## Notes

- This page demonstrates how to create a standalone parser from a Lark grammar file (json.lark) and run the resulting Python parser.
- The commands and code blocks above are preserved exactly as in the source.

<!-- Documentation footer links preserved for reference -->

Versions:
- latest: https://lark-parser.readthedocs.io/en/latest/examples/standalone/
- stable: https://lark-parser.readthedocs.io/en/stable/examples/standalone/

Downloads:
- PDF: https://lark-parser.readthedocs.io/_/downloads/en/stable/pdf/
- HTML: https://lark-parser.readthedocs.io/_/downloads/en/stable/htmlzip/
- EPUB: https://lark-parser.readthedocs.io/_/downloads/en/stable/epub/

Project on Read the Docs:
- Project Home: https://app.readthedocs.org/projects/lark-parser/?utm_source=lark-parser&utm_content=flyout
- Builds: https://app.readthedocs.org/projects/lark-parser/builds/?utm_source=lark-parser&utm_content=flyout

Hosted by Read the Docs: https://about.readthedocs.com/?utm_source=lark-parser&utm_content=flyout
