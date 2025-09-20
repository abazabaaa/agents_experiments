"""
Demonstration of ambiguity handling with Lark's Earley parser.

This example parses the sentence "fruit flies like bananas" and shows
how Lark can produce explicit ambiguity results (an _ambig node).
"""

# Standard imports first
import sys
from lark import Lark, Transformer, v_args, tree

# Grammar definitions as constants
GRAMMAR = r'''
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
'''

# Transformer classes
@v_args(inline=True)
class MyTransformer(Transformer):
    pass

# Parser
parser = Lark(GRAMMAR, start='sentence', ambiguity='explicit')

sentence = 'fruit flies like bananas'

# Utilities to output graph representations (requires pydot)
def make_png(filename):
    tree.pydot__tree_to_png(parser.parse(sentence), filename)

def make_dot(filename):
    tree.pydot__tree_to_dot(parser.parse(sentence), filename)

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    print(parser.parse(sentence).pretty())
    # To produce files, pass a filename on the command line and uncomment:
    # make_png(argv[0])
    # make_dot(argv[0])


if __name__ == '__main__':
    main()

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
