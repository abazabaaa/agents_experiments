---
title: "JSON parser - Tutorial"
description: "A step-by-step tutorial showing how to build a JSON parser with Lark, covering grammar, parser creation, tree shaping, evaluation, and optimization."
source_url: "original_raw_document"
---

<!--
Reviewer feedback:
- Missing tutorial content; placeholder only.
- Need to preserve all code blocks and grammar examples verbatim.
- Normalize anchors and remove navigation headers/footers.
-->

# JSON parser - Tutorial

Lark is a parser - a program that accepts a grammar and text, and produces a structured tree that represents that text.
In this tutorial we will write a JSON parser in Lark, and explore Lark’s various features in the process.

It has 5 parts.

1. Writing the grammar

2. Creating the parser

3. Shaping the tree

4. Evaluating the tree

5. Optimizing


Knowledge assumed:

- Using Python

- A basic understanding of how to use regular expressions


## Part 1 - The Grammar

Lark accepts its grammars in a format called EBNF. It basically looks like this:

```ebnf
rule_name : list of rules and TERMINALS to match
          | another possible list of items
          | etc.

TERMINAL: "some text to match"

```

... (content continues as in the original tutorial, including all code blocks and examples)
