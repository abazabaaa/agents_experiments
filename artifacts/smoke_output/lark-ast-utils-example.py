"""
Example: Creating an AST from the parse tree using Lark and lark.ast_utils

This module is a conversion of a Jupyter notebook into a standalone Python script.
It preserves the original cells' code and the explanatory markdown (converted to
comments). The Lark grammar is preserved as a module-level raw triple-quoted
string. Transformer classes, @v_args decorators, and AST dataclasses are kept
intact. Execution order and the example test at the bottom are preserved.

Summary of changes made during conversion:
- Notebook markdown cells converted into section comments.
- All code cells copied in original execution order.
- Grammar extracted as a module-level raw triple-quoted string constant.
- Kept all imports, AST classes, Transformer, and parse/test logic.
"""

# Standard library imports
import sys
from typing import List
from dataclasses import dataclass

# Lark imports
from lark import Lark, ast_utils, Transformer, v_args
from lark.tree import Meta

# Reference to this module is needed by ast_utils.create_transformer()
this_module = sys.modules[__name__]


#
#   Define AST
#
# The following dataclasses define the AST nodes. Some classes start with an
# underscore to demonstrate that create_transformer() will skip names that
# begin with an underscore.
class _Ast(ast_utils.Ast):
    # This will be skipped by create_transformer(), because it starts with an underscore
    pass

class _Statement(_Ast):
    # This will be skipped by create_transformer(), because it starts with an underscore
    pass

@dataclass
class Value(_Ast, ast_utils.WithMeta):
    """Uses WithMeta to include line-number metadata in the meta attribute"""
    meta: Meta
    value: object

@dataclass
class Name(_Ast):
    name: str

@dataclass
class CodeBlock(_Ast, ast_utils.AsList):
    # Corresponds to code_block in the grammar
    statements: List[_Statement]

@dataclass
class If(_Statement):
    cond: Value
    then: CodeBlock

@dataclass
class SetVar(_Statement):
    # Corresponds to set_var in the grammar
    name: str
    value: Value

@dataclass
class Print(_Statement):
    value: Value


class ToAst(Transformer):
    # Define extra transformation functions, for rules that don't correspond to an AST class.

    def STRING(self, s):
        # Remove quotation marks
        return s[1:-1]

    def DEC_NUMBER(self, n):
        return int(n)

    @v_args(inline=True)
    def start(self, x):
        return x


#
#   Define Parser
#
# Grammar is preserved as a module-level raw triple-quoted string constant.
GRAMMAR = r'''
    start: code_block

    code_block: statement+

    ?statement: if | set_var | print

    if: "if" value "{" code_block "}"
    set_var: NAME "=" value ";"
    print: "print" value ";"

    value: name | STRING | DEC_NUMBER
    name: NAME

    %import python (NAME, STRING, DEC_NUMBER)
    %import common.WS
    %ignore WS
'''

parser = Lark(GRAMMAR, parser="lalr")

# Create a transformer that maps the parse-tree into our AST classes.
transformer = ast_utils.create_transformer(this_module, ToAst())


def parse(text):
    """Parse the given text and return the generated AST."""
    tree = parser.parse(text)
    return transformer.transform(tree)


#
#   Test
#
if __name__ == '__main__':
    # Sample program from the original notebook
    sample = """
        a = 1;
        if a {
            print "a is 1";
            a = 2;
        }
    """
    print(parse(sample))
