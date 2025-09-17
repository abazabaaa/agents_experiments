---
title: Lark Transformers & Visitors
source_url: https://lark-parser.readthedocs.io/en/stable/visitors.html
description: Overview of Lark's Visitor, Interpreter, Transformer APIs, v_args decorator, merge_transformers utility, Discard, and VisitError.
---

# Transformers & Visitors

Transformers and Visitors provide a convenient interface to process the parse trees that Lark returns.

They are used by inheriting from the correct class (visitor or transformer) and implementing methods corresponding to the rule you wish to process. Each method accepts the children as an argument. That can be modified using the `v_args` decorator, which allows one to inline the arguments (akin to `*args`), or add the tree `meta` property as an argument.

See: https://github.com/lark-parser/lark/blob/master/lark/visitors.py

## Visitor

Visitors visit each node of the tree, and run the appropriate method on it according to the node’s data.

They work bottom-up, starting with the leaves and ending at the root of the tree.

There are two classes that implement the visitor interface:

- `Visitor`: Visit every node (without recursion)
- `Visitor_Recursive`: Visit every node using recursion. Slightly faster.

Example:

```python
class IncreaseAllNumbers(Visitor):
    def number(self, tree):
        assert tree.data == "number"
        tree.children[0] += 1

IncreaseAllNumbers().visit(parse_tree)
```

### lark.visitors.Visitor(*args, **kwds)

Tree visitor, non-recursive (can handle huge trees).

Visiting a node calls its methods (provided by the user via inheritance) according to `tree.data`.

- visit(tree: Tree[_Leaf_T]) -> Tree[_Leaf_T]
  - Visits the tree, starting with the leaves and finally the root (bottom-up)
- visit_topdown(tree: Tree[_Leaf_T]) -> Tree[_Leaf_T]
  - Visit the tree, starting at the root, and ending at the leaves (top-down)
- __default__(tree)
  - Default function that is called if there is no attribute matching `tree.data`. Can be overridden. Defaults to doing nothing.

### lark.visitors.Visitor_Recursive(*args, **kwds)

Bottom-up visitor, recursive.

Visiting a node calls its methods (provided by the user via inheritance) according to `tree.data`.

Slightly faster than the non-recursive version.

- visit(tree: Tree[_Leaf_T]) -> Tree[_Leaf_T]
  - Visits the tree, starting with the leaves and finally the root (bottom-up)
- visit_topdown(tree: Tree[_Leaf_T]) -> Tree[_Leaf_T]
  - Visit the tree, starting at the root, and ending at the leaves (top-down)
- __default__(tree)
  - Default function that is called if there is no attribute matching `tree.data`. Can be overridden. Defaults to doing nothing.

## Interpreter

### lark.visitors.Interpreter(*args, **kwds)

Interpreter walks the tree starting at the root.

Visits the tree, starting with the root and finally the leaves (top-down).

For each tree node, it calls its methods (provided by user via inheritance) according to `tree.data`.

Unlike `Transformer` and `Visitor`, the Interpreter doesn’t automatically visit its sub-branches. The user has to explicitly call `visit`, `visit_children`, or use the `@visit_children_decor`. This allows the user to implement branching and loops.

Example:

```python
class IncreaseSomeOfTheNumbers(Interpreter):
    def number(self, tree):
        tree.children[0] += 1

    def skip(self, tree):
        # skip this subtree. don't change any number node inside it.
        pass

IncreaseSomeOfTheNumbers().visit(parse_tree)
```

## Transformer

### lark.visitors.Transformer(visit_tokens: bool = True)

Transformers work bottom-up (or depth-first), starting with visiting the leaves and working their way up until ending at the root of the tree.

For each node visited, the transformer will call the appropriate method (callbacks), according to the node’s `data`, and use the returned value to replace the node, thereby creating a new tree structure.

Transformers can be used to implement map & reduce patterns. Because nodes are reduced from leaf to root, at any point the callbacks may assume the children have already been transformed (if applicable).

If the transformer cannot find a method with the right name, it will instead call `__default__`, which by default creates a copy of the node.

To discard a node, return `Discard` (`lark.visitors.Discard`).

`Transformer` can do anything `Visitor` can do, but because it reconstructs the tree, it is slightly less efficient.

A transformer without methods essentially performs a non-memoized partial deepcopy.

All these classes implement the transformer interface:

- `Transformer` — Recursively transforms the tree. This is the one you probably want.
- `Transformer_InPlace` — Non-recursive. Changes the tree in-place instead of returning new instances
- `Transformer_InPlaceRecursive` — Recursive. Changes the tree in-place instead of returning new instances

Parameters:

- visit_tokens (bool, optional) – Should the transformer visit tokens in addition to rules. Setting this to `False` is slightly faster. Defaults to `True`. (For processing ignored tokens, use the `lexer_callbacks` options)

Methods:

- transform(tree: Tree[_Leaf_T]) -> _Return_T
  - Transform the given tree, and return the final result
- __mul__(other: Union[Transformer, TransformerChain[_Leaf_U, _Return_V]]) -> TransformerChain[_Leaf_T, _Return_V]
  - Chain two transformers together, returning a new transformer.
- __default__(data, children, meta)
  - Default function that is called if there is no attribute matching `data`. Can be overridden. Defaults to creating a new copy of the tree node (i.e. `return Tree(data, children, meta)`).
- __default_token__(token)
  - Default function that is called if there is no attribute matching `token.type`. Can be overridden. Defaults to returning the token as-is.

Example:

```python
from lark import Tree, Transformer

class EvalExpressions(Transformer):
    def expr(self, args):
        return eval(args[0])

t = Tree('a', [Tree('expr', ['1+2'])])
print(EvalExpressions().transform(t))
# Prints: Tree(a, [3])
```

Another example:

```python
class T(Transformer):
    INT = int
    NUMBER = float
    def NAME(self, name):
        return lookup_dict.get(name, name)

T(visit_tokens=True).transform(tree)
```

### lark.visitors.Transformer_NonRecursive(visit_tokens: bool = True)

Same as `Transformer` but non-recursive.

Like `Transformer`, it doesn’t change the original tree.

Useful for huge trees.

### lark.visitors.Transformer_InPlace(visit_tokens: bool = True)

Same as `Transformer`, but non-recursive, and changes the tree in-place instead of returning new instances.

Useful for huge trees. Conservative in memory.

### lark.visitors.Transformer_InPlaceRecursive(visit_tokens: bool = True)

Same as `Transformer`, recursive, but changes the tree in-place instead of returning new instances.

## v_args

### lark.visitors.v_args(inline: bool = False, meta: bool = False, tree: bool = False, wrapper: Optional[Callable] = None) -> Callable

A convenience decorator factory for modifying the behavior of user-supplied visitor methods.

By default, callback methods of transformers/visitors accept one argument — a list of the node’s children.

`v_args` can modify this behavior. When used on a transformer/visitor class definition, it applies to all the callback methods inside it.

`v_args` can be applied to a single method, or to an entire class. When applied to both, the options given to the method take precedence.

Parameters:

- inline (bool, optional) – Children are provided as `*args` instead of a list argument (not recommended for very long lists).
- meta (bool, optional) – Provides two arguments: `meta` and `children` (instead of just the latter).
- tree (bool, optional) – Provides the entire tree as the argument, instead of the children.
- wrapper (function, optional) – Provide a function to decorate all methods.

Example:

```python
@v_args(inline=True)
class SolveArith(Transformer):
    def add(self, left, right):
        return left + right

    @v_args(meta=True)
    def mul(self, meta, children):
        logger.info(f'mul at line {meta.line}')
        left, right = children
        return left * right

class ReverseNotation(Transformer_InPlace):
    @v_args(tree=True)
    def tree_node(self, tree):
        tree.children = tree.children[::-1]
```

## merge_transformers

### lark.visitors.merge_transformers(base_transformer=None, **transformers_to_merge)

Merge a collection of transformers into the `base_transformer`, each into its own “namespace”.

When called, it will collect the methods from each transformer, and assign them to `base_transformer`, with their name prefixed with the given keyword, as `prefix__methodname`.

This function is especially useful for processing grammars that import other grammars, thereby creating some of their rules in a “namespace” (i.e., with a consistent name prefix). In this case, the key for the transformer should match the name of the imported grammar.

Parameters:

- base_transformer (Transformer, optional) – The transformer that all other transformers will be added to.
- **transformers_to_merge – Keyword arguments, in the form of `name_prefix = transformer`.

Raises:

- AttributeError – In case of a name collision in the merged methods

Example:

```python
class TBase(Transformer):
    def start(self, children):
        return children[0] + 'bar'

class TImportedGrammar(Transformer):
    def foo(self, children):
        return "foo"

composed_transformer = merge_transformers(TBase(), imported=TImportedGrammar())

t = Tree('start', [Tree('imported__foo', [])])

assert composed_transformer.transform(t) == 'foobar'
```

## Discard

`Discard` is the singleton instance of `_DiscardType`.

### lark.visitors._DiscardType

When the `Discard` value is returned from a transformer callback, that node is discarded and won’t appear in the parent.

Note: This feature is disabled when the transformer is provided to Lark using the `transformer` keyword (aka Tree-less LALR mode).

Example:

```python
class T(Transformer):
    def ignore_tree(self, children):
        return Discard

    def IGNORE_TOKEN(self, token):
        return Discard
```

## VisitError

### lark.exceptions.VisitError(rule, obj, orig_exc)

VisitError is raised when visitors are interrupted by an exception.

It provides the following attributes for inspection:

Parameters:

- rule – the name of the visit rule that failed
- obj – the tree-node or token that was being processed
- orig_exc – the exception that caused it to fail

Note: These parameters are available as attributes.
