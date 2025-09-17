# Python 3 to Python 2 converter (tree templates)
#
# This example demonstrates how to translate between two trees using tree templates.
# It parses Python 3, translates it to a Python 2-like AST, and then outputs the result as Python 2 code.
#
# The original notebook uses reconstruct_python.py for generating the final Python 2 code.
# This script will try to import that helper. If it's not available, it falls back to
# lark.reconstruct.Reconstructor so the script still runs end-to-end.
#
# Source notebook:
# https://lark-parser.readthedocs.io/en/stable/_downloads/c1123c2587eda70bc64752df00c577b1/py3to2.ipynb

from lark import Lark
from lark.tree_templates import TemplateConf, TemplateTranslator
from lark.indenter import PythonIndenter

# Prefer the example's specialized Python reconstructor if available.
# Fallback to the generic Lark reconstructor to keep this script runnable.
try:
    from reconstruct_python import PythonReconstructor  # Provided in Lark's examples
except Exception:
    try:
        from lark.reconstruct import Reconstructor as _Reconstructor

        class PythonReconstructor:  # Minimal compatible fallback
            def __init__(self, parser):
                self._recon = _Reconstructor(parser)

            def reconstruct(self, tree):
                return self._recon.reconstruct(tree)
    except Exception as _e:
        raise ImportError(
            "Could not import reconstructors. Ensure lark is installed, or provide reconstruct_python.py"
        ) from _e


# 1) Define a Python parser that also accepts template vars in the code (in the form of $var)
TEMPLATED_PYTHON = r"""
%import python (single_input, file_input, eval_input, atom, var, stmt, expr, testlist_star_expr, _NEWLINE, _INDENT, _DEDENT, COMMENT, NAME)

%extend atom: TEMPLATE_NAME -> var

TEMPLATE_NAME: "$" NAME

?template_start: (stmt | testlist_star_expr _NEWLINE)

%ignore /[\t \f]+/          // WS
%ignore /\\[\t \f]*\r?\n/   // LINE_CONT
%ignore COMMENT
"""

# Create a parser that can parse regular Python files and our template snippets
parser = Lark(
    TEMPLATED_PYTHON,
    parser="lalr",
    start=["single_input", "file_input", "eval_input", "template_start"],
    postlex=PythonIndenter(),
    maybe_placeholders=False,
)


def parse_template(s: str):
    """Parse a template snippet that may contain $-variables."""
    return parser.parse(s + "\n", start="template_start")


def parse_code(s: str):
    """Parse a full Python source file (or snippet) as Python code."""
    return parser.parse(s + "\n", start="file_input")


# 2) Define translations using templates (each template code is parsed to a template tree)
pytemplate = TemplateConf(parse=parse_template)

translations_3to2 = {
    # PEP 380: 'yield from x' -> simple for-loop expansion
    "yield from $a": "for _tmp in $a: yield _tmp",

    # PEP 409/415: 'raise E from cause' -> drop the cause in Py2
    "raise $e from $x": "raise $e",

    # True division -> float(...) to better match Py2 semantics
    "$a / $b": "float($a) / $b",
}

# Compile templates into tree patterns
translations_3to2 = {pytemplate(k): pytemplate(v) for k, v in translations_3to2.items()}


# 3) Translate and reconstruct Python 3 code into valid Python 2-like code
python_reconstruct = PythonReconstructor(parser)


def translate_py3to2(code: str) -> str:
    """Translate a Python 3 snippet into a Python 2-style snippet using tree templates."""
    tree = parse_code(code)
    tree = TemplateTranslator(translations_3to2).translate(tree)
    return python_reconstruct.reconstruct(tree)


# Test Code
_TEST_CODE = '''
if a / 2 > 1:
    yield from [1,2,3]
else:
    raise ValueError(a) from e

'''


def test():
    print(_TEST_CODE)
    print("   ----->    ")
    print(translate_py3to2(_TEST_CODE))


if __name__ == "__main__":
    test()
