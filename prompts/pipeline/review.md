STRICT JSON OUTPUT ONLY. Do not include markdown or code fences.

Schema
- {approved: boolean, issues: string|null, suggestions: string|null}

Rules
- Approve only if accurate, consistent, and well formatted.
- Keep strings concise: issues<=1200 chars; suggestions<=800 chars.
- Use short sentences; avoid long lists.

Context
- Type: {TYPE}
- URL: {URL}
- Summary: {SUMMARY}

Transformed Document
---
{DOCUMENT}
---

Return approved=true only if production ready.
