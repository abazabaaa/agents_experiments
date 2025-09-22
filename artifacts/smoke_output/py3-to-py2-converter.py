"""
Example: Python 3 -> Python 2 converter using Lark tree templates.

This script demonstrates parsing Python 3 code (with template variables of the form $var),
translating parts of the tree using tree templates, and reconstructing valid Python 2 code.

It mirrors the original notebook example from the Lark documentation.
"""

# Standard imports
from lark import Lark
from lark.tree_templates import TemplateConf, TemplateTranslator
from lark.indenter import PythonIndenter
from reconstruct_python import PythonReconstructor


# Grammar definition for templated Python (note: multi-line grammar uses r''')
TEMPLATED_PYTHON = r'''
%import python (single_input, file_input, eval_input, atom, var, stmt, expr, testlist_star_expr, _NEWLINE, _INDENT, _DEDENT, COMMENT, NAME)

%extend atom: TEMPLATE_NAME -> var

TEMPLATE_NAME: "$" NAME

?template_start: (stmt | testlist_star_expr _NEWLINE)

%ignore /[\t \f]+/          // WS
%ignore /\\[\t \f]*\r?\n/   // LINE_CONT
%ignore COMMENT
'''

# Build parser that accepts template variables
parser = Lark(
    TEMPLATED_PYTHON,
    parser='lalr',
    start=['single_input', 'file_input', 'eval_input', 'template_start'],
    postlex=PythonIndenter(),
    maybe_placeholders=False,
)


def parse_template(s):
    """Parse a string as a template (allows $var template names).

    The parser expects the input to be a template fragment, so we add a trailing newline
    and use the 'template_start' start rule.
    """
    return parser.parse(s + '\n', start='template_start')


def parse_code(s):
    """Parse full Python code (file_input start rule)."""
    return parser.parse(s + '\n', start='file_input')


# Template configuration using the parse_template function
pytemplate = TemplateConf(parse=parse_template)

# Define translations (Python 3 -> Python 2 equivalents) using templates
translations_3to2 = {
    'yield from $a':
        'for _tmp in $a: yield _tmp',

    'raise $e from $x':
        'raise $e',

    '$a / $b':
        'float($a) / $b',
}
# Parse each template string into a template tree
translations_3to2 = {pytemplate(k): pytemplate(v) for k, v in translations_3to2.items()}


# Reconstructor for outputting Python 2 code
python_reconstruct = PythonReconstructor(parser)


def translate_py3to2(code):
    """Translate Python 3 code (string) to Python 2 code (string).

    Steps:
    - parse code into a tree
    - apply template-based translations
    - reconstruct Python 2 code from the transformed tree
    """
    tree = parse_code(code)
    tree = TemplateTranslator(translations_3to2).translate(tree)
    return python_reconstruct.reconstruct(tree)


# Test/demo code
_TEST_CODE = '''
if a / 2 > 1:
    yield from [1,2,3]
else:
    raise ValueError(a) from e

'''


def test():
    print(_TEST_CODE)
    print('   ----->    ')
    print(translate_py3to2(_TEST_CODE))


def main():
    test()


if __name__ == '__main__':
    main()
