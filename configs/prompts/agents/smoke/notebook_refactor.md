# NOTEBOOK TO PYTHON CONVERTER - GPT-5-MINI OPTIMIZED

## INPUT TYPE DETECTION
```
IF contains {"cells": → Python notebook JSON
IF contains ```python → Markdown notebook
ELSE → ERROR: Invalid input format
```

## CRITICAL STRING RULES - MUST FOLLOW EXACTLY
```
GRAMMAR STRINGS:
├── Multi-line grammar? → ALWAYS use r''' ... '''
│   └── NEVER use r"" or plain """
├── Concatenating grammars? → r''' part1 ''' + GRAMMAR_VAR + r''' part2 '''
│   └── Each segment MUST use r''' not r""
└── Single line? → Can use r"..." or r'...'

COMMON ERRORS TO AVOID:
✗ r"" (empty raw string) - WILL CAUSE SYNTAX ERROR
✗ """ for grammars - USE r''' INSTEAD
✗ Mixed quotes in concatenation
✓ r''' for ALL multiline grammars
```

## STEP-BY-STEP CONVERSION

### 1. Extract Content
- Parse notebook cells in order
- Code cells → Python code blocks
- Markdown cells → Section comments with #

### 2. Build Structure (IN THIS ORDER)
```python
"""
Module docstring describing the Lark example
"""

# Standard imports first
from lark import Lark, Transformer, v_args
# Other imports...

# Grammar definitions as constants
GRAMMAR_NAME = r'''
    rule: expression
    terminal: "literal" | /regex/
'''

# Transformer classes
@v_args(inline=True)  # Preserve decorators EXACTLY
class MyTransformer(Transformer):
    pass

# Main execution
if __name__ == '__main__':
    main()
```

### 3. Grammar Handling Checklist
- [ ] All grammars use r''' not """
- [ ] No r"" empty strings
- [ ] Operators preserved: | + * ? ~
- [ ] Directives intact: %import %ignore
- [ ] Regex patterns unchanged: /pattern/flags

### 4. Validation Before Output
```
CHECK: ast.parse(output_code) succeeds?
CHECK: No unterminated strings?
CHECK: All ''' properly closed?
CHECK: Filename doesn't end with .py.py?
```

## ERROR RECOVERY
If review_feedback mentions:
- "unterminated string" → Check all r''' are closed
- "syntax error" → Verify grammar concatenation uses r'''
- "imports missing" → Add from lark import ...
