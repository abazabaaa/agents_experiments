"""
Handling Ambiguity

A demonstration of ambiguity

This example shows how to use get explicit ambiguity from Lark's Earley parser.
"""

# --- Imports ---------------------------------------------------------------
import sys
from lark import Lark, tree, Transformer, v_args  # Transformer/v_args imported for completeness; not used here.

# --- Grammar Definition (preserved exactly as in the notebook) -------------
GRAMMAR = r"""
    sentence: noun verb noun        -> simple
            | noun verb "like" noun -> comparative

    noun: adj? NOUN
    verb: VERB
    adj: ADJ

    NOUN: "flies" | "bananas" | "fruit"
    VERB: "like" | "flies"
    ADJ: "fruit"

    %import common.WS
    %ignore WS
"""

# --- Parser Setup: Earley parser with explicit ambiguity -------------------
parser = Lark(GRAMMAR, start='sentence', ambiguity='explicit')

# --- Example input from the notebook --------------------------------------
sentence = 'fruit flies like bananas'

# --- Helper functions to export the parse forest using pydot/graphviz ------

def make_png(filename: str) -> None:
    """Write the parse forest to a PNG image (requires pydot and Graphviz)."""
    tree.pydot__tree_to_png(parser.parse(sentence), filename)


def make_dot(filename: str) -> None:
    """Write the parse forest to a DOT file (requires pydot and Graphviz)."""
    tree.pydot__tree_to_dot(parser.parse(sentence), filename)

# --- Main demonstration -----------------------------------------------------
if __name__ == '__main__':
    # Print the parse forest with explicit ambiguity
    print(parser.parse(sentence).pretty())

    # You can also render the parse forest; pass an output path as the first CLI arg:
    # make_png(sys.argv[1])
    # make_dot(sys.argv[1])

    # Output:
    #
    # _ambig
    #   comparative
    #     noun	fruit
    #     verb	flies
    #     noun	bananas
    #   simple
    #     noun
    #       fruit
    #       flies
    #     verb	like
    #     noun	bananas
    #
    # (or view a nicer version at "./fruitflies.png")
