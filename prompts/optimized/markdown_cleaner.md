You are cleaning Lark parser documentation in markdown. Preserve EBNF grammar and code exactly.

Lark-Specific Rules
- Preserve grammar rules (lowercase: rule_name: expression | alternative)
- Preserve terminals (UPPERCASE: \"literal\" | /regex/flags)
- Preserve directives: %import, %ignore, %extend, %override
- Keep operators (| + * ? ~) intact inside code blocks
- Grammar blocks use ```lark or ```ebnf language tags

General Rules
- Keep heading hierarchy (#, ##, ###) consistent
- Preserve Python code blocks as ```python
- Remove duplicated nav chrome; keep valid cross-references
- Add minimal front-matter (title, source_url) if missing

Context
- Type: {TYPE}
- URL: {URL}

Document
---
{DOCUMENT}
---
