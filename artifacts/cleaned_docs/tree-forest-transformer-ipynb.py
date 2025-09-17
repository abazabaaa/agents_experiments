"""
Transform a Forest (Lark SPPF example)

This script demonstrates how to subclass Lark's TreeForestTransformer to directly transform
an Earley parse forest (SPPF). It resolves the classic ambiguity in the sentence
"fruit flies like bananas" by selecting the 'simple' derivation, discards adjectives,
capitalizes tokens, and prints the resulting tree.

Converted from the notebook: tree_forest_transformer.ipynb
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from lark import Lark, Transformer, v_args  # (Transformer, v_args) imported for reference
from lark.parsers.earley_forest import TreeForestTransformer, handles_ambiguity, Discard


# ---------------------------------------------------------------------------
# Grammar Definition (preserved exactly as in the notebook)
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# Transformer that operates directly on the parse forest (SPPF)
# ---------------------------------------------------------------------------
class CustomTransformer(TreeForestTransformer):
    # When a rule is ambiguous, this method is called with all candidate trees.
    # We choose the derivation labeled 'simple'.
    @handles_ambiguity
    def sentence(self, trees):
        return next(tree for tree in trees if tree.data == 'simple')

    # Build the 'simple' sentence tree and append a '.' token to its children.
    def simple(self, children):
        children.append('.')
        return self.tree_class('simple', children)

    # Discard adjectives entirely to simplify the result.
    def adj(self, children):
        return Discard

    # Capitalize all tokens by default (Token is a str subclass in Lark).
    def __default_token__(self, token):
        return token.capitalize()


# ---------------------------------------------------------------------------
# Main execution and demonstration
# ---------------------------------------------------------------------------
def main():
    # Build a parser that returns a forest for ambiguous parses
    parser = Lark(GRAMMAR, start='sentence', ambiguity='forest')

    # Example input
    sentence = 'fruit flies like bananas'

    # Parse into an SPPF (forest)
    forest = parser.parse(sentence)

    # Transform the forest into a single tree using our custom transformer
    tree = CustomTransformer(resolve_ambiguity=False).transform(forest)

    # Pretty-print the resulting tree
    print(tree.pretty())

    # Output:
    #
    # simple
    #   noun  Flies
    #   verb  Like
    #   noun  Bananas
    #   .
    #


if __name__ == '__main__':
    main()
