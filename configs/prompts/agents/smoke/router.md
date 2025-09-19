TASK: Classify document as markdown OR notebook.

DECISION TREE:
Check content structure:
├── Contains ```python cells or {"cells": [ → route=notebook
├── Contains .ipynb JSON structure → route=notebook
├── Contains Jupyter magic commands (%%, !) → route=notebook
├── Contains EBNF grammar rules (lowercase: pattern) → route=markdown
├── Contains TERMINALS (UPPERCASE: /regex/) → route=markdown
├── Contains Lark directives (%import, %ignore) → route=markdown
├── Contains Templates name{params}: expression → route=markdown
└── Default markdown prose → route=markdown

OUTPUT: route=markdown OR route=notebook
KEEP EXPLANATION UNDER 10 WORDS.
