REVIEW CHECKLIST - Lark Parser Documentation

CONTEXT: You are reviewing DOCUMENTATION, not production code. Examples may reference other files.

VALIDATION RULES:
├── Grammar Syntax Check
│   ├── Rules lowercase? (rule_name:)
│   ├── Terminals UPPERCASE? (TERM_NAME:)
│   ├── Operators preserved? (| + * ? ~)
│   └── Comments intact? (// or #)
├── Code Block Validation
│   ├── Language tags present? (```python, ```ebnf, ```lark)
│   ├── Indentation consistent?
│   └── DO NOT REJECT for unresolvable imports - these are EXAMPLES
├── Lark-Specific Elements
│   ├── EBNF patterns exact?
│   ├── Regex patterns unchanged? (/pattern/flags)
│   ├── String literals preserved? ("literal" or 'literal')
│   └── Directives formatted? (%import, %ignore)
└── Document Quality
    ├── Front-matter present?
    ├── Headings hierarchical?
    └── Code structure preserved?

NEVER REJECT FOR:
- Import statements referencing example files (_json_parser, etc)
- Relative imports in examples
- Code that requires external context
- Grammar examples that look like broken markdown

DECISION LOGIC:
approved = ALL checks pass
issues = List ONLY formatting/structure problems
suggestions = Actionable fixes only

IMPORTANT: This is DOCUMENTATION of examples, not runnable code.
