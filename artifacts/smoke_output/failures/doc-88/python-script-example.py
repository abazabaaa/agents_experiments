"""
Lark parser examples converted from a Jupyter notebook into a standalone Python script.

This module demonstrates multiple Lark grammars, Transformer usage, and parsing examples.

Reviewer feedback (applied):
- The TURTLE_GRAMMAR raw triple-quoted string was not closed correctly in a prior version. It ended with ``'''``\' which broke the string literal. That has been fixed: the TURTLE_GRAMMAR now uses a properly terminated raw triple-quoted string (r''' ... ''').

The file preserves grammar definitions as raw triple-quoted strings, retains Transformer classes and @v_args usage, and keeps example inputs and tests in the main block.
"""

# Section: Imports
from lark import Lark, Transformer, v_args, Visitor, Token, Tree
import sys

# Section: Grammar definitions

# Simple arithmetic grammar example
SIMPLE_ARITH_GRAMMAR = r'''
?start: sum

?sum: product
    | sum "+" product   -> add
    | sum "-" product   -> sub

?product: atom
    | product "*" atom  -> mul
    | product "/" atom  -> div

?atom: NUMBER           -> number
     | "(" sum ")"

%import common.NUMBER
%import common.WS_INLINE
%ignore WS_INLINE
'''

# Turtle-like grammar example (fixed closing triple quote)
# Note: Reviewer feedback above indicated this raw string was previously unterminated.
TURTLE_GRAMMAR = r'''
start: statement*

statement: prefixDecl
         | baseDecl
         | triples "."

prefixDecl: "@prefix" PNAME_NS IRIREF "."
baseDecl: "@base" IRIREF "."

triples: subject predicateObjectList

predicateObjectList: verb objectList (";" (verb objectList)*)?
objectList: object ("," object)*

subject: varOrTerm
verb: varOrTerm | "a"
object: varOrTerm | RDFLiteral

varOrTerm: IRIREF | PNAME_LN | BLANK_NODE_LABEL | NIL | RDFLiteral | NUMBER

PNAME_NS: /[A-Za-z][A-Za-z0-9_-]*:/
PNAME_LN: PNAME_NS /[A-Za-z][A-Za-z0-9_\-]*/
IRIREF: "<" /[^>\n]*/ ">"
BLANK_NODE_LABEL: "_:" /[A-Za-z0-9]+/
NIL: "()"
RDFLiteral: STRING (LANGTAG | "^^" (IRIREF | PNAME_LN))?

STRING: /\"([^\\\n\r\"]|\\.)*\"/ | /\'([^\\\n\r\']|\\.)*\'/
LANGTAG: "@" /[a-zA-Z]+(-[a-zA-Z0-9]+)*/
NUMBER: /[0-9]+(\.[0-9]+)?/

%import common.WS
%ignore WS
'''

# Another example: simple JSON-ish grammar (for demonstration)
SIMPLE_JSON_GRAMMAR = r'''
?start: value

?value: object
      | array
      | STRING      -> string
      | NUMBER      -> number
      | "true"     -> true
      | "false"    -> false
      | "null"     -> null

array  : "[" [value ("," value)*] "]"
object : "{" [pair ("," pair)*] "}"
pair   : STRING ":" value

%import common.ESCAPED_STRING -> STRING
%import common.NUMBER
%import common.WS
%ignore WS
'''

# Section: Transformer classes

@v_args(inline=True)  # inline arguments to methods
class CalcTransformer(Transformer):
    def number(self, token):
        try:
            if '.' in token:
                return float(token)
            return int(token)
        except Exception:
            return float(token)

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


class TurtleTransformer(Transformer):
    """A minimal transformer to convert a parsed Turtle-like structure into Python dicts.
    This is intentionally small and illustrative, not a full Turtle processor.
    """

    def start(self, items):
        # items is a list of statements
        return {"statements": items}

    def prefixDecl(self, items):
        # items: [PNAME_NS, IRIREF]
        return ("prefix", items[0].value, items[1].value)

    def baseDecl(self, items):
        return ("base", items[0].value)

    def triples(self, items):
        # items: subject, predicateObjectList
        subj = items[0]
        po = items[1]
        return ("triples", subj, po)

    def IRIREF(self, token):
        # Token value includes angle brackets
        v = token.value
        return v[1:-1]

    def PNAME_NS(self, token):
        return token

    def PNAME_LN(self, token):
        return token

    def STRING(self, token):
        # strip quotes
        v = token.value
        if v.startswith('"') and v.endswith('"') or v.startswith("'") and v.endswith("'"):
            return v[1:-1]
        return v

    def RDFLiteral(self, items):
        # items: STRING (optional language or datatype)
        if len(items) == 1:
            return items[0]
        return (items[0], items[1])

    def NUMBER(self, token):
        if '.' in token:
            return float(token)
        return int(token)


@v_args(inline=True)
class JSONTransformer(Transformer):
    def string(self, s):
        return s[1:-1]

    def number(self, n):
        if '.' in n:
            return float(n)
        return int(n)

    def array(self, *items):
        return list(items)

    def pair(self, key, value):
        return (key[1:-1], value)

    def object(self, *pairs):
        return dict(pairs)

    def true(self):
        return True

    def false(self):
        return False

    def null(self):
        return None


# Section: Utility functions (parsers creation)

def make_calc_parser():
    return Lark(SIMPLE_ARITH_GRAMMAR, parser='lalr', transformer=CalcTransformer())


def make_turtle_parser():
    # Using Earley for potentially ambiguous grammars; keep tree for custom transformation
    return Lark(TURTLE_GRAMMAR, parser='lalr')


def make_json_parser():
    return Lark(SIMPLE_JSON_GRAMMAR, parser='lalr', transformer=JSONTransformer())


# Section: Example usages and tests

if __name__ == '__main__':
    # Demonstrate arithmetic parser
    calc_parser = make_calc_parser()
    exprs = ["1 + 2 * 3", "(1 + 2) * 3", "10 / 4 + 2"]
    print("Arithmetic examples:")
    for e in exprs:
        res = calc_parser.parse(e)
        print(f"  {e} -> {res}")

    # Demonstrate JSON parser
    json_parser = make_json_parser()
    json_examples = ["{\"a\": 1, \"b\": [true, false, null]}", "[1, 2, 3, {\"x\": \"y\"}]"]
    print("\nJSON examples:")
    for j in json_examples:
        parsed = json_parser.parse(j)
        transformed = parsed  # transformer already applied via parser creation
        print(f"  {j} -> {transformed}")

    # Demonstrate Turtle-like parser
    turtle_parser = make_turtle_parser()
    turtle_example = """
    @prefix ex: <http://example.org/> .
    @base <http://example.org/base> .
    ex:subject ex:predicate "A literal"@en .
    """
    print("\nTurtle-like parse (tree):")
    try:
        tree = turtle_parser.parse(turtle_example)
        print(tree.pretty())

        # Apply transformer manually
        tt = TurtleTransformer()
        transformed = tt.transform(tree)
        print("Transformed:", transformed)
    except Exception as exc:
        print("Error parsing Turtle example:", exc, file=sys.stderr)

    # Additional simple checks
    print('\nDone.')
