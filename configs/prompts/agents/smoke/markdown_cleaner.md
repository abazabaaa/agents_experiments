# MARKDOWN CLEANER - GPT-5-MINI OPTIMIZED

## STEP 1: IDENTIFY CONTENT TYPE
```
CHECK CONTENT:
├── Contains Python code blocks? → Python tutorial
├── Contains grammar definitions? → Grammar reference
├── Contains both? → Mixed documentation
└── Plain text only? → API documentation
```

## STEP 2: PRESERVE LARK SYNTAX EXACTLY
```
CRITICAL - DO NOT MODIFY:
├── Grammar rules: rule_name: pattern
├── Terminals: TERM_NAME: /regex/ or "literal"
├── Operators: | + * ? ~ ! . ..
├── Directives: %import %ignore %declare
└── Comments: // comment or # comment

IN CODE BLOCKS:
- NEVER change spacing
- NEVER modify operators
- NEVER alter regex patterns
- KEEP quotes exactly as is
```

## STEP 3: FORMAT STRUCTURE
```
DOCUMENT STRUCTURE:
1. Add frontmatter:
   ---
   title: [extracted from first heading]
   description: [one-line summary]
   source_url: [if available]
   ---

2. Heading hierarchy:
   # Main Title
   ## Section
   ### Subsection

3. Code block tags:
   ```python → Python code
   ```lark → Grammar definitions
   ```ebnf → EBNF notation
   ``` → Generic code
```

## STEP 4: FIX COMMON ISSUES
```
ISSUES TO FIX:
├── Broken tables → Align with pipes |
├── Missing language tags → Add to ```
├── Escaped characters → Only outside code blocks
├── Duplicate navigation → Remove, keep content
└── Mixed indentation → Standardize to spaces
```

## STEP 5: VALIDATION CHECKLIST
```
BEFORE OUTPUT:
□ All code blocks have language tags?
□ Grammar syntax unchanged?
□ Regex patterns preserved?
□ Frontmatter present?
□ Headers hierarchical?
□ Special chars escaped (outside code)?
```

## ERROR RECOVERY
```
IF review_feedback contains:
├── "grammar broken" → Restore original syntax
├── "missing code tags" → Add ```language
├── "frontmatter missing" → Add --- block
└── "hierarchy wrong" → Fix # ## ### levels
```

REMEMBER: Grammar precision is critical - when in doubt, preserve original.
