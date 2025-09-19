Transform Jupyter notebook (JSON or markdown) containing Lark parser examples into a standalone Python script.

LARK-SPECIFIC HANDLING:
1. Preserve all Lark grammar definitions in triple-quoted strings
2. Keep grammar syntax exact: rules, terminals, operators, directives
3. Maintain Transformer and Visitor class structures
4. Preserve @v_args decorators and their arguments
5. Keep parse tree manipulation code intact
6. Convert notebook cells to logical sections with clear comments

STRUCTURE:
- Start with module docstring explaining the Lark example
- Import statements (especially: from lark import Lark, Transformer, v_args)
- Grammar definitions as module-level constants (use r''' for raw strings)
- Transformer/Visitor classes with proper decorators
- Main execution block with if __name__ == '__main__':
- Convert markdown cells to section comments
- Preserve all test cases and example inputs

RESULT: Executable Python script demonstrating Lark parser functionality.

If review_feedback provided, implement those specific changes.
