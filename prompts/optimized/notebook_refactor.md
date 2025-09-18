Transform a Jupyter notebook (JSON or markdown export) about Lark into a standalone Python script.

Lark-Specific Handling
- Preserve all grammar definitions exactly; use r''' strings
- Keep Transformer/Visitor classes with decorators (@v_args)
- Maintain parse/transform code unchanged

Structure
- Start with a module docstring summarizing purpose and source URL
- Imports (e.g., from lark import Lark, Transformer, v_args)
- Grammar constants
- Transformer/Visitor classes
- Main execution block
- Convert markdown cells to clear comments

Context
- Type: {TYPE}
- URL: {URL}

Notebook Content
---
{DOCUMENT}
---
