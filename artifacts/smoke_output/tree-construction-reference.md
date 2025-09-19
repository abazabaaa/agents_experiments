---
title: "Tree Construction Reference"
description: "Documentation for how Lark builds parse trees from grammars: terminal filtering, rule inlining, pinning, aliasing, and examples."
source_url: "https://github.com/lark-parser/lark/blob/acfe33d943a1310f3ca26145eb2896bc5c4955c9/docs/tree_construction.md"
---

# Tree Construction Reference

Lark builds a tree automatically based on the structure of the grammar, where each rule that is matched becomes a branch (node) in the tree, and its children are its matches, in the order of matching.

For example, the rule `node: child1 child2` will create a tree node with two children. If it is matched as part of another rule (i.e. if it isn’t the root), the new rule’s tree node will become its parent.

Using `item+` or `item*` will result in a list of items, equivalent to writing `item item item ..`.

Using `item?` will return the item if it matched, or nothing.

If `maybe_placeholders=True` (the default), then using `[item]` will return the item if it matched, or the value `None`, if it didn’t.

If `maybe_placeholders=False`, then `[]` behaves like `()?`.

## Terminals

Terminals are always values in the tree, never branches.

Lark filters out certain types of terminals by default, considering them punctuation:

- Terminals that won’t appear in the tree are:

  - Unnamed literals (like `"keyword"` or `"+"`)

  - Terminals whose name starts with an underscore (like `_DIGIT`)
- Terminals that _will_ appear in the tree are:

  - Unnamed regular expressions (like `/[0-9]/`)

  - Named terminals whose name starts with a letter (like `DIGIT`)

Note: Terminals composed of literals and other terminals always include the entire match without filtering any part.

Example:

```lark
start:  PNAME pname

PNAME:  "(" NAME ")"
pname:  "(" NAME ")"

NAME:   /\w+/
%ignore /\s+/

```

Lark will parse “(Hello) (World)” as:

```text
start
    (Hello)
    pname World

```

Rules prefixed with `!` will retain all their literals regardless.

Example:

```lark
    expr: "(" expr ")"
        | NAME+

    NAME: /\w+/

    %ignore " "

```

Lark will parse “((hello world))” as:

```text
expr
    expr
        expr
            "hello"
            "world"

```

The brackets do not appear in the tree by design. The words appear because they are matched by a named terminal.

## Shaping the tree

Users can alter the automatic construction of the tree using a collection of grammar features.

### Inlining rules with `_`

Rules whose name begins with an underscore will be inlined into their containing rule.

Example:

```lark
    start: "(" _greet ")"
    _greet: /\w+/ /\w+/

```

Lark will parse “(hello world)” as:

```text
start
    "hello"
    "world"

```

### Conditionally inlining rules with `?`

Rules that receive a question mark (?) at the beginning of their definition, will be inlined if they have a single child, after filtering.

Example:

```lark
    start: greet greet
    ?greet: "(" /\w+/ ")"
          | /\w+/ /\w+/

```

Lark will parse “hello world (planet)” as:

```text
start
    greet
        "hello"
        "world"
    "planet"

```

### Pinning rule terminals with `!`

Rules that begin with an exclamation mark will keep all their terminals (they won’t get filtered).

```lark
    !expr: "(" expr ")"
         | NAME+
    NAME: /\w+/
    %ignore " "

```

Will parse “((hello world))” as:

```text
expr
  (
  expr
    (
    expr
      hello
      world
    )
  )

```

Using the `!` prefix is usually a “code smell”, and may point to a flaw in your grammar design.

### Aliasing rules

Aliases - options in a rule can receive an alias. It will be then used as the branch name for the option, instead of the rule name.

Example:

```lark
    start: greet greet
    greet: "hello"
         | "world" -> planet

```

Lark will parse “hello world” as:

```text
start
    greet
    planet

```
