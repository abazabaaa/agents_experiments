"""
Custom SPPF Prioritizer

This example demonstrates how to subclass ForestVisitor to make a custom
SPPF node prioritizer to be used in conjunction with TreeForestTransformer.

Our prioritizer will count the number of descendants of a node that are tokens.
By negating this count, our prioritizer will prefer nodes with fewer token
descendants. Thus, we choose the more specific parse.

Converted from the Jupyter notebook: prioritizer.ipynb
"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------
from lark import Lark, Transformer, v_args  # Transformer and v_args are imported for completeness
from lark.parsers.earley_forest import ForestVisitor, TreeForestTransformer


# ------------------------------------------------------------
# Grammar definition (preserved exactly)
# ------------------------------------------------------------
GRAMMAR = r"""
start: hello " " world | hello_world
hello: "Hello"
world: "World"
hello_world: "Hello World"
"""


# ------------------------------------------------------------
# Custom prioritizer (ForestVisitor subclass)
# ------------------------------------------------------------
class TokenPrioritizer(ForestVisitor):
    """A custom SPPF prioritizer that prefers parses with fewer token descendants.

    Implementation notes:
    - Tokens do not carry a 'priority' attribute in the forest, so we count them as -1.
    - Symbol and packed nodes accumulate priorities from their children.
    - With this scheme, nodes with fewer token descendants have a higher (less negative) total priority.
    - TreeForestTransformer will then favor those alternatives.
    """

    def visit_symbol_node_in(self, node):
        # Visit the entire forest by returning node.children
        return node.children

    def visit_packed_node_in(self, node):
        return node.children

    def visit_symbol_node_out(self, node):
        priority = 0
        for child in node.children:
            # Tokens do not have a priority attribute; count them as -1
            priority += getattr(child, 'priority', -1)
        node.priority = priority

    def visit_packed_node_out(self, node):
        priority = 0
        for child in node.children:
            priority += getattr(child, 'priority', -1)
        node.priority = priority

    def on_cycle(self, node, path):
        raise Exception("Oops, we encountered a cycle.")


# ------------------------------------------------------------
# Demonstration / Main execution
# ------------------------------------------------------------
if __name__ == '__main__':
    # Build an Earley parser that produces an SPPF (ambiguity='forest')
    parser = Lark(GRAMMAR, parser='earley', ambiguity='forest')

    # Example input
    text = "Hello World"

    # Default prioritizer
    print("Default prioritizer:")
    forest = parser.parse(text)
    tree = TreeForestTransformer(resolve_ambiguity=True).transform(forest)
    print(tree.pretty())

    # Custom prioritizer
    print("Custom prioritizer:")
    forest = parser.parse(text)
    tree = TreeForestTransformer(
        resolve_ambiguity=True,
        prioritizer=TokenPrioritizer()
    ).transform(forest)
    print(tree.pretty())

    # Expected output (for reference):
    #
    # Default prioritizer:
    # start
    #   hello Hello
    #
    #   world World
    #
    # Custom prioritizer:
    # start
    #   hello_world   Hello World
