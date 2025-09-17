# Handling Ambiguity
#
# A demonstration of ambiguity in natural-language-like input.
# This example shows how to explicitly obtain ambiguity from Lark's Earley parser.
#
# It parses the classic sentence:
#   "fruit flies like bananas"
# which has (at least) two readings:
#   - simple:      "fruit flies" (a noun phrase) + "like" (verb) + "bananas" (noun)
#   - comparative:  "fruit" (noun) + "flies" (verb) + "like" (literal) + "bananas" (noun)
# The parser is configured with ambiguity='explicit' so the result is an _ambig node
# that contains both parse trees. Printing .pretty() shows both alternatives.
#
# Optional visualization helpers are provided (PNG/DOT), which require pydot and Graphviz.
# Source: Lark docs example (fruitflies.ipynb)

import sys
from lark import Lark, tree

# Grammar:
# - Two alternative sentence structures are labeled with rule names (-> simple / -> comparative)
# - noun can be an optional adjective + NOUN
# - Tokens are fixed strings to keep the example minimal
grammar = """
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

# Create an Earley parser that keeps ambiguities explicit as a special _ambig node.
parser = Lark(grammar, start="sentence", ambiguity="explicit")

# The ambiguous input sentence
sentence = "fruit flies like bananas"

def make_png(filename: str) -> None:
    """
    Render the parse forest to a PNG image using pydot/Graphviz.
    """
    tree.pydot__tree_to_png(parser.parse(sentence), filename)

def make_dot(filename: str) -> None:
    """
    Export the parse forest to a DOT file.
    """
    tree.pydot__tree_to_dot(parser.parse(sentence), filename)

if __name__ == "__main__":
    # Print a human-readable representation of the parse forest, showing both parses.
    print(parser.parse(sentence).pretty())
    # To save a visualization, uncomment one of the following and provide a filename:
    # make_png(sys.argv[1])
    # make_dot(sys.argv[1])

# Example output:
#
# _ambig
#   comparative
#     noun    fruit
#     verb    flies
#     noun    bananas
#   simple
#     noun
#       fruit
#       flies
#     verb    like
#     noun    bananas
#
# (or view a nicer version at "./fruitflies.png")
