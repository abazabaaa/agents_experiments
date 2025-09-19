"""
Lark parser examples converted from a Jupyter notebook into a standalone Python script.

This file demonstrates:
- An arithmetic expression grammar and a Transformer that evaluates expressions.
- A simple configuration file grammar (key=value pairs) that demonstrates terminal regex fixes
  to allow empty values and values containing commas and quotes.

Reviewer feedback (applied in this script):
1) Fixed NAME terminal regex to use /\w+/ (one or more word chars) instead of a spaced/malformed pattern.
2) Fixed VALUE terminal regex to /[^\n]*/ to allow empty values and values containing commas/quotes.
3) Ensured sample_conf parsing aligns with the VALUE pattern by stripping surrounding whitespace in the Transformer.

Converted notebook cells are provided as section comments. All Lark grammars are preserved as module-level raw triple-quoted strings.
"""

# -----------------------------
# Imports
# -----------------------------
from lark import Lark, Transformer, v_args

# -----------------------------
# Arithmetic expression grammar and transformer
# -----------------------------
expr_grammar = r'''
?start: sum

?sum: product
    | sum "+" product   -> add
    | sum "-" product   -> sub

?product: atom
    | product "*" atom  -> mul
    | product "/" atom  -> div

?atom: NUMBER           -> number
     | "-" atom        -> neg
     | "(" sum ")"

%import common.NUMBER
%import common.WS_INLINE
%ignore WS_INLINE
'''

# Transformer to evaluate arithmetic expressions
@v_args(inline=True)  # preserve decorator use and its arguments
class EvalTransformer(Transformer):
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

    def number(self, token):
        # NUMBER imported from common; convert to float or int as appropriate
        s = token.value
        return int(s) if s.isdigit() else float(s)

# -----------------------------
# Simple configuration grammar and transformer
# -----------------------------
# NOTE: The terminals below reflect reviewer feedback:
# - NAME: /\w+/  (one or more word characters)
# - VALUE: /[^\n]*/  (zero or more non-newline characters; allows empty values and commas/quotes)
config_grammar = r'''
start: pair*
pair: NAME "=" VALUE NEWLINE?

NAME: /\w+/      // fixed: one or more word chars
VALUE: /[^\n]*/  // fixed: accept empty values and characters including commas and quotes

%import common.NEWLINE
%import common.WS_INLINE
%ignore WS_INLINE
'''

@v_args(inline=True)
class ConfigTransformer(Transformer):
    """Transform parsed pairs into a Python dict.

    The VALUE token may include leading/trailing spaces depending on how whitespace
    is tokenized; strip() is used here to produce clean values while preserving
    empty values (which become empty strings).
    """
    def pair(self, name_token, value_token):
        name = str(name_token)
        # value_token can be an empty string (allowed by VALUE regex)
        value = str(value_token).strip()
        return (name, value)

    def start(self, *pairs):
        # pairs are tuples (name, value); combine into dict
        return dict(pairs)

# -----------------------------
# Example inputs and tests
# -----------------------------
# Section: arithmetic examples (converted from notebook cells)
arithmetic_examples = [
    "1 + 2 * 3",
    "(4 + 5) * (7 - 2) / 3",
    "-5 + 10",
    "42",
]

# Section: sample configuration demonstrating VALUE behavior
sample_conf = """
username=alice
password=
path=/usr/local/bin,/opt/bin
quote="a, b, c"
empty=
trailing_comma=one,two,
# a comment_line_should_be_treated_as_name_if_no_comment_rule=no
"""

# -----------------------------
# Main execution: build parsers, run examples
# -----------------------------
if __name__ == '__main__':
    print('--- Arithmetic expression parser demo ---')
    expr_parser = Lark(expr_grammar, parser='lalr', transformer=EvalTransformer())
    for expr in arithmetic_examples:
        try:
            tree = expr_parser.parse(expr)
            # Because transformer is attached, parse() already returns the evaluated result
            print(f"{expr} -> {tree}")
        except Exception as e:
            print(f"Error parsing '{expr}': {e}")

    print('\n--- Configuration file parser demo ---')
    config_parser = Lark(config_grammar, parser='lalr')
    parsed = config_parser.parse(sample_conf)

    # Transform separately to show preserved Transformer structure
    config_transformer = ConfigTransformer()
    config = config_transformer.transform(parsed)

    print('Raw sample_conf:')
    print(sample_conf)
    print('Parsed configuration dict:')
    for k, v in config.items():
        print(f"  {k!r}: {v!r}")

    # Demonstrate that VALUE allows empty values and values with commas/quotes
    assert config.get('username') == 'alice'
    assert config.get('password') == ''
    assert config.get('path') == '/usr/local/bin,/opt/bin'
    assert config.get('quote') == '"a, b, c"'
    assert config.get('empty') == ''
    assert config.get('trailing_comma') == 'one,two,'

    print('\nAll config assertions passed.')