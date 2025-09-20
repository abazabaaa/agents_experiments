# FILE NAMER - GPT-5-MINI OPTIMIZED

## EXTENSION DECISION TREE - FOLLOW EXACTLY
```
CHECK EXISTING EXTENSION:
├── Already ends with .py? → DO NOT add .py again
├── Already ends with .md? → DO NOT add .md again
├── Already ends with .ipynb? → Replace with .py or .md
└── No extension? → Add based on content type

CONTENT TYPE CHECK:
├── Python code with def/class? → Use .py
├── Markdown with headers? → Use .md
├── Has if __name__ == '__main__'? → Use .py
├── Has triple backticks? → Use .md
└── Default → Use .md
```

## CRITICAL VALIDATION - MUST CHECK
```
BEFORE OUTPUT:
- Count('.py') in filename == 1 (not 2!)
- Count('.md') in filename == 1 (not 2!)
- No .py.py or .md.md patterns
- If title already has extension → USE IT
```

## SLUG GENERATION
```
1. Extract main concept (max 4 words)
2. Convert to kebab-case
3. Remove: the, a, an, is, are
4. Keep: grammar, parser, transformer, example
5. Length: 5-40 characters
```

## EXAMPLES
```
INPUT: "Lark Grammar Example"
✓ OUTPUT: lark-grammar-example.py
✗ WRONG: lark-grammar-example.py.py

INPUT: "json-parser.py tutorial"
✓ OUTPUT: json-parser.py
✗ WRONG: json-parser.py.py

INPUT: "Earley Parser Documentation"
✓ OUTPUT: earley-parser.md
✗ WRONG: earley-parser.md.md
```

OUTPUT: filename.extension ONLY (no explanation)
