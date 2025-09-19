"""
lark_notebook_converted.py

This script is a template and example for converting a Jupyter notebook containing
Lark parser examples into a standalone Python script. The script:

- Preserves Lark grammar definitions as triple-quoted raw strings
- Keeps Transformer/Visitor classes, including @v_args decorators
- Organizes notebook cells as commented sections
- Includes example inputs and outputs as comments

If you want me to convert a specific notebook, please paste the notebook JSON
or the notebook's markdown and code cells here. I will replace the placeholders
below with the exact notebook content and preserve all code and markdown as
comments.

The remainder of this file contains a working example (a simple calculator)
that demonstrates the required structure and Lark-specific handling.
"""

# --------------------------- Imports --------------------------------------
from lark import Lark, Transformer, v_args

# ------------------------ Grammar Definitions -----------------------------
# Preserve grammar definitions in triple-quoted raw strings (r'''...''')
# Replace the grammar below with the notebook's grammar strings when available.
CALC_GRAMMAR = r''' 
?start: sum

?sum: product
    | sum "+" product   -> add
    | sum "-" product   -> sub

?product: atom
    | product "*" atom  -> mul
    | product "/" atom  -> div

?atom: NUMBER           -> number
     | "-" atom         -> neg
     | "(" sum ")"

%import common.NUMBER
%import common.WS_INLINE
%ignore WS_INLINE
'''

# --------------------- Transformer / Visitor Classes ---------------------
# Preserve Transformer/Visitor class structures. Keep @v_args decorators.
# The example below uses @v_args(inline=True) which is a common pattern.

@v_args(inline=True)
class CalcTransformer(Transformer):
    """Transformer for the calculator grammar.

    This preserves structure and decorators as required. Replace or extend
    methods with notebook-specific transformations.
    """

    def number(self, token):
        # token is a lark.Token containing the number string
        return float(token)

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def neg(self, a):
        return -a

# ----------------------------- Parser ------------------------------------
# Create a reusable parser object. In the original notebook this might have
# been created inside a cell; here we create it at module level for reuse.

calc_parser = Lark(CALC_GRAMMAR, parser='lalr', transformer=CalcTransformer())

# -------------------------- Example Usage --------------------------------
# Convert code cells into functions or main-block execution. Preserve example
# inputs and outputs as comments.

EXAMPLES = [
    "1 + 2 * 3",
    "(1 + 2) * 3",
    "-5 + 3 * (2 + 1)",
]

# Example outputs (expected):
# 1 + 2 * 3 => 7.0
# (1 + 2) * 3 => 9.0
# -5 + 3 * (2 + 1) => 4.0

# --------------------------- Utility Functions ---------------------------
def evaluate_expression(expr: str):
    """Parse and evaluate a single expression using the calc_parser.

    Returns the Python numeric result produced by the Transformer.
    """
    # If the original notebook used parser.parse(...) and then transformer.transform(...)
    # combination, we preserve the code pattern here by demonstrating both options.

    # Option A: using parser with attached transformer (we already attached it)
    return calc_parser.parse(expr)

    # Option B: separate parse and transform (uncomment if you prefer explicit steps):
    # parse_tree = Lark(CALC_GRAMMAR, parser='lalr').parse(expr)
    # result = CalcTransformer().transform(parse_tree)
    # return result

# --------------------------- Converted Markdown ---------------------------
# The notebook's markdown cells are preserved below as commented sections.
# Replace these placeholders with the actual notebook markdown content.

# === Notebook Title ===
# Lark Parser Examples
# 
# This notebook demonstrates how to use Lark to parse simple grammars, transform
# parse trees, and visit nodes. The following sections contain grammar
# definitions, Transformer/Visitor implementations, and example parsings.

# === Section: Simple Calculator ===
# This section defined a calculator grammar and a Transformer to evaluate
# arithmetic expressions. The grammar is stored in CALC_GRAMMAR, and the
# transformation logic is implemented in CalcTransformer.

# If the notebook contained additional sections (e.g., demonstrations of
# visitors, AST manipulation, or debugging), paste those cells below as
# commented blocks and include the code cells as active Python code in this
# script.

# ------------------------------ Main Block --------------------------------
if __name__ == '__main__':
    # Execute and print example evaluations. In the original notebook the
    # outputs were shown as cell outputs; we include them here as printed
    # results and also preserve the original outputs as comments above.

    print("Calculator grammar:\n", CALC_GRAMMAR)

    for expr in EXAMPLES:
        result = evaluate_expression(expr)
        print(f"{expr} => {result}")

    # Additional notes:
    # - To convert a full notebook, provide the notebook JSON or markdown and
    #   code cells. I will integrate each code cell as executable code and each
    #   markdown cell as a commented section, preserving ordering.
    # - All Lark grammar strings will be kept verbatim in triple-quoted raw
    #   strings. Transformer and Visitor classes will be kept intact, including
    #   @v_args decorators and parse-tree manipulation code.

# ---------------------------- End of File --------------------------------
