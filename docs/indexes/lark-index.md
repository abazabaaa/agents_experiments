# Lark Parser Library Documentation Index

## Table of Contents

- [Core Documentation](#core-documentation)
- [Reference Documentation](#reference-documentation)
- [LLGuidance Extensions](#llguidance-extensions)
- [Tutorials and Guides](#tutorials-and-guides)
- [Basic Examples](#basic-examples)
- [Advanced Examples](#advanced-examples)
- [Specialized Parsers](#specialized-parsers)
- [Tools and Utilities](#tools-and-utilities)
- [Interactive Notebooks](#interactive-notebooks)

## Core Documentation

[**lark-documentation-welcome.md**](../larkdocs/lark-documentation-welcome.md)
- **Summary:** Main entry point to Lark documentation introducing the modern parsing library for Python with EBNF grammar language, multiple parsing algorithms (Earley, LALR, CYK), and automatic tree construction.
- **Related docs:** [lark-features-md.md](../larkdocs/lark-features-md.md), [how-to-use-lark-guide.md](../larkdocs/how-to-use-lark-guide.md), [lark-philosophy-md.md](../larkdocs/lark-philosophy-md.md)
- **Examples to review:** Install guide, syntax highlighting setup, and links to comprehensive tutorials and examples.

[**lark-api-reference.md**](../larkdocs/lark-api-reference.md)
- **Summary:** Complete API reference for core Lark classes including Lark parser options, Tree operations, Token handling, Transformer/Visitor patterns, exception handling, and interactive parser interfaces.
- **Related docs:** [how-to-use-lark-guide.md](../larkdocs/how-to-use-lark-guide.md), [tree-construction-reference-md.md](../larkdocs/tree-construction-reference-md.md)
- **Examples to review:** Class usage patterns, configuration options, and method examples throughout the reference.

[**how-to-use-lark-guide.md**](../larkdocs/how-to-use-lark-guide.md)
- **Summary:** Practical workflow guide covering recommended development process, debugging techniques for regex and shift/reduce collisions, strict-mode validation, and available tools including stand-alone parser generation.
- **Related docs:** [lark-api-reference.md](../larkdocs/lark-api-reference.md), [tools-nearley-md.md](../larkdocs/tools-nearley-md.md)
- **Examples to review:** Debug examples for collision detection, strict-mode usage patterns, and tool command examples.

[**lark-features-md.md**](../larkdocs/lark-features-md.md)
- **Summary:** Comprehensive overview of Lark's main features including Earley and LALR parsers, EBNF grammar support, parse tree construction, error handling, and extra features like grammar composition and Unicode support.
- **Related docs:** [lark-documentation-welcome.md](../larkdocs/lark-documentation-welcome.md), [lark-philosophy-md.md](../larkdocs/lark-philosophy-md.md)
- **Examples to review:** Feature demonstrations across the examples directory, particularly composition and visualization examples.

[**lark-philosophy-md.md**](../larkdocs/lark-philosophy-md.md)
- **Summary:** Design philosophy and principles behind Lark's architecture, explaining the choices that prioritize usability, correctness, and developer experience in the parsing library's design.
- **Related docs:** [lark-features-md.md](../larkdocs/lark-features-md.md), [how-to-develop-lark-guide-md.md](../larkdocs/how-to-develop-lark-guide-md.md)
- **Examples to review:** Philosophy is demonstrated through the clean APIs and intuitive grammar syntax shown in all examples.

[**how-to-develop-lark-guide-md.md**](../larkdocs/how-to-develop-lark-guide-md.md)
- **Summary:** Developer's guide for contributing to Lark itself, covering codebase organization, testing procedures, development setup, and guidelines for extending the library.
- **Related docs:** [lark-philosophy-md.md](../larkdocs/lark-philosophy-md.md), [how-to-use-lark-guide.md](../larkdocs/how-to-use-lark-guide.md)
- **Examples to review:** Development examples and test cases within the Lark repository structure.

## Reference Documentation

[**lark-grammar-reference.md**](../larkdocs/lark-grammar-reference.md)
- **Summary:** Complete grammar specification for Lark's EBNF syntax including rule definitions, terminal patterns, operators, priorities, and advanced features like imports and templates.
- **Related docs:** [tree-construction-reference-md.md](../larkdocs/tree-construction-reference-md.md), [grammar-composition-reference-md.md](../larkdocs/grammar-composition-reference-md.md)
- **Examples to review:** Grammar syntax examples throughout all parser examples, especially [grammar-composition-example.md](../larkdocs/grammar-composition-example.md).

[**lark-grammar-reference-md.md**](../larkdocs/lark-grammar-reference-md.md)
- **Summary:** Reference implementation demonstrating Lark's own grammar parser using LALR(1) algorithm to parse and validate multiple grammar files including Python, JSON, and other complex language grammars.
- **Related docs:** [lark-grammar-reference.md](../larkdocs/lark-grammar-reference.md), [grammar-python-parser.md](../larkdocs/grammar-python-parser.md)
- **Examples to review:** Self-parsing example showing Lark parsing its own grammar definition files.

[**tree-construction-reference-md.md**](../larkdocs/tree-construction-reference-md.md)
- **Summary:** Detailed guide to parse tree construction including tree shaping techniques, node filtering, aliasing, inlining rules, and controlling the structure of generated parse trees for optimal processing.
- **Related docs:** [lark-api-reference.md](../larkdocs/lark-api-reference.md), [creating-ast-from-parse-tree.md](../larkdocs/creating-ast-from-parse-tree.md)
- **Examples to review:** Tree shaping examples in [json-parser-tutorial.md](../larkdocs/json-parser-tutorial.md) and AST creation examples.

[**grammar-composition-reference-md.md**](../larkdocs/grammar-composition-reference-md.md)
- **Summary:** Advanced grammar composition techniques allowing modular grammar development through imports, rule inheritance, terminal sharing, and building complex parsers from reusable components.
- **Related docs:** [lark-grammar-reference.md](../larkdocs/lark-grammar-reference.md), [grammar-composition-example.md](../larkdocs/grammar-composition-example.md)
- **Examples to review:** [grammar-composition-example.md](../larkdocs/grammar-composition-example.md), [templates-example.md](../larkdocs/templates-example.md).

## LLGuidance Extensions

**Note:** The following documentation covers LLGuidance, a system that extends Lark-like syntax for constraining language model generation. These are not part of standard Lark.

[**syntax.md**](../larkdocs/syntax.md)
- **Summary:** LLGuidance variant of Lark syntax supporting inline JSON schemas, special tokens, parametric grammars, and extensions for language model constraints - not standard Lark syntax.
- **Related docs:** [parametric.md](../larkdocs/parametric.md), [special_tokens.md](../larkdocs/special_tokens.md)
- **Examples to review:** JSON schema integration examples for function calling, GBNF conversion patterns.

[**parametric.md**](../larkdocs/parametric.md)
- **Summary:** LLGuidance extension for parametric grammar rules using 64-bit parameters, enabling combinatorial structures like permutations and unique lists with bit manipulation functions.
- **Related docs:** [syntax.md](../larkdocs/syntax.md), [de_recursing.md](../larkdocs/de_recursing.md)
- **Examples to review:** Permutation grammars, unique lists, and bit-based state tracking examples.

[**special_tokens.md**](../larkdocs/special_tokens.md)
- **Summary:** LLGuidance special token handling using 0xFF marker byte for distinguishing between literal text and tokenizer special tokens in grammar constraints.
- **Related docs:** [syntax.md](../larkdocs/syntax.md), [toktrie.md](../larkdocs/toktrie.md)
- **Examples to review:** Special token marker usage in language model tokenization.

[**optimizations.md**](../larkdocs/optimizations.md)
- **Summary:** LLGuidance-specific performance optimizations for token masking, including lexer construction with derivatives, Earley parser optimizations, and slicer optimization for large masks.
- **Related docs:** [toktrie.md](../larkdocs/toktrie.md), [fast_forward.md](../larkdocs/fast_forward.md)
- **Examples to review:** MaskBench performance statistics, slicer optimization patterns.

[**de_recursing.md**](../larkdocs/de_recursing.md)
- **Summary:** Cookbook of examples for removing recursion from grammars, covering simple lists, delimited lists, and optimization techniques for better parser performance.
- **Related docs:** [syntax.md](../larkdocs/syntax.md), [parametric.md](../larkdocs/parametric.md)
- **Examples to review:** Grammar transformation patterns and recursion elimination techniques.

[**fast_forward.md**](../larkdocs/fast_forward.md)
- **Summary:** Fast-forward token implementation for language model generation with grammar constraints, covering canonical tokenization and avoiding distribution impact in LLMs.
- **Related docs:** [json_schema.md](../larkdocs/json_schema.md), [toktrie.md](../larkdocs/toktrie.md)
- **Examples to review:** Canonical tokenization algorithms, LLTokenizer usage examples.

[**json_schema.md**](../larkdocs/json_schema.md)
- **Summary:** LLGuidance JSON schema converter supporting Draft 2020-12 semantics with fixed property order, whitespace handling, and extensive feature coverage for language model constraints.
- **Related docs:** [fast_forward.md](../larkdocs/fast_forward.md), [syntax.md](../larkdocs/syntax.md)
- **Examples to review:** Schema conversion examples, property ordering rules, maskbench compatibility.

[**toktrie.md**](../larkdocs/toktrie.md)
- **Summary:** Token trie implementation for efficient token masking in LLGuidance, with DFS layout, traversal algorithm, and performance analysis for constraint-based generation.
- **Related docs:** [fast_forward.md](../larkdocs/fast_forward.md), [optimizations.md](../larkdocs/optimizations.md)
- **Examples to review:** Trie traversal algorithm, memory layout optimizations, performance benchmarks.

## Tutorials and Guides

[**json-parser-tutorial.md**](../larkdocs/json-parser-tutorial.md)
- **Summary:** Comprehensive step-by-step tutorial building a complete JSON parser from grammar design through optimization, covering tree shaping, transformers, LALR optimization, and performance benchmarking.
- **Related docs:** [simple-json-parser.md](../larkdocs/simple-json-parser.md), [simple-json-transformer-md.md](../larkdocs/simple-json-transformer-md.md)
- **Examples to review:** Complete JSON parser implementation with progressive optimization techniques and performance comparisons.

[**creating-ast-from-parse-tree.md**](../larkdocs/creating-ast-from-parse-tree.md)
- **Summary:** Tutorial demonstrating conversion of Lark parse trees into custom Abstract Syntax Tree (AST) classes using ast_utils module for type-safe tree processing and structured data representation.
- **Related docs:** [tree-construction-reference-md.md](../larkdocs/tree-construction-reference-md.md), [creating-ast-parse-tree.md](../larkdocs/creating-ast-parse-tree.md)
- **Examples to review:** [creating-ast-from-parse-notebook.py](../larkdocs/creating-ast-from-parse-notebook.py) for hands-on AST creation patterns.

[**creating-ast-parse-tree.md**](../larkdocs/creating-ast-parse-tree.md)
- **Summary:** Alternative approach to AST creation showing direct parse tree manipulation and custom transformer patterns for converting parse results into application-specific data structures.
- **Related docs:** [creating-ast-from-parse-tree.md](../larkdocs/creating-ast-from-parse-tree.md), [tree-construction-reference-md.md](../larkdocs/tree-construction-reference-md.md)
- **Examples to review:** AST transformation examples and custom visitor implementations.

[**parsing-indentation.md**](../larkdocs/parsing-indentation.md)
- **Summary:** Guide to parsing indentation-sensitive languages using Lark's Indenter class, demonstrating Python-like syntax parsing with proper INDENT/DEDENT token handling and nested block structures.
- **Related docs:** [lark-api-reference.md](../larkdocs/lark-api-reference.md) (Indenter class), [grammar-python-parser.md](../larkdocs/grammar-python-parser.md)
- **Examples to review:** [indented-tree-notebook.py](../larkdocs/indented-tree-notebook.py) for practical indentation parsing implementation.

## Basic Examples

[**basic-calculator-example.md**](../larkdocs/basic-calculator-example.md)
- **Summary:** Fundamental calculator example demonstrating basic grammar construction, arithmetic expression parsing, operator precedence, and simple transformer implementation for mathematical evaluation.
- **Related docs:** [basic-calc-parser.md](../larkdocs/basic-calc-parser.md), [json-parser-tutorial.md](../larkdocs/json-parser-tutorial.md)
- **Examples to review:** [lark-calculator-notebook.py](../larkdocs/lark-calculator-notebook.py) for interactive calculator implementation.

[**basic-calc-parser.md**](../larkdocs/basic-calc-parser.md)
- **Summary:** Simplified calculator parser focusing on core parsing concepts, grammar rules for mathematical expressions, and basic tree traversal patterns for expression evaluation.
- **Related docs:** [basic-calculator-example.md](../larkdocs/basic-calculator-example.md), [how-to-use-lark-guide.md](../larkdocs/how-to-use-lark-guide.md)
- **Examples to review:** Calculator grammar patterns and basic transformer usage examples.

[**json-parser-example.md**](../larkdocs/json-parser-example.md)
- **Summary:** Complete JSON parser implementation example showcasing grammar design, tree transformation, and validation for parsing JSON documents with proper error handling.
- **Related docs:** [json-parser-tutorial.md](../larkdocs/json-parser-tutorial.md), [simple-json-parser.md](../larkdocs/simple-json-parser.md)
- **Examples to review:** [json-parser-notebook.py](../larkdocs/json-parser-notebook.py) for interactive implementation.

[**simple-json-parser.md**](../larkdocs/simple-json-parser.md)
- **Summary:** Introductory JSON parser example showing fundamental grammar design for structured data, handling nested objects and arrays, and basic tree construction for JSON processing.
- **Related docs:** [json-parser-tutorial.md](../larkdocs/json-parser-tutorial.md), [simple-json-parser-python.md](../larkdocs/simple-json-parser-python.md)
- **Examples to review:** Simplified JSON grammar and basic parsing patterns.

[**simple-json-parser-python.md**](../larkdocs/simple-json-parser-python.md)
- **Summary:** Python-specific JSON parser implementation demonstrating integration with Python data structures, proper string handling, and conversion between JSON and Python object representations.
- **Related docs:** [simple-json-parser.md](../larkdocs/simple-json-parser.md), [simple-json-transformer-md.md](../larkdocs/simple-json-transformer-md.md)
- **Examples to review:** Python JSON parser with native type conversion examples.

[**simple-json-transformer-md.md**](../larkdocs/simple-json-transformer-md.md)
- **Summary:** JSON transformer implementation showing how to convert parse trees into Python dictionaries and lists, handling type conversions, and creating clean data processing pipelines.
- **Related docs:** [json-parser-tutorial.md](../larkdocs/json-parser-tutorial.md), [simple-json-parser-python.md](../larkdocs/simple-json-parser-python.md)
- **Examples to review:** [json-transformer-notebook.py](../larkdocs/json-transformer-notebook.py) for interactive JSON transformation.

[**turtle-dsl-example.md**](../larkdocs/turtle-dsl-example.md)
- **Summary:** Domain-Specific Language (DSL) example creating a turtle graphics language parser, demonstrating how to design grammars for command-based languages and implement interpreters.
- **Related docs:** [turtle-dsl-markdown.md](../larkdocs/turtle-dsl-markdown.md), [how-to-use-lark-guide.md](../larkdocs/how-to-use-lark-guide.md)
- **Examples to review:** [turtle-dsl-notebook.py](../larkdocs/turtle-dsl-notebook.py) for complete DSL implementation with graphics.

[**turtle-dsl-markdown.md**](../larkdocs/turtle-dsl-markdown.md)
- **Summary:** Markdown documentation for the turtle DSL showing grammar design principles for command languages, syntax specification, and integration with graphics libraries for visual output.
- **Related docs:** [turtle-dsl-example.md](../larkdocs/turtle-dsl-example.md), [lark-examples-md.md](../larkdocs/lark-examples-md.md)
- **Examples to review:** DSL command syntax and graphics generation examples.

## Advanced Examples

[**advanced-examples-md.md**](../larkdocs/advanced-examples-md.md)
- **Summary:** Gallery overview of advanced Lark examples including contextual lexers, templates, error handling, reconstruction, custom lexers, forest transformation, Python parsing, and syntax highlighting implementations.
- **Related docs:** All advanced example files listed below, [lark-features-md.md](../larkdocs/lark-features-md.md)
- **Examples to review:** Complete catalog of advanced parsing techniques and specialized implementations.

[**custom-lexer-example.md**](../larkdocs/custom-lexer-example.md)
- **Summary:** Advanced custom lexer implementation showing how to create specialized tokenization logic, handle complex token patterns, and integrate custom lexing with Lark's parsing framework.
- **Related docs:** [custom-lexer-md.md](../larkdocs/custom-lexer-md.md), [using-lexer-dynamic-complete.md](../larkdocs/using-lexer-dynamic-complete.md)
- **Examples to review:** [custom-lexer-notebook.py](../larkdocs/custom-lexer-notebook.py) for hands-on custom lexer development.

[**custom-lexer-md.md**](../larkdocs/custom-lexer-md.md)
- **Summary:** Documentation for custom lexer development covering lexer interfaces, token generation patterns, state management, and advanced tokenization techniques for complex languages.
- **Related docs:** [custom-lexer-example.md](../larkdocs/custom-lexer-example.md), [lexer-dynamic-complete-earley.md](../larkdocs/lexer-dynamic-complete-earley.md)
- **Examples to review:** Custom lexer implementations and integration patterns.

[**error-handling-interactive-parser.md**](../larkdocs/error-handling-interactive-parser.md)
- **Summary:** Interactive parser error handling demonstrating recovery strategies, error reporting, user feedback mechanisms, and graceful parsing failure management for robust parser applications.
- **Related docs:** [lark-api-reference.md](../larkdocs/lark-api-reference.md) (InteractiveParser), [how-to-use-lark-guide.md](../larkdocs/how-to-use-lark-guide.md)
- **Examples to review:** [interactive-errors-notebook.py](../larkdocs/interactive-errors-notebook.py) for interactive error handling patterns.

[**handling-ambiguity-fruit-flies-md.md**](../larkdocs/handling-ambiguity-fruit-flies-md.md)
- **Summary:** Ambiguity resolution techniques using the famous "fruit flies" example, demonstrating how to handle ambiguous grammars, parse forests, and disambiguation strategies in complex parsing scenarios.
- **Related docs:** [transform-forest-transformer-md.md](../larkdocs/transform-forest-transformer-md.md), [custom-sppf-prioritizer-md.md](../larkdocs/custom-sppf-prioritizer-md.md)
- **Examples to review:** [fruitflies-notebook.py](../larkdocs/fruitflies-notebook.py) for ambiguity handling and forest processing.

[**using-lexer-dynamic-complete.md**](../larkdocs/using-lexer-dynamic-complete.md)
- **Summary:** Advanced dynamic lexer usage showing complete tokenization exploration, handling multiple parsing paths, and comprehensive lexical analysis for complex language constructs.
- **Related docs:** [lexer-dynamic-complete-earley.md](../larkdocs/lexer-dynamic-complete-earley.md), [custom-lexer-example.md](../larkdocs/custom-lexer-example.md)
- **Examples to review:** Dynamic lexer examples with complete path exploration.

[**lexer-dynamic-complete-earley.md**](../larkdocs/lexer-dynamic-complete-earley.md)
- **Summary:** Earley parser integration with dynamic complete lexer showing advanced parsing techniques, handling complex ambiguities, and leveraging Earley's full context-free grammar capabilities.
- **Related docs:** [using-lexer-dynamic-complete.md](../larkdocs/using-lexer-dynamic-complete.md), [lark-lalr-contextual-lexer-md.md](../larkdocs/lark-lalr-contextual-lexer-md.md)
- **Examples to review:** Complex grammar parsing with dynamic lexing strategies.

[**lark-lalr-contextual-lexer-md.md**](../larkdocs/lark-lalr-contextual-lexer-md.md)
- **Summary:** LALR parser with contextual lexer implementation demonstrating context-sensitive tokenization, state-dependent lexing, and optimized parsing for performance-critical applications.
- **Related docs:** [lexer-dynamic-complete-earley.md](../larkdocs/lexer-dynamic-complete-earley.md), [custom-lexer-md.md](../larkdocs/custom-lexer-md.md)
- **Examples to review:** LALR contextual lexing examples and performance optimizations.

[**custom-sppf-prioritizer-md.md**](../larkdocs/custom-sppf-prioritizer-md.md)
- **Summary:** Shared Packed Parse Forest (SPPF) prioritization techniques for controlling ambiguity resolution in Earley parsing, implementing custom disambiguation strategies and parse tree selection.
- **Related docs:** [custom-sppf-prioritizer-md-1.md](../larkdocs/custom-sppf-prioritizer-md-1.md), [handling-ambiguity-fruit-flies-md.md](../larkdocs/handling-ambiguity-fruit-flies-md.md)
- **Examples to review:** [prioritizer-notebook.py](../larkdocs/prioritizer-notebook.py) for SPPF manipulation and prioritization.

[**custom-sppf-prioritizer-md-1.md**](../larkdocs/custom-sppf-prioritizer-md-1.md)
- **Summary:** Extended SPPF prioritizer documentation covering advanced forest manipulation, custom priority schemes, and sophisticated ambiguity resolution for complex parsing scenarios.
- **Related docs:** [custom-sppf-prioritizer-md.md](../larkdocs/custom-sppf-prioritizer-md.md), [transform-forest-transformer-md.md](../larkdocs/transform-forest-transformer-md.md)
- **Examples to review:** Advanced prioritization techniques and forest processing examples.

[**transform-forest-transformer-md.md**](../larkdocs/transform-forest-transformer-md.md)
- **Summary:** Forest transformation techniques using TreeForestTransformer for converting Earley SPPF forests into usable tree structures while preserving ambiguity information.
- **Related docs:** [transform-forest-treeforesttransformer-md.md](../larkdocs/transform-forest-treeforesttransformer-md.md), [handling-ambiguity-fruit-flies-md.md](../larkdocs/handling-ambiguity-fruit-flies-md.md)
- **Examples to review:** [tree-forest-transformer-ipynb.py](../larkdocs/tree-forest-transformer-ipynb.py) for hands-on forest transformation.

[**transform-forest-treeforesttransformer-md.md**](../larkdocs/transform-forest-treeforesttransformer-md.md)
- **Summary:** Extended TreeForestTransformer example demonstrating direct transformation of Earley SPPF forests into trees while handling complex ambiguity scenarios.
- **Related docs:** [transform-forest-transformer-md.md](../larkdocs/transform-forest-transformer-md.md), [handling-ambiguity-fruit-flies-md.md](../larkdocs/handling-ambiguity-fruit-flies-md.md)
- **Examples to review:** Advanced forest transformation patterns and ambiguity resolution techniques.

## Specialized Parsers

[**grammar-python-parser.md**](../larkdocs/grammar-python-parser.md)
- **Summary:** Complete Python grammar implementation showing how to parse full Python syntax, handle complex language constructs, and build comprehensive language processors for Python code analysis.
- **Related docs:** [reconstruct-python-example.md](../larkdocs/reconstruct-python-example.md), [py3to2-trees-templates.md](../larkdocs/py3to2-trees-templates.md)
- **Examples to review:** [reconstruct-python-notebook.py](../larkdocs/reconstruct-python-notebook.py) for Python code parsing and manipulation.

[**reconstruct-python-example.md**](../larkdocs/reconstruct-python-example.md)
- **Summary:** Python code reconstruction demonstrating how to parse Python and regenerate equivalent source code, useful for code transformation, formatting, and automated refactoring tools.
- **Related docs:** [reconstruct-python-md.md](../larkdocs/reconstruct-python-md.md), [grammar-python-parser.md](../larkdocs/grammar-python-parser.md)
- **Examples to review:** Python parsing and reconstruction with code preservation techniques.

[**reconstruct-python-md.md**](../larkdocs/reconstruct-python-md.md)
- **Summary:** Documentation for Python reconstruction techniques covering parse tree to source code conversion, preserving semantics while enabling code transformation and automated code generation.
- **Related docs:** [reconstruct-python-example.md](../larkdocs/reconstruct-python-example.md), [py3to2-tree-templates-md.md](../larkdocs/py3to2-tree-templates-md.md)
- **Examples to review:** Code reconstruction examples and transformation pipelines.

[**py3to2-trees-templates.md**](../larkdocs/py3to2-trees-templates.md)
- **Summary:** Python 3 to Python 2 converter using tree templates, demonstrating advanced code transformation, syntax migration, and automated language version conversion techniques.
- **Related docs:** [py3to2-tree-templates-md.md](../larkdocs/py3to2-tree-templates-md.md), [lark-templates-example-md.md](../larkdocs/lark-templates-example-md.md)
- **Examples to review:** [python-3-to-2-notebook-md.py](../larkdocs/python-3-to-2-notebook-md.py) for version conversion implementation.

[**py3to2-tree-templates-md.md**](../larkdocs/py3to2-tree-templates-md.md)
- **Summary:** Tree template system for Python version conversion showing pattern-based code transformation, template matching, and systematic syntax modernization or legacy conversion.
- **Related docs:** [py3to2-trees-templates.md](../larkdocs/py3to2-trees-templates.md), [templates-example.md](../larkdocs/templates-example.md)
- **Examples to review:** Template-based transformation examples and pattern matching.

[**csv-eval-transformer-md.md**](../larkdocs/csv-eval-transformer-md.md)
- **Summary:** CSV parser with evaluation transformer demonstrating structured data parsing, field validation, type conversion, and integration with data processing pipelines for CSV data analysis.
- **Related docs:** [csv-transformer-pandas-dict-md.md](../larkdocs/csv-transformer-pandas-dict-md.md), [simple-json-transformer-md.md](../larkdocs/simple-json-transformer-md.md)
- **Examples to review:** CSV parsing with data transformation and validation examples.

[**csv-transformer-pandas-dict-md.md**](../larkdocs/csv-transformer-pandas-dict-md.md)
- **Summary:** CSV to pandas DataFrame transformer showing integration with data science libraries, efficient data structure conversion, and seamless workflow integration for data analysis tasks.
- **Related docs:** [csv-eval-transformer-md.md](../larkdocs/csv-eval-transformer-md.md), [simple-json-transformer-md.md](../larkdocs/simple-json-transformer-md.md)
- **Examples to review:** CSV to pandas conversion examples and data processing workflows.

[**lark-json-reconstructor-example.md**](../larkdocs/lark-json-reconstructor-example.md)
- **Summary:** JSON reconstruction example demonstrating round-trip parsing where JSON is parsed into trees and then reconstructed back to JSON, preserving structure while enabling transformation.
- **Related docs:** [reconstruct-json-md.md](../larkdocs/reconstruct-json-md.md), [simple-json-transformer-md.md](../larkdocs/simple-json-transformer-md.md)
- **Examples to review:** [reconstruct-json-notebook.py](../larkdocs/reconstruct-json-notebook.py) for JSON round-trip processing.

[**reconstruct-json-md.md**](../larkdocs/reconstruct-json-md.md)
- **Summary:** JSON reconstruction documentation covering parse-to-source conversion, format preservation, and JSON manipulation techniques for data transformation and validation workflows.
- **Related docs:** [lark-json-reconstructor-example.md](../larkdocs/lark-json-reconstructor-example.md), [json-parser-tutorial.md](../larkdocs/json-parser-tutorial.md)
- **Examples to review:** JSON reconstruction patterns and data preservation techniques.

[**example-grammars-verilog-md.md**](../larkdocs/example-grammars-verilog-md.md)
- **Summary:** Verilog grammar example showing hardware description language parsing, demonstrating Lark's capabilities for specialized technical languages and complex syntax structures.
- **Related docs:** [lark-examples-md.md](../larkdocs/lark-examples-md.md), [grammar-composition-example.md](../larkdocs/grammar-composition-example.md)
- **Examples to review:** Verilog syntax parsing and hardware language processing examples.

## Tools and Utilities

[**standalone-example-md.md**](../larkdocs/standalone-example-md.md)
- **Summary:** Stand-alone parser generation showing how to create independent parsers from Lark grammars, enabling deployment without Lark dependencies and embedded parser applications.
- **Related docs:** [standalone-example-md-1.md](../larkdocs/standalone-example-md-1.md), [standalone-json-parser-md.md](../larkdocs/standalone-json-parser-md.md)
- **Examples to review:** Stand-alone parser generation and deployment examples.

[**standalone-example-md-1.md**](../larkdocs/standalone-example-md-1.md)
- **Summary:** Extended stand-alone parser documentation covering advanced generation options, optimization techniques, and deployment strategies for production parser applications.
- **Related docs:** [standalone-example-md.md](../larkdocs/standalone-example-md.md), [tools-nearley-md.md](../larkdocs/tools-nearley-md.md)
- **Examples to review:** Advanced stand-alone parser configurations and optimization examples.

[**standalone-json-parser-md.md**](../larkdocs/standalone-json-parser-md.md)
- **Summary:** Stand-alone JSON parser implementation demonstrating specific application of parser generation for JSON processing, creating self-contained JSON parsing modules.
- **Related docs:** [standalone-json-parser-md-1.md](../larkdocs/standalone-json-parser-md-1.md), [standalone-example-md.md](../larkdocs/standalone-example-md.md)
- **Examples to review:** JSON-specific stand-alone parser generation and usage.

[**standalone-json-parser-md-1.md**](../larkdocs/standalone-json-parser-md-1.md)
- **Summary:** Extended stand-alone JSON parser with additional features, optimization techniques, and integration patterns for high-performance JSON processing applications.
- **Related docs:** [standalone-json-parser-md.md](../larkdocs/standalone-json-parser-md.md), [json-parser-tutorial.md](../larkdocs/json-parser-tutorial.md)
- **Examples to review:** Optimized JSON parser generation and performance tuning.

[**tools-nearley-md.md**](../larkdocs/tools-nearley-md.md)
- **Summary:** Nearley.js grammar import tools allowing conversion of Nearley grammars to Lark format, enabling migration from JavaScript parsing projects and cross-platform grammar sharing.
- **Related docs:** [how-to-use-lark-guide.md](../larkdocs/how-to-use-lark-guide.md), [grammar-composition-reference-md.md](../larkdocs/grammar-composition-reference-md.md)
- **Examples to review:** Nearley grammar conversion examples and migration patterns.

[**qscintilla-json-highlighting-md.md**](../larkdocs/qscintilla-json-highlighting-md.md)
- **Summary:** QScintilla-based syntax highlighting implementation using Lark for JSON, demonstrating integration with text editors and syntax highlighting systems for enhanced code editing.
- **Related docs:** [qscintilla-json-highlight-md.md](../larkdocs/qscintilla-json-highlight-md.md), [json-parser-tutorial.md](../larkdocs/json-parser-tutorial.md)
- **Examples to review:** Syntax highlighting integration and editor enhancement examples.

[**qscintilla-json-highlight-md.md**](../larkdocs/qscintilla-json-highlight-md.md)
- **Summary:** JSON syntax highlighting with QScintilla showing specific implementation details, color schemes, and integration patterns for JSON editing environments and development tools.
- **Related docs:** [qscintilla-json-highlighting-md.md](../larkdocs/qscintilla-json-highlighting-md.md), [advanced-examples-md.md](../larkdocs/advanced-examples-md.md)
- **Examples to review:** JSON highlighting implementation and editor integration.

[**templates-example.md**](../larkdocs/templates-example.md)
- **Summary:** Template system example demonstrating Lark's template capabilities for grammar reuse, parameterized parsing, and modular grammar construction for maintainable parser development.
- **Related docs:** [lark-templates-example-md.md](../larkdocs/lark-templates-example-md.md), [grammar-composition-example.md](../larkdocs/grammar-composition-example.md)
- **Examples to review:** Template usage patterns and modular grammar development.

[**lark-templates-example-md.md**](../larkdocs/lark-templates-example-md.md)
- **Summary:** Extended template system documentation covering advanced template features, parameter substitution, and complex template hierarchies for sophisticated grammar organization.
- **Related docs:** [templates-example.md](../larkdocs/templates-example.md), [grammar-composition-reference-md.md](../larkdocs/grammar-composition-reference-md.md)
- **Examples to review:** Advanced template examples and complex grammar composition.

[**lark-examples-md.md**](../larkdocs/lark-examples-md.md)
- **Summary:** Comprehensive gallery of Lark examples covering basic to advanced use cases, serving as a central reference for implementation patterns and best practices across different parsing scenarios.
- **Related docs:** All example files, [advanced-examples-md.md](../larkdocs/advanced-examples-md.md)
- **Examples to review:** Complete example catalog spanning simple calculators to complex language processors.

## Interactive Notebooks

The following Python notebook files provide hands-on, executable examples that complement the documentation:

[**creating-ast-from-parse-notebook.py**](../larkdocs/creating-ast-from-parse-notebook.py)
- **Summary:** Interactive AST creation tutorial with executable code cells demonstrating step-by-step conversion from parse trees to custom Abstract Syntax Trees.
- **Related docs:** [creating-ast-from-parse-tree.md](../larkdocs/creating-ast-from-parse-tree.md)
- **Usage:** Hands-on AST development and testing environment.

[**custom-lexer-notebook.py**](../larkdocs/custom-lexer-notebook.py)
- **Summary:** Custom lexer development notebook with practical examples of building specialized tokenizers and integrating them with Lark parsers.
- **Related docs:** [custom-lexer-example.md](../larkdocs/custom-lexer-example.md)
- **Usage:** Interactive lexer experimentation and development.

[**error-reporting-earley-notebook.py**](../larkdocs/error-reporting-earley-notebook.py)
- **Summary:** Error reporting techniques with Earley parser in interactive format, demonstrating error recovery and user-friendly error messages.
- **Related docs:** [error-handling-interactive-parser.md](../larkdocs/error-handling-interactive-parser.md)
- **Usage:** Error handling strategy development and testing.

[**example-lark-error-lalr-notebook.py**](../larkdocs/example-lark-error-lalr-notebook.py)
- **Summary:** LALR error handling examples with interactive demonstrations of error detection, reporting, and recovery strategies.
- **Related docs:** [error-handling-interactive-parser.md](../larkdocs/error-handling-interactive-parser.md)
- **Usage:** LALR-specific error handling experimentation.

[**fruitflies-notebook.py**](../larkdocs/fruitflies-notebook.py)
- **Summary:** Interactive ambiguity handling using the classic "fruit flies" example, with hands-on forest processing and disambiguation techniques.
- **Related docs:** [handling-ambiguity-fruit-flies-md.md](../larkdocs/handling-ambiguity-fruit-flies-md.md)
- **Usage:** Ambiguity resolution experimentation and learning.

[**indented-tree-notebook.py**](../larkdocs/indented-tree-notebook.py)
- **Summary:** Indentation parsing notebook demonstrating Python-like syntax parsing with interactive examples of INDENT/DEDENT handling.
- **Related docs:** [parsing-indentation.md](../larkdocs/parsing-indentation.md)
- **Usage:** Indentation-sensitive language development.

[**interactive-errors-notebook.py**](../larkdocs/interactive-errors-notebook.py)
- **Summary:** Interactive error handling notebook with live examples of parser error scenarios and recovery mechanisms.
- **Related docs:** [error-handling-interactive-parser.md](../larkdocs/error-handling-interactive-parser.md)
- **Usage:** Error handling pattern development and testing.

[**json-parser-notebook.py**](../larkdocs/json-parser-notebook.py) and [**json-parser-notebook-1.py**](../larkdocs/json-parser-notebook-1.py)
- **Summary:** JSON parser development notebooks with step-by-step implementation, optimization, and testing of JSON parsing capabilities.
- **Related docs:** [json-parser-tutorial.md](../larkdocs/json-parser-tutorial.md)
- **Usage:** JSON parser learning and experimentation.

[**json-transformer-notebook.py**](../larkdocs/json-transformer-notebook.py)
- **Summary:** JSON transformer implementation with interactive examples of converting parse trees to Python data structures.
- **Related docs:** [simple-json-transformer-md.md](../larkdocs/simple-json-transformer-md.md)
- **Usage:** Transformer development and data conversion testing.

[**lark-calculator-notebook.py**](../larkdocs/lark-calculator-notebook.py)
- **Summary:** Calculator implementation notebook demonstrating arithmetic expression parsing and evaluation with interactive testing.
- **Related docs:** [basic-calculator-example.md](../larkdocs/basic-calculator-example.md)
- **Usage:** Basic parser development and expression evaluation.

[**notebook-dynamic-ambiguity.py**](../larkdocs/notebook-dynamic-ambiguity.py)
- **Summary:** Dynamic ambiguity handling notebook with interactive examples of resolving parsing conflicts and managing multiple interpretations.
- **Related docs:** [handling-ambiguity-fruit-flies-md.md](../larkdocs/handling-ambiguity-fruit-flies-md.md)
- **Usage:** Advanced ambiguity resolution experimentation.

[**prioritizer-notebook.py**](../larkdocs/prioritizer-notebook.py)
- **Summary:** SPPF prioritizer notebook with hands-on examples of forest manipulation and custom disambiguation strategies.
- **Related docs:** [custom-sppf-prioritizer-md.md](../larkdocs/custom-sppf-prioritizer-md.md)
- **Usage:** Forest processing and prioritization development.

[**python-3-to-2-notebook-md.py**](../larkdocs/python-3-to-2-notebook-md.py)
- **Summary:** Python version conversion notebook demonstrating code transformation and syntax migration with interactive examples.
- **Related docs:** [py3to2-trees-templates.md](../larkdocs/py3to2-trees-templates.md)
- **Usage:** Code transformation and migration tool development.

[**reconstruct-json-notebook.py**](../larkdocs/reconstruct-json-notebook.py) and [**reconstruct-python-notebook.py**](../larkdocs/reconstruct-python-notebook.py)
- **Summary:** Code reconstruction notebooks showing round-trip parsing and source code regeneration with preservation of structure and semantics.
- **Related docs:** [reconstruct-json-md.md](../larkdocs/reconstruct-json-md.md), [reconstruct-python-example.md](../larkdocs/reconstruct-python-example.md)
- **Usage:** Code analysis, transformation, and generation tool development.

[**tree-forest-transformer-ipynb.py**](../larkdocs/tree-forest-transformer-ipynb.py)
- **Summary:** Forest transformation notebook with interactive examples of processing shared packed parse forests and handling complex parsing scenarios.
- **Related docs:** [transform-forest-transformer-md.md](../larkdocs/transform-forest-transformer-md.md)
- **Usage:** Advanced parsing technique development and forest manipulation.

[**turtle-dsl-notebook.py**](../larkdocs/turtle-dsl-notebook.py)
- **Summary:** Domain-Specific Language development notebook creating a turtle graphics language with interactive graphics output and command interpretation.
- **Related docs:** [turtle-dsl-example.md](../larkdocs/turtle-dsl-example.md)
- **Usage:** DSL development and interpreter implementation with visual feedback.