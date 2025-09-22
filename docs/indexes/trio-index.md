Trio and Trio-Asyncio Documentation Index
=========================================

This index highlights the local documentation for Trio and trio-asyncio, summarizes what each file covers, and points you to related references.

**Important Note:** This repository contains documentation excerpts from the Trio and trio-asyncio projects but does not include Trio-specific example code. The example references have been updated to either:
- Point to relevant OpenAI agents SDK examples that demonstrate similar async patterns
- Note when examples are available in the upstream Trio repository but not included locally

For complete Trio examples and tutorials, please refer to the official Trio repository at https://github.com/python-trio/trio.

Docs under ``docs/trio``
------------------------

[../trio/index.md](../trio/index.md)
    Summary: Main entry point to Trio documentation providing orientation to Trio's goals, supported environments, and installation instructions, with links to the tutorial and all major reference chapters.
    Related docs to review: Start with [../trio/reference-core1.md](../trio/reference-core1.md) for core concepts, then [../trio/reference-io.md](../trio/reference-io.md) for I/O operations, [../trio/reference-testing.md](../trio/reference-testing.md) for testing utilities, and [../trio/awesome-trio-libraries.md](../trio/awesome-trio-libraries.md) for ecosystem overview.
    Examples worth studying: The index serves as a roadmap to Trio's documentation. Start here to understand Trio's philosophy before diving into specific API references.

[../trio/reference-core1.md](../trio/reference-core1.md)
    Summary: Comprehensive guide to Trio's core functionality including trio.run entry point, checkpoint semantics and rules, cancellation scopes and error handling, nurseries for structured concurrency, task supervision, memory channels for inter-task communication, thread integration (to_thread/from_thread), context variables, and the complete synchronization primitive suite.
    Related docs to review: [../trio/reference-lowlevel.rst](../trio/reference-lowlevel.rst) for advanced instrumentation, [../trio/reference-testing.md](../trio/reference-testing.md) for MockClock and testing utilities, [../trio/reference-internals.md](../trio/reference-internals.md) for design philosophy behind these APIs.
    Examples worth studying: Core concepts like checkpoints, cancellation scopes, and nurseries are foundational. The documentation references examples (contextvar-example.py, channels-*.py, thread integration examples) available in the official Trio repository at github.com/python-trio/trio.

[../trio/reference-io.md](../trio/reference-io.md)
    Summary: Comprehensive I/O reference covering Trio's abstract stream API (SendStream, ReceiveStream, Stream), socket operations and SSL/TLS support, TCP/UDP networking helpers, subprocess management, file descriptor operations, and practical examples of stream adapters like SSLStream and StapledStream for building complex I/O pipelines.
    Related docs to review: [../trio/reference-testing.md](../trio/reference-testing.md) for memory and lockstep stream pairs, [../trio/reference-core1.md](../trio/reference-core1.md) for checkpoint and cancellation semantics that affect streams, [../trio/reference-lowlevel.rst](../trio/reference-lowlevel.rst) for low-level I/O primitives.
    Examples worth studying: Stream adapters like SSLStream wrapping SocketStream demonstrate Trio's composable I/O design. The documentation shows SSL-over-SSL patterns and subprocess stream handling. For complete code examples, refer to the official Trio repository.

[../trio/reference-testing.md](../trio/reference-testing.md)
    Summary: Testing utilities including the @trio_test decorator for pytest integration, MockClock for controllable time simulation with autojump capabilities, wait_all_tasks_blocked for synchronization testing, Sequencer for deterministic test ordering, memory stream pairs for in-memory stream testing, lockstep streams for protocol testing, and virtual networking infrastructure.
    Related docs to review: [../trio/reference-io.md](../trio/reference-io.md) for stream abstractions being tested, [../trio/reference-core1.md](../trio/reference-core1.md) for cancellation and checkpoint behavior during tests, [../trio/reference-lowlevel.rst](../trio/reference-lowlevel.rst) for instrumentation hooks useful in testing.
    Examples worth studying: MockClock with autojump_threshold demonstrates powerful time control for testing. Memory stream pairs enable deterministic protocol testing. Testing examples (across-realtime.py) are available in the official Trio repository.

[../trio/reference-lowlevel.rst](../trio/reference-lowlevel.rst)
    Summary: Low-level APIs for extending and introspecting Trio, including global statistics gathering, instrumentation hooks for monitoring task execution, custom clock implementations, manual cancel scope control, task and nursery introspection, custom scheduling primitives, and safe patterns for building new synchronization primitives or interfacing with C libraries and other event loops.
    Related docs to review: [../trio/reference-core1.md](../trio/reference-core1.md) for the high-level APIs built on these primitives, [../trio/reference-internals.md](../trio/reference-internals.md) for design philosophy, [../trio/reference-testing.md](../trio/reference-testing.md) for practical instrumentation usage.
    Examples worth studying: These APIs are for advanced use cases like building custom synchronization primitives or interfacing with C libraries. Study Trio's own implementation of higher-level primitives as examples.

[../trio/reference-internals.md](../trio/reference-internals.md)
    Summary: Deep dive into Trio's design philosophy prioritizing usability and correctness over raw speed, cooperative scheduling model, checkpoint semantics, cancellation propagation rules, structured concurrency principles, task lifecycle management, and the architectural decisions that shape Trio's API including the trade-offs between microbenchmark performance and real-world reliability.
    Related docs to review: [../trio/reference-core1.md](../trio/reference-core1.md) for the APIs that embody these principles, [../trio/reference-lowlevel.rst](../trio/reference-lowlevel.rst) for implementation details, [../trio/release-history.md](../trio/release-history.md) for evolution of design decisions.
    Examples worth studying: Understanding the usability-over-speed philosophy and structured concurrency principles is essential before using Trio effectively. This document explains why Trio's APIs work the way they do.

[../trio/awesome-trio-libraries.md](../trio/awesome-trio-libraries.md)
    Summary: Curated catalog of Trio-compatible third-party libraries organized by domain: web frameworks (httpx, quart-trio, hypercorn), databases (triopg, trio-mysql, redis clients), IoT (DistMQTT, asyncgpio), CLI tools (trio-click, urwid), GUI integration (QTrio), and essential development tools like cookiecutter-trio, pytest-trio, and sphinxcontrib-trio.
    Related docs to review: [../trio/reference-core1.md](../trio/reference-core1.md) for Trio's core APIs these libraries build upon, [../trio/reference-io.md](../trio/reference-io.md) for I/O patterns used by networking libraries, [../trio/reference-testing.md](../trio/reference-testing.md) for testing Trio-based libraries.
    Examples worth studying: Libraries like httpx, pytest-trio, and trio-websocket demonstrate well-designed Trio integrations. The cookiecutter-trio template provides a starting point for new projects.

[../trio/release-history.md](../trio/release-history.md)
    Summary: Towncrier-generated release notes for Trio versions (currently showing 0.30.0 and 0.29.0), documenting new features like @trio.as_safe_channel for async generator safety, bug fixes including MockClock improvements and socket compatibility, type hint updates, documentation improvements, and Python version compatibility requirements.
    Related docs to review: [../trio/reference-core1.md](../trio/reference-core1.md) and [../trio/reference-lowlevel.rst](../trio/reference-lowlevel.rst) for APIs affected by changes, [../trio/reference-internals.md](../trio/reference-internals.md) for rationale behind feature additions.
    Examples worth studying: The @trio.as_safe_channel decorator (0.30.0) addresses async generator safety. MockClock improvements and type hint updates show Trio's evolution toward better developer experience.

Docs under ``docs/trio-asyncio``
-------------------------------

[../trio-asyncio/usage.md](../trio-asyncio/usage.md)
    Summary: Practical guide for Trio-asyncio interoperability covering trio_asyncio.run and open_loop context managers for setting up dual-mode event loops, cross-domain function wrappers (aio_as_trio, trio_as_aio) for calling between frameworks, loop lifecycle management including automatic shutdown, and detailed patterns for bridging Trio and asyncio code while maintaining proper cancellation and exception propagation semantics.
    Related docs to review: [../trio-asyncio/principles.md](../trio-asyncio/principles.md) for understanding flavor distinction, [../trio/reference-core1.md](../trio/reference-core1.md) for Trio-side APIs, Python's asyncio documentation for event loop semantics.
    Examples worth studying: The trio_asyncio.run and open_loop patterns show how to integrate asyncio libraries into Trio applications. Cross-domain wrappers (aio_as_trio, trio_as_aio) enable seamless interoperability.

[../trio-asyncio/principles.md](../trio-asyncio/principles.md)
    Summary: Conceptual foundation explaining the distinction between Trio-flavored and asyncio-flavored async functions, the difference between function flavor and execution context, why flavor transitions must be explicit to maintain semantic correctness, how trio-asyncio manages dual event loop implementations, and critical error patterns that arise from mixing flavors incorrectly.
    Related docs to review: [../trio-asyncio/usage.md](../trio-asyncio/usage.md) for practical implementation patterns, [../trio/reference-core1.md](../trio/reference-core1.md) for Trio's concurrency model, [../trio/reference-internals.md](../trio/reference-internals.md) for design philosophy differences from asyncio.
    Examples worth studying: The flavor distinction is critical - mixing flavors incorrectly causes runtime errors. Study the error messages documented here to recognize and fix flavor mismatches in your code.

[../trio-asyncio/release-history.md](../trio-asyncio/release-history.md)
    Summary: Release notes for trio-asyncio versions (showing 0.15.0 and 0.14.1), documenting proper async generator finalization fixes, event loop stopping behavior improvements, Python 3.13 support addition and 3.8 removal, TrioExecutor token management fixes, and compatibility requirements with specific Trio versions.
    Related docs to review: [../trio-asyncio/usage.md](../trio-asyncio/usage.md) and [../trio-asyncio/principles.md](../trio-asyncio/principles.md) for affected APIs, [../trio/release-history.md](../trio/release-history.md) for corresponding Trio version requirements.
    Examples worth studying: Version 0.15.0's async generator finalization fixes show the complexity of bridging two async frameworks. The TrioExecutor token management fix demonstrates careful resource handling across domains.
