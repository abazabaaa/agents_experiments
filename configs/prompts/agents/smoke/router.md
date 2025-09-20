# DOCUMENT ROUTER - GPT-5-MINI OPTIMIZED

## PRIMARY CHECK - NOTEBOOK INDICATORS
```
STRONG NOTEBOOK SIGNALS (ANY = notebook):
├── Contains {"cells": [ → route=notebook
├── Contains "cell_type": "code" → route=notebook
├── Has ```python with class/def → route=notebook
├── Has from lark import → route=notebook
├── Contains if __name__ == '__main__' → route=notebook
└── Has .ipynb anywhere in text → route=notebook
```

## SECONDARY CHECK - CONTENT ANALYSIS
```
IF NOT notebook from above, CHECK:
├── Multiple ```python blocks with code? → route=notebook
├── Has Python imports + functions? → route=notebook
├── Grammar in triple quotes r'''? → route=notebook
├── Only documentation/explanation? → route=markdown
├── Grammar in ```lark blocks only? → route=markdown
└── No executable Python code? → route=markdown
```

## EDGE CASES - SPECIFIC RULES
```
MIXED CONTENT:
├── Markdown with embedded notebook JSON → route=notebook
├── Tutorial with runnable Python code → route=notebook
├── Grammar reference (no Python) → route=markdown
└── API documentation → route=markdown
```

## OUTPUT FORMAT
```
ANSWER: route=notebook OR route=markdown
REASON: [max 10 words explaining the key indicator]
```

## CRITICAL: AVOID MISCLASSIFICATION
```
NEVER route Python code to markdown if it has:
- Class definitions with methods
- Function definitions
- Main execution blocks
- Import statements
```
