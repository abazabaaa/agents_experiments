---
title: Lark API Reference (Stable)
source_url: https://lark-parser.readthedocs.io/en/stable/classes.html
description: Cleaned and normalized API reference for Lark core classes and utilities, including Lark, Tree, Token, InteractiveParser, ast_utils, and Indenter.
---

# API Reference

## Lark

class lark.Lark(grammar: Union[Grammar, str, IO[str]], **options)

Main interface for the library.

It’s mostly a thin wrapper for the many different parsers, and for the tree constructor.

Parameters:
- grammar – a string or file-object containing the grammar spec (using Lark’s EBNF syntax)
- options – a dictionary controlling various aspects of Lark.

Example

```python
>>> Lark(r'''start: "foo" ''')
Lark(...)
```

General Options

- start: The start symbol. Either a string, or a list of strings for multiple possible starts (Default: "start").
- debug: Display debug information and extra warnings. Use only when debugging (Default: False). When used with Earley, it generates a forest graph as "sppf.png", if 'dot' is installed.
- strict: Throw an exception on any potential ambiguity, including shift/reduce conflicts, and regex collisions.
- transformer: Applies the transformer to every parse tree (equivalent to applying it after the parse, but faster).
- propagate_positions: Propagates positional attributes into the 'meta' attribute of all tree branches. Sets attributes: (line, column, end_line, end_column, start_pos, end_pos, container_line, container_column, container_end_line, container_end_column). Accepts False, True, or a callable filter.
- maybe_placeholders: When True, the [] operator returns None when not matched. When False, [] behaves like the ? operator, and returns no value at all. (Default: True)
- cache: Cache the results of the Lark grammar analysis, for 2x–3x faster loading. LALR only for now.
  - False: no caching (default)
  - True: cache to a temporary file in the local directory
  - str: cache to the given path
- regex: When True, uses the regex module instead of the stdlib re.
- g_regex_flags: Flags that are applied to all terminals (both regex and strings).
- keep_all_tokens: Prevent the tree builder from automatically removing punctuation tokens (Default: False).
- tree_class: Lark will produce trees comprised of instances of this class instead of the default lark.Tree.

Algorithm Options

- parser: Decides which parser engine to use. Accepts "earley" or "lalr". (Default: "earley"). There is also a legacy "cyk" option.
- lexer: Decides whether or not to use a lexer stage.
  - "auto" (default): Choose based on the parser
  - "basic": Use a basic lexer
  - "contextual": Stronger lexer (only with parser="lalr")
  - "dynamic": Flexible and powerful (only with parser="earley")
  - "dynamic_complete": Same as dynamic, but tries every variation of tokenizing possible
- ambiguity: Decides how to handle ambiguity in the parse. Only relevant if parser="earley".
  - "resolve": Automatically choose the simplest derivation (greedy for tokens, non-greedy for rules)
  - "explicit": Return all derivations wrapped in "_ambig" tree nodes (i.e., a forest)
  - "forest": Return the root of the shared packed parse forest (SPPF)

Misc. / Domain Specific Options

- postlex: Lexer post-processing (Default: None). Only works with the basic and contextual lexers.
- priority: How priorities should be evaluated - "auto", None, "normal", "invert" (Default: "auto").
- lexer_callbacks: Dictionary of callbacks for the lexer. May alter tokens during lexing. Use with caution.
- use_bytes: Accept an input of type bytes instead of str.
- ordered_sets: Should Earley use ordered-sets to achieve stable output (~10% slower than regular sets. Default: True).
- edit_terminals: A callback for editing the terminals before parse.
- import_paths: A list of either paths or loader functions to specify from where grammars are imported.
- source_path: Override the source of from where the grammar was loaded. Useful for relative imports and unconventional grammar loading.

End of Options

save(f, exclude_options: Collection[str] = ()) → None

Saves the instance into the given file object. Useful for caching and multiprocessing.

classmethod load(f) → T

Loads an instance from the given file object. Useful for caching and multiprocessing.

classmethod open(grammar_filename: str, rel_to: Optional[str] = None, **options) → T

Create an instance of Lark with the grammar given by its filename. If rel_to is provided, the function will find the grammar filename in relation to it.

Example

```python
>>> Lark.open("grammar_file.lark", rel_to=__file__, parser="lalr")
Lark(...)
```

classmethod open_from_package(package: str, grammar_path: str, search_paths: Sequence[str] = [''], **options) → T

Create an instance of Lark with the grammar loaded from within the given package. This allows grammar loading from zipapps. Imports in the grammar will use the package and search_paths provided, through FromPackageLoader.

Example

```python
Lark.open_from_package(__name__, "example.lark", ("grammars",), parser="...")
```

lex(text: str, dont_ignore: bool = False) → Iterator[Token]

Only lex (and postlex) the text, without parsing it. Only relevant when lexer='basic'. When dont_ignore=True, the lexer will return all tokens, even those marked for %ignore.

Raises: UnexpectedCharacters – In case the lexer cannot find a suitable match.

get_terminal(name: str) → TerminalDef

Get information about a terminal.

parse_interactive(text: Optional[str] = None, start: Optional[str] = None) → InteractiveParser

Start an interactive parsing session.

Parameters:
- text (optional) – Text to be parsed. Required for resume_parse().
- start (optional) – Start symbol.

Returns: A new InteractiveParser instance.

See also: Lark.parse()

parse(text: str, start: Optional[str] = None, on_error: Optional[Callable[[UnexpectedInput], bool]] = None) → ParseTree

Parse the given text, according to the options provided.

Parameters:
- text – Text to be parsed.
- start (optional) – Required if Lark was given multiple possible start symbols (using the start option).
- on_error (optional) – If provided, will be called on UnexpectedToken error. Return True to resume parsing. LALR only. See examples/advanced/error_handling.py for usage.

Returns: If a transformer is supplied to __init__, returns the transformation result. Otherwise, returns a Tree instance.

Raises: UnexpectedInput – On a parse error, one of these sub-exceptions will rise: UnexpectedCharacters, UnexpectedToken, or UnexpectedEOF. These also inherit from ParserError and LexerError.

### Using Unicode character classes with regex

Python’s builtin re module has known bugs and won’t parse advanced regex features such as character classes. With `pip install lark[regex]`, the regex module will be installed alongside lark and can act as a drop-in replacement to re.

Any instance of Lark instantiated with regex=True will use the regex module instead of re.

For example, character classes to match PEP-3131 compliant Python identifiers:

```python
from lark import Lark

>>> g = Lark(r"""
                    ?start: NAME
                    NAME: ID_START ID_CONTINUE*
                    ID_START: /[\p{Lu}\p{Ll}\p{Lt}\p{Lm}\p{Lo}\p{Nl}_]+/
                    ID_CONTINUE: ID_START | /[\p{Mn}\p{Mc}\p{Nd}\p{Pc}·]+/
                """, regex=True)

>>> g.parse('வணக்கம்')
'வணக்கம்'
```

## Tree

class lark.Tree(data: str, children: List[Union[_Leaf_T, Tree[_Leaf_T]]], meta: Optional[Meta] = None)

The main tree class.

Creates a new tree, and stores data and children in attributes of the same name. Trees can be hashed and compared.

Parameters:
- data – The name of the rule or alias
- children – List of matched sub-rules and terminals
- meta – Line & Column numbers (if propagate_positions is enabled).
  - meta attributes: (line, column, end_line, end_column, start_pos, end_pos, container_line, container_column, container_end_line, container_end_column)

container_* attributes consider all symbols, including those that have been inlined in the tree. For example, in the rule `a: _A B _C`, the regular attributes will mark the start and end of `B`, but the container_* attributes will also include `_A` and `_C` in the range. However, rules that contain `a` will consider it in full, including `_A` and `_C` for all attributes.

pretty(indent_str: str = '') → str

Returns an indented string representation of the tree. Great for debugging.

__rich__(parent: Optional[rich.tree.Tree] = None) → rich.tree.Tree

Returns a tree widget for the 'rich' library.

Example

```python
from rich import print
from lark import Tree

tree = Tree('root', ['node1', 'node2'])
print(tree)
```

iter_subtrees() → Iterator[Tree[_Leaf_T]]

Depth-first iteration. Iterates over all the subtrees, never returning to the same node twice (Lark’s parse-tree is actually a DAG).

iter_subtrees_topdown()

Breadth-first iteration. Iterates over all the subtrees, returning nodes in the same order as pretty().

find_pred(pred: Callable[[Tree[_Leaf_T]], bool]) → Iterator[Tree[_Leaf_T]]

Returns all nodes of the tree that evaluate pred(node) as true.

find_data(data: str) → Iterator[Tree[_Leaf_T]]

Returns all nodes of the tree whose data equals the given data.

scan_values(pred: Callable[[Union[_Leaf_T, Tree[_Leaf_T]]], bool]) → Iterator[_Leaf_T]

Return all values in the tree that evaluate pred(value) as true. This can be used to find all the tokens in the tree.

Example

```python
>>> all_tokens = tree.scan_values(lambda v: isinstance(v, Token))
```

## Token

class lark.Token(type: str, value: Any, start_pos: Optional[int] = None, line: Optional[int] = None, column: Optional[int] = None, end_line: Optional[int] = None, end_column: Optional[int] = None, end_pos: Optional[int] = None)

A string with meta-information, produced by the lexer.

When parsing text, the resulting chunks of the input that haven’t been discarded will end up in the tree as Token instances. Token inherits from Python’s str, so normal string comparisons and operations work as expected.

Attributes:
- type (str): Name of the token (as specified in grammar)
- value (Any): Value of the token (redundant, as token.value == token)
- start_pos (Optional[int]): The index of the token in the text
- line (Optional[int]): The line of the token in the text (starting with 1)
- column (Optional[int]): The column of the token in the text (starting with 1)
- end_line (Optional[int]): The line where the token ends
- end_column (Optional[int]): The next column after the end of the token
- end_pos (Optional[int]): The index where the token ends (start_pos + len(token))

## Transformer, Visitor & Interpreter

See Transformers & Visitors: https://lark-parser.readthedocs.io/en/stable/visitors.html

## ForestVisitor, ForestTransformer, & TreeForestTransformer

See Working with the SPPF: https://lark-parser.readthedocs.io/en/stable/forest.html

## UnexpectedInput

class lark.exceptions.UnexpectedInput

UnexpectedInput error.

Used as a base class for the following exceptions:
- UnexpectedCharacters: The lexer encountered an unexpected string
- UnexpectedToken: The parser received an unexpected token
- UnexpectedEOF: The parser expected a token, but the input ended

After catching one of these exceptions, you may call the following helper methods to create a nicer error message.

get_context(text: str, span: int = 40) → str

Returns a pretty string pinpointing the error in the text, with span amount of context characters around it.

Note: The parser doesn’t hold a copy of the text it has to parse, so you have to provide it again.

match_examples(parse_fn: Callable[[str], Tree], examples: Union[Mapping[T, Iterable[str]], Iterable[Tuple[T, Iterable[str]]]], token_type_match_fallback: bool = False, use_accepts: bool = True) → Optional[T]

Detect what’s wrong in the input text by matching against example errors.

Given a parser instance and a dictionary mapping some label with malformed syntax examples, it returns the label for the example that best matches the current error. Iterates until it finds a matching error and returns the corresponding value.

For an example usage, see examples/error_reporting_lalr.py

Parameters:
- parse_fn – parse function (usually lark_instance.parse)
- examples – dictionary of {'example_string': value}
- use_accepts – Recommended to keep as True

class lark.exceptions.UnexpectedToken(token, expected, considered_rules=None, state=None, interactive_parser=None, terminals_by_name=None, token_history=None)

Raised by the parser when the token it received doesn’t match any valid step forward.

Parameters:
- token – The mismatched token
- expected – The set of expected tokens
- considered_rules – Which rules were considered, to deduce the expected tokens
- state – A value representing the parser state. Do not rely on its value or type.
- interactive_parser – An instance of InteractiveParser, initialized to the point of failure, for debugging and error handling.

Note: These parameters are available as attributes of the instance.

class lark.exceptions.UnexpectedCharacters(seq, lex_pos, line, column, allowed=None, considered_tokens=None, state=None, token_history=None, terminals_by_name=None, considered_rules=None)

Raised by the lexer when it cannot match the next string of characters to any of its terminals.

class lark.exceptions.UnexpectedEOF(expected, state=None, terminals_by_name=None)

Raised by the parser when the input ends while it still expects a token.

## InteractiveParser

class lark.parsers.lalr_interactive_parser.InteractiveParser(parser, parser_state: ParserState, lexer_thread: LexerThread)

InteractiveParser gives you advanced control over parsing and error handling when parsing with LALR.

For a simpler interface, see the on_error argument to Lark.parse().

feed_token(token: Token)

Feed the parser with a token, and advance it to the next state, as if it received it from the lexer. Note that token has to be an instance of Token.

exhaust_lexer() → List[Token]

Try to feed the rest of the lexer state into the interactive parser. Note that this modifies the instance in place and does not feed an '$END' Token.

as_immutable()

Convert to an ImmutableInteractiveParser.

pretty()

Print the output of choices() in a way that’s easier to read.

choices()

Returns a dictionary of token types matched to their action in the parser. Only returns token types that are accepted by the current state. Updated by feed_token().

accepts()

Returns the set of possible tokens that will advance the parser into a new valid state.

resume_parse()

Resume automated parsing from the current state.

class lark.parsers.lalr_interactive_parser.ImmutableInteractiveParser(parser, parser_state: ParserState, lexer_thread: LexerThread)

Same as InteractiveParser, but operations create a new instance instead of changing it in-place.

feed_token(token)

Feed the parser with a token, and advance it to the next state, as if it received it from the lexer. Note that token has to be an instance of Token.

exhaust_lexer()

Try to feed the rest of the lexer state into the parser. Returns a new ImmutableInteractiveParser and does not feed an '$END' Token.

as_mutable()

Convert to an InteractiveParser.

choices()

Returns a dictionary of token types matched to their action in the parser. Only returns token types that are accepted by the current state. Updated by feed_token().

pretty()

Print the output of choices() in a way that’s easier to read.

resume_parse()

Resume automated parsing from the current state.

accepts()

Returns the set of possible tokens that will advance the parser into a new valid state.

## ast_utils

For an example of using ast_utils, see /examples/advanced/create_ast.py: https://lark-parser.readthedocs.io/en/stable/examples/advanced/create_ast.html

class lark.ast_utils.Ast

Abstract class. Subclasses will be collected by create_transformer().

class lark.ast_utils.AsList

Abstract class. Subclasses will be instantiated with the parse results as a single list, instead of as arguments.

lark.ast_utils.create_transformer(ast_module: module, transformer: Optional[lark.visitors.Transformer] = None, decorator_factory: Callable = v_args) → Transformer

Collects Ast subclasses from the given module, and creates a Lark transformer that builds the AST.

For each class, a corresponding rule is created in the transformer, with a matching name. CamelCase names will be converted into snake_case. Example: CodeBlock -> code_block.

Classes starting with an underscore (_) will be skipped.

Parameters:
- ast_module – A Python module containing all the subclasses of ast_utils.Ast
- transformer (optional) – An initial transformer. Its attributes may be overwritten.
- decorator_factory (Callable) – Optional callable accepting two booleans, inline and meta, and returning a decorator for the methods of transformer (default: v_args).

## Indenter

class lark.indenter.Indenter

Postlexer that injects indent/dedent tokens based on indentation.

It keeps track of the current indentation, as well as the current level of parentheses. Inside parentheses, the indentation is ignored, and no indent/dedent tokens get generated.

Note: This is an abstract class. To use it, inherit and implement all its abstract methods:
- tab_len
- NL_type
- OPEN_PAREN_types, CLOSE_PAREN_types
- INDENT_type, DEDENT_type

See also: the postlex option in Lark.

class lark.indenter.PythonIndenter

A postlexer that injects _INDENT/_DEDENT tokens based on indentation, according to the Python syntax.

See also: the postlex option in Lark.
