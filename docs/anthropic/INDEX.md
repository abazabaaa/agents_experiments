# Anthropic Documentation Index

This comprehensive index provides navigation for the complete Anthropic documentation set, covering the Claude Developer Platform, Claude Code, API reference, and extensive resources for building with Claude.

## Table of Contents

- [Quick Start & Overview](#quick-start--overview)
- [API Reference](#api-reference)
- [Core Platform Features](#core-platform-features)
- [Tool Use & Agents](#tool-use--agents)
- [Prompt Engineering](#prompt-engineering)
- [Claude Code Terminal Tool](#claude-code-terminal-tool)
- [Model Information](#model-information)
- [Administration & Management](#administration--management)
- [Resources & Learning Materials](#resources--learning-materials)
- [Release Notes & Updates](#release-notes--updates)
- [Key Topics Index](#key-topics-index)

---

## Quick Start & Overview

### Getting Started
- **Path**: `./docs/get-started.md`
- **Summary**: Complete quickstart guide with API calls in multiple languages. Shows how to build a simple web search assistant using Claude API.
- **Examples**: cURL, Python, TypeScript, and Java code examples for first API integration

### Platform Overview
- **Path**: `./home.md`
- **Summary**: Landing page overview of Claude Developer Platform and Claude Code. Provides high-level navigation to key features and learning resources.
- **Related**: Links to Console, API reference, courses, and cookbooks

### Features Overview
- **Path**: `./docs/build-with-claude/overview.md`
- **Summary**: Comprehensive table of Claude's advanced capabilities including 1M context, batch processing, citations, extended thinking, and tool use. Details availability across platforms.
- **Cross-References**: Links to detailed guides for each feature listed

---

## API Reference

### Core API
- **Path**: `./api/overview.md`
- **Summary**: Fundamental API concepts including authentication, content types, request limits, and basic examples. Essential reference for any API integration.
- **Examples**: Authentication headers, basic message creation in multiple languages

- **Path**: `./api/messages.md`
- **Summary**: Complete Messages API reference covering conversation patterns, streaming, and advanced message formatting. Core API for Claude interactions.
- **Examples**: Single messages, conversations, streaming responses, image inputs

### Authentication & Security
- **Path**: `./api/beta-headers.md`
- **Summary**: Beta feature access through special headers. Covers experimental features and version-specific functionality.

- **Path**: `./api/errors.md`
- **Summary**: Complete error handling guide with HTTP status codes, error types, and troubleshooting strategies. Essential for robust API integrations.
- **Examples**: Error response formats, rate limiting, request size limits

### Platform Integrations
- **Path**: `./api/claude-on-amazon-bedrock.md`
- **Summary**: Guide for using Claude through Amazon Bedrock. Covers model access, authentication, and platform-specific considerations.

- **Path**: `./api/claude-on-vertex-ai.md`
- **Summary**: Google Cloud Vertex AI integration for Claude models. Details setup, authentication, and regional availability.

- **Path**: `./api/openai-sdk.md`
- **Summary**: Using Claude API with OpenAI-compatible SDK for easy migration from OpenAI. Covers compatibility layer and differences.

- **Path**: `./api/client-sdks.md`
- **Summary**: Official client libraries in Python, TypeScript, and other languages for easier API integration.

### API Development & Tools

- **Path**: `./api/messages-examples.md`
- **Summary**: Comprehensive examples of Messages API usage patterns, from basic to advanced scenarios.

- **Path**: `./api/messages-count-tokens.md`
- **Summary**: Token counting utilities for estimating API costs and managing context windows.

- **Path**: `./api/handling-stop-reasons.md`
- **Summary**: Understanding and handling different stop reasons in API responses for robust implementations.

- **Path**: `./api/versioning.md`
- **Summary**: API versioning strategy and migration guides for maintaining stable integrations.

- **Path**: `./api/ip-addresses.md`
- **Summary**: IP allowlisting and network configuration for enterprise deployments.

- **Path**: `./api/models.md`
- **Summary**: Detailed model specifications including capabilities, limits, and pricing tiers.

- **Path**: `./api/models-list.md`
- **Summary**: Complete list of available models with their identifiers and characteristics.

- **Path**: `./api/migrating-from-text-completions-to-messages.md`
- **Summary**: Migration guide from legacy text completion API to modern Messages API.

- **Path**: `./api/getting-help.md`
- **Summary**: Support resources and troubleshooting guides for API developers.

### Batch Processing APIs

- **Path**: `./api/messages-batch-examples.md`
- **Summary**: Examples and patterns for batch message processing with cost optimization.

- **Path**: `./api/canceling-message-batches.md`
- **Summary**: How to cancel in-progress batch operations and handle partial results.

- **Path**: `./api/deleting-message-batches.md`
- **Summary**: Clean up completed batch jobs and manage storage resources.

- **Path**: `./api/retrieving-message-batch-results.md`
- **Summary**: Retrieve and process results from completed batch operations.

### Prompt Tools API

- **Path**: `./api/prompt-tools-generate.md`
- **Summary**: AI-powered prompt generation tool for creating effective prompts from descriptions.

- **Path**: `./api/prompt-tools-improve.md`
- **Summary**: Automated prompt improvement tool that optimizes existing prompts for better performance.

- **Path**: `./api/prompt-tools-templatize.md`
- **Summary**: Convert static prompts into reusable templates with variables and placeholders.

### Analytics & Monitoring

- **Path**: `./api/claude-code-analytics-api.md`
- **Summary**: Track and analyze Claude Code usage, performance metrics, and cost data.

### Operational APIs
- **Path**: `./api/usage-cost-api.md`
- **Summary**: Track API usage and costs programmatically. Essential for monitoring and budget management in production applications.

- **Path**: `./api/administration-api.md`
- **Summary**: Organization and workspace management APIs. Covers user management, workspace creation, and administrative operations.

---

## Core Platform Features

### Advanced Capabilities

#### Batch Processing
- **Path**: `./docs/build-with-claude/batch-processing.md`
- **Summary**: Process large volumes of requests asynchronously with 50% cost savings. Ideal for bulk operations and non-real-time processing.
- **Related APIs**: `./api/creating-message-batches.md`, `./api/listing-message-batches.md`, `./api/retrieving-message-batches.md`

#### Context Windows
- **Path**: `./docs/build-with-claude/context-windows.md`
- **Summary**: Leverage extended context windows up to 1M tokens for processing large documents and maintaining long conversations.
- **Examples**: Large document analysis, extended conversation patterns

#### Prompt Caching
- **Path**: `./docs/build-with-claude/prompt-caching.md`
- **Summary**: Optimize costs and latency by caching frequently used prompt prefixes. Supports both 5-minute and 1-hour cache durations.
- **Examples**: System prompt caching, document analysis workflows

#### Extended Thinking
- **Path**: `./docs/build-with-claude/extended-thinking.md`
- **Summary**: Enhanced reasoning capabilities that show Claude's step-by-step thought process before delivering final answers.
- **Use Cases**: Complex problem solving, detailed analysis, transparent reasoning

### File and Content Handling

#### Files API
- **Path**: `./docs/build-with-claude/files.md`
- **Summary**: Upload and manage files for use with Claude without re-uploading content. Supports PDFs, images, and text files.
- **Related APIs**: `./api/files-create.md`, `./api/files-list.md`, `./api/files-metadata.md`, `./api/files-content.md`, `./api/files-delete.md`

#### PDF Support
- **Path**: `./docs/build-with-claude/pdf-support.md`
- **Summary**: Process and analyze both text and visual content from PDF documents. Handles complex layouts and multi-page documents.

#### Citations
- **Path**: `./docs/build-with-claude/citations.md`
- **Summary**: Ground Claude's responses in source documents with detailed references. Enables verifiable, trustworthy outputs for RAG applications.

### Developer Tools

#### Embeddings
- **Path**: `./docs/build-with-claude/embeddings.md`
- **Summary**: Text embedding capabilities for semantic search, clustering, and similarity analysis. Essential for RAG and content organization.

#### Streaming
- **Path**: `./docs/build-with-claude/streaming.md`
- **Summary**: Real-time response streaming for improved user experience. Covers server-sent events and partial response handling.

#### Vision & Multimodal
- **Path**: `./docs/build-with-claude/vision.md`
- **Summary**: Image understanding and visual analysis capabilities. Process and analyze images alongside text.

#### Additional Features
- **Path**: `./docs/build-with-claude/multilingual-support.md`
- **Summary**: Claude's multilingual capabilities and best practices for non-English languages.

- **Path**: `./docs/build-with-claude/token-counting.md`
- **Summary**: Tools and techniques for counting tokens to manage costs and context limits.

- **Path**: `./docs/build-with-claude/search-results.md`
- **Summary**: Processing and understanding search results with Claude for enhanced responses.

---

## Tool Use & Agents

### Core Tool Use
- **Path**: `./docs/agents-and-tools/tool-use/overview.md`
- **Summary**: Comprehensive guide to Claude's tool use capabilities. Covers both client-side and server-side tools with complete workflow examples.
- **Examples**: Weather tool, JSON mode, parallel tool use, sequential tool chains

- **Path**: `./docs/agents-and-tools/tool-use/implement-tool-use.md`
- **Summary**: Detailed implementation guide for custom tools. Covers schema definition, execution patterns, and error handling best practices.

### Built-in Tools

#### Computer Use
- **Path**: `./docs/agents-and-tools/tool-use/computer-use-tool.md`
- **Summary**: Control computer interfaces through screenshots and mouse/keyboard commands. Enables automation of GUI applications.

#### Code Execution
- **Path**: `./docs/agents-and-tools/tool-use/code-execution-tool.md`
- **Summary**: Run Python code in sandboxed environment for data analysis and computation. Ideal for dynamic analysis and calculations.

#### Web Tools
- **Path**: `./docs/agents-and-tools/tool-use/web-search-tool.md`
- **Summary**: Augment Claude with real-time web search capabilities. Access current information beyond training data.

- **Path**: `./docs/agents-and-tools/tool-use/web-fetch-tool.md`
- **Summary**: Retrieve and analyze content from specific web pages and PDF documents. Enables detailed content analysis.

#### Development Tools
- **Path**: `./docs/agents-and-tools/tool-use/bash-tool.md`
- **Summary**: Execute bash commands and scripts for system operations. Enables command-line automation and system interactions.

- **Path**: `./docs/agents-and-tools/tool-use/text-editor-tool.md`
- **Summary**: Create and edit text files with built-in text editor interface. Supports file manipulation and content creation tasks.

### Advanced Tool Features
- **Path**: `./docs/agents-and-tools/tool-use/fine-grained-tool-streaming.md`
- **Summary**: Stream tool parameters without buffering for reduced latency. Optimizes large parameter handling in tool execution.

- **Path**: `./docs/agents-and-tools/tool-use/token-efficient-tool-use.md`
- **Summary**: Optimize token usage in tool interactions. Strategies for minimizing costs while maintaining functionality.

### MCP (Model Context Protocol)
- **Path**: `./docs/agents-and-tools/mcp-connector.md`
- **Summary**: Connect to remote MCP servers directly from Messages API. Enables integration with external tool ecosystems without separate clients.

- **Path**: `./docs/agents-and-tools/remote-mcp-servers.md`
- **Summary**: Deploy and manage remote MCP servers for distributed tool architectures. Covers scaling and deployment patterns.

### Additional Tools
- **Path**: `./docs/agents-and-tools/claude-for-sheets.md`
- **Summary**: Claude integration for Google Sheets. Add AI capabilities to spreadsheets.

---

## Prompt Engineering

### Core Techniques
- **Path**: `./docs/build-with-claude/prompt-engineering/overview.md`
- **Summary**: Systematic approach to prompt engineering with techniques ordered by effectiveness. Essential guide for optimizing Claude performance.

- **Path**: `./docs/build-with-claude/prompt-engineering/be-clear-and-direct.md`
- **Summary**: Fundamental clarity principles for effective prompts. First technique to try when optimizing Claude interactions.

- **Path**: `./docs/build-with-claude/prompt-engineering/multishot-prompting.md`
- **Summary**: Use examples to improve Claude's performance. Demonstrates few-shot learning patterns and example selection strategies.

- **Path**: `./docs/build-with-claude/prompt-engineering/chain-of-thought.md`
- **Summary**: Enable Claude's reasoning through step-by-step thinking. Improves complex problem-solving and transparent reasoning.

### Advanced Techniques
- **Path**: `./docs/build-with-claude/prompt-engineering/use-xml-tags.md`
- **Summary**: Structure prompts with XML tags for better parsing and organization. Improves Claude's understanding of complex instructions.

- **Path**: `./docs/build-with-claude/prompt-engineering/system-prompts.md`
- **Summary**: Give Claude specific roles and personas through system prompts. Controls behavior and response style effectively.

- **Path**: `./docs/build-with-claude/prompt-engineering/prefill-claudes-response.md`
- **Summary**: Guide Claude's response format by prefilling the beginning. Ensures consistent output formatting and structure.

- **Path**: `./docs/build-with-claude/prompt-engineering/chain-prompts.md`
- **Summary**: Break complex tasks into sequential prompts. Handles multi-step workflows and complex reasoning chains.

### Specialized Prompting
- **Path**: `./docs/build-with-claude/prompt-engineering/long-context-tips.md`
- **Summary**: Optimize prompts for extended context windows. Strategies for processing large documents and maintaining coherence.

- **Path**: `./docs/build-with-claude/prompt-engineering/extended-thinking-tips.md`
- **Summary**: Best practices for models with extended thinking capabilities. Optimize reasoning and transparency in complex tasks.

- **Path**: `./docs/build-with-claude/prompt-engineering/claude-4-best-practices.md`
- **Summary**: Specific optimization techniques for Claude 4 models. Leverage unique capabilities effectively.

- **Path**: `./docs/build-with-claude/prompt-engineering/prompt-templates-and-variables.md`
- **Summary**: Create reusable prompt templates with dynamic variables for scalable applications.

### Prompt Development Tools
- **Path**: `./docs/build-with-claude/prompt-engineering/prompt-generator.md`
- **Summary**: AI-assisted prompt generation tool for creating effective prompts from requirements.

- **Path**: `./docs/build-with-claude/prompt-engineering/prompt-improver.md`
- **Summary**: Automated prompt improvement tool that optimizes existing prompts for better results.

---

## Claude Code Terminal Tool

### Getting Started
- **Path**: `./docs/claude-code/overview.md`
- **Summary**: Anthropic's agentic coding tool for terminal environments. Transforms natural language descriptions into working code with direct file editing and command execution.

- **Path**: `./docs/claude-code/quickstart.md`
- **Summary**: 5-minute quickstart guide with practical examples. Get Claude Code running and explore common workflows quickly.

### Core Workflows
- **Path**: `./docs/claude-code/common-workflows.md`
- **Summary**: Step-by-step guides for frequent development tasks. Covers feature building, debugging, codebase navigation, and automation patterns.

### Configuration & Setup
- **Path**: `./docs/claude-code/setup.md`
- **Summary**: Advanced installation and configuration options. Covers custom environments, enterprise setups, and integration with existing toolchains.

- **Path**: `./docs/claude-code/settings.md`
- **Summary**: Customize Claude Code for your workflow. Configuration options, preferences, and environment-specific settings.

- **Path**: `./docs/claude-code/cli-reference.md`
- **Summary**: Complete command-line interface reference. All available commands, flags, and usage patterns for Claude Code.

### Integrations & Extensions
- **Path**: `./docs/claude-code/ide-integrations.md`
- **Summary**: Integrate Claude Code with popular IDEs. Setup guides for VS Code, JetBrains IDEs, and other development environments.

- **Path**: `./docs/claude-code/third-party-integrations.md`
- **Summary**: Configure Claude Code with AWS Bedrock and Google Vertex AI. Enterprise cloud platform integrations and deployment options.

- **Path**: `./docs/claude-code/mcp.md`
- **Summary**: Extend Claude Code with Model Context Protocol. Connect to external data sources like Google Drive, Figma, and Slack.

### Advanced Features
- **Path**: `./docs/claude-code/interactive-mode.md`
- **Summary**: Interactive mode for real-time coding sessions with Claude Code.

- **Path**: `./docs/claude-code/slash-commands.md`
- **Summary**: Complete list of slash commands for advanced Claude Code operations.

- **Path**: `./docs/claude-code/sub-agents.md`
- **Summary**: Using sub-agents for specialized tasks and distributed workloads.

- **Path**: `./docs/claude-code/hooks.md`
- **Summary**: Custom hooks for extending Claude Code functionality.

- **Path**: `./docs/claude-code/hooks-guide.md`
- **Summary**: Comprehensive guide to writing and deploying custom hooks.

- **Path**: `./docs/claude-code/memory.md`
- **Summary**: Memory management and context retention in Claude Code sessions.

- **Path**: `./docs/claude-code/output-styles.md`
- **Summary**: Customize output formatting and display options.

- **Path**: `./docs/claude-code/statusline.md`
- **Summary**: Configure and customize the Claude Code status line display.

### Configuration & Deployment
- **Path**: `./docs/claude-code/model-config.md`
- **Summary**: Configure model selection and parameters for Claude Code.

- **Path**: `./docs/claude-code/terminal-config.md`
- **Summary**: Terminal-specific configuration options and optimizations.

- **Path**: `./docs/claude-code/network-config.md`
- **Summary**: Network configuration for proxy, firewall, and enterprise environments.

- **Path**: `./docs/claude-code/devcontainer.md`
- **Summary**: Using Claude Code in development containers and Docker environments.

- **Path**: `./docs/claude-code/llm-gateway.md`
- **Summary**: Configure Claude Code to work with LLM gateways and proxies.

### Cloud Platform Integrations
- **Path**: `./docs/claude-code/amazon-bedrock.md`
- **Summary**: Deploy Claude Code with Amazon Bedrock integration.

- **Path**: `./docs/claude-code/google-vertex-ai.md`
- **Summary**: Configure Claude Code for Google Vertex AI deployment.

### CI/CD Integration
- **Path**: `./docs/claude-code/github-actions.md`
- **Summary**: Integrate Claude Code into GitHub Actions workflows.

- **Path**: `./docs/claude-code/gitlab-ci-cd.md`
- **Summary**: Using Claude Code in GitLab CI/CD pipelines.

### Monitoring & Analytics
- **Path**: `./docs/claude-code/analytics.md`
- **Summary**: Track Claude Code usage patterns and productivity metrics.

- **Path**: `./docs/claude-code/monitoring-usage.md`
- **Summary**: Monitor resource consumption and optimize performance.

- **Path**: `./docs/claude-code/costs.md`
- **Summary**: Understanding and managing Claude Code usage costs.

### Security & Compliance
- **Path**: `./docs/claude-code/iam.md`
- **Summary**: Identity and access management for Claude Code deployments.

- **Path**: `./docs/claude-code/legal-and-compliance.md`
- **Summary**: Legal considerations and compliance requirements for Claude Code usage.

### Claude Code SDK
- **Path**: `./docs/claude-code/sdk/sdk-overview.md`
- **Summary**: Overview of the Claude Code SDK for custom integrations.

- **Path**: `./docs/claude-code/sdk/sdk-typescript.md`
- **Summary**: TypeScript SDK documentation for Claude Code integration.

- **Path**: `./docs/claude-code/sdk/sdk-python.md`
- **Summary**: Python SDK for building Claude Code extensions.

- **Path**: `./docs/claude-code/sdk/sdk-headless.md`
- **Summary**: Running Claude Code in headless mode for automation.

- **Path**: `./docs/claude-code/sdk/sdk-sessions.md`
- **Summary**: Managing Claude Code sessions programmatically.

- **Path**: `./docs/claude-code/sdk/custom-tools.md`
- **Summary**: Building custom tools and extensions for Claude Code.

- **Path**: `./docs/claude-code/sdk/modifying-system-prompts.md`
- **Summary**: Customize system prompts for specialized behaviors.

- **Path**: `./docs/claude-code/sdk/sdk-permissions.md`
- **Summary**: Permission management in SDK-based integrations.

- **Path**: `./docs/claude-code/sdk/sdk-mcp.md`
- **Summary**: MCP integration through the Claude Code SDK.

- **Path**: `./docs/claude-code/sdk/sdk-slash-commands.md`
- **Summary**: Implementing custom slash commands via SDK.

- **Path**: `./docs/claude-code/sdk/sdk-cost-tracking.md`
- **Summary**: Track and optimize costs in SDK applications.

- **Path**: `./docs/claude-code/sdk/streaming-vs-single-mode.md`
- **Summary**: Choose between streaming and single response modes.

- **Path**: `./docs/claude-code/sdk/subagents.md`
- **Summary**: Creating and managing subagents through the SDK.

- **Path**: `./docs/claude-code/sdk/todo-tracking.md`
- **Summary**: Implement todo tracking in custom Claude Code integrations.

### Operations & Support
- **Path**: `./docs/claude-code/troubleshooting.md`
- **Summary**: Solutions for common Claude Code issues. Debugging guide, error resolution, and performance optimization tips.

- **Path**: `./docs/claude-code/security.md`
- **Summary**: Security safeguards and best practices. Understanding Claude Code's security model and safe usage patterns.

- **Path**: `./docs/claude-code/data-usage.md`
- **Summary**: Data handling and privacy policies. How Claude Code processes and protects your code and development data.

---

## Model Information

### Model Overview
- **Path**: `./docs/about-claude/models/overview.md`
- **Summary**: Comprehensive guide to Claude model family including Claude 4, Sonnet 4, and comparison tables. Details capabilities, pricing, and model selection guidance.
- **Key Info**: Model names, context windows, training data cutoffs, performance characteristics

### Model Selection & Migration
- **Path**: `./docs/about-claude/models/choosing-a-model.md`
- **Summary**: Decision framework for selecting the right Claude model for your use case. Balances capability, cost, and performance requirements.

- **Path**: `./docs/about-claude/models/migrating-to-claude-4.md`
- **Summary**: Migration guide from Claude 3 to Claude 4 models. Covers API changes, performance improvements, and compatibility considerations.

### Pricing & Operations
- **Path**: `./docs/about-claude/pricing.md`
- **Summary**: Detailed pricing information across all Claude models. Includes token costs, cache pricing, and usage optimization strategies.

- **Path**: `./docs/about-claude/model-deprecations.md`
- **Summary**: Model lifecycle and deprecation timeline. Plan for model transitions and understand support windows.

### Technical Reference
- **Path**: `./docs/about-claude/glossary.md`
- **Summary**: Comprehensive glossary of terms and concepts in the Claude ecosystem. Essential reference for understanding technical documentation.

---

## Administration & Management

### Organization Management
- **Path**: `./api/admin-api/organization/get-me.md`
- **Summary**: Retrieve organization information and settings. Essential for programmatic organization management and introspection.

### User Management
- **Path**: `./api/admin-api/users/list-users.md`
- **Summary**: List and manage organization users. Programmatic access to user management for large teams.
- **Related**: `./api/admin-api/users/get-user.md`, `./api/admin-api/users/update-user.md`, `./api/admin-api/users/remove-user.md`

### Invitations Management
- **Path**: `./api/admin-api/invites/list-invites.md`
- **Summary**: List pending invitations to your organization.

- **Path**: `./api/admin-api/invites/create-invite.md`
- **Summary**: Send invitations to new users to join your organization.

- **Path**: `./api/admin-api/invites/get-invite.md`
- **Summary**: Retrieve details about a specific invitation.

- **Path**: `./api/admin-api/invites/delete-invite.md`
- **Summary**: Cancel pending invitations before they are accepted.

### API Key Management
- **Path**: `./api/admin-api/apikeys/list-api-keys.md`
- **Summary**: Programmatically manage API keys for organization security. List, create, update, and monitor API key usage.
- **Related**: `./api/admin-api/apikeys/get-api-key.md`, `./api/admin-api/apikeys/update-api-key.md`

### Workspace Management
- **Path**: `./api/admin-api/workspaces/list-workspaces.md`
- **Summary**: Manage workspaces for team organization and access control. Create isolated environments for different projects.
- **Related**: `./api/admin-api/workspaces/create-workspace.md`, `./api/admin-api/workspaces/get-workspace.md`, `./api/admin-api/workspaces/update-workspace.md`

- **Path**: `./api/admin-api/workspaces/archive-workspace.md`
- **Summary**: Archive workspaces that are no longer active while preserving data.

### Workspace Members Management
- **Path**: `./api/admin-api/workspace_members/list-workspace-members.md`
- **Summary**: List all members of a specific workspace.

- **Path**: `./api/admin-api/workspace_members/create-workspace-member.md`
- **Summary**: Add users to workspaces with specific roles and permissions.

- **Path**: `./api/admin-api/workspace_members/get-workspace-member.md`
- **Summary**: Retrieve details about a specific workspace member.

- **Path**: `./api/admin-api/workspace_members/update-workspace-member.md`
- **Summary**: Update roles and permissions for workspace members.

- **Path**: `./api/admin-api/workspace_members/delete-workspace-member.md`
- **Summary**: Remove users from specific workspaces.

### Usage & Analytics
- **Path**: `./api/admin-api/usage-cost/get-cost-report.md`
- **Summary**: Monitor organization spending and usage patterns. Essential for budget management and cost optimization.
- **Related**: `./api/admin-api/usage-cost/get-messages-usage-report.md`, `./api/admin-api/claude-code/get-claude-code-usage-report.md`

---

## Resources & Learning Materials

### Interactive Learning
- **Path**: `./resources/overview.md`
- **Summary**: Hub for learning resources including quickstarts, courses, cookbook, and prompt library. Central navigation for educational content.

### Prompt Library
- **Path**: `./resources/prompt-library/library.md`
- **Summary**: Curated collection of optimized prompts for business and personal tasks. Over 60 ready-to-use prompt templates with examples.
- **Examples**: Includes prompts for coding, writing, analysis, creativity, and productivity tasks

### Complete Prompt Library

#### Business & Productivity
- `./resources/prompt-library/meeting-scribe.md` - Transcribe and summarize meetings
- `./resources/prompt-library/memo-maestro.md` - Create professional memos
- `./resources/prompt-library/efficiency-estimator.md` - Estimate task completion times
- `./resources/prompt-library/email-extractor.md` - Extract key information from emails
- `./resources/prompt-library/corporate-clairvoyant.md` - Predict business trends
- `./resources/prompt-library/brand-builder.md` - Develop brand strategies
- `./resources/prompt-library/product-naming-pro.md` - Generate product names
- `./resources/prompt-library/interview-question-crafter.md` - Create interview questions
- `./resources/prompt-library/career-coach.md` - Career guidance and planning
- `./resources/prompt-library/master-moderator.md` - Moderate discussions and meetings

#### Coding & Development
- `./resources/prompt-library/code-consultant.md` - Code review and optimization
- `./resources/prompt-library/python-bug-buster.md` - Debug Python code
- `./resources/prompt-library/git-gud.md` - Git workflow assistance
- `./resources/prompt-library/code-clarifier.md` - Explain complex code
- `./resources/prompt-library/function-fabricator.md` - Generate functions from descriptions
- `./resources/prompt-library/sql-sorcerer.md` - SQL query optimization
- `./resources/prompt-library/excel-formula-expert.md` - Excel formula creation
- `./resources/prompt-library/google-apps-scripter.md` - Google Apps Script development
- `./resources/prompt-library/latex-legend.md` - LaTeX document formatting
- `./resources/prompt-library/website-wizard.md` - Web development assistance

#### Creative Writing & Language
- `./resources/prompt-library/storytelling-sidekick.md` - Story development helper
- `./resources/prompt-library/alliteration-alchemist.md` - Create alliterative phrases
- `./resources/prompt-library/cosmic-keystrokes.md` - Sci-fi writing assistant
- `./resources/prompt-library/prose-polisher.md` - Refine and improve writing
- `./resources/prompt-library/adaptive-editor.md` - Adaptive writing style editor
- `./resources/prompt-library/pun-dit.md` - Generate puns and wordplay
- `./resources/prompt-library/simile-savant.md` - Create vivid similes
- `./resources/prompt-library/portmanteau-poet.md` - Blend words creatively
- `./resources/prompt-library/neologism-creator.md` - Invent new words
- `./resources/prompt-library/tongue-twister.md` - Create tongue twisters
- `./resources/prompt-library/babels-broadcasts.md` - Multilingual content creation
- `./resources/prompt-library/polyglot-superpowers.md` - Translation and language learning
- `./resources/prompt-library/idiom-illuminator.md` - Explain idioms and phrases
- `./resources/prompt-library/emoji-encoder.md` - Convert text to emoji
- `./resources/prompt-library/grammar-genie.md` - Grammar correction and explanation
- `./resources/prompt-library/second-grade-simplifier.md` - Simplify complex text
- `./resources/prompt-library/cite-your-sources.md` - Add citations to content

#### Data & Analysis
- `./resources/prompt-library/data-organizer.md` - Structure unorganized data
- `./resources/prompt-library/csv-converter.md` - Convert data formats
- `./resources/prompt-library/spreadsheet-sorcerer.md` - Advanced spreadsheet operations
- `./resources/prompt-library/direction-decoder.md` - Parse and clarify directions
- `./resources/prompt-library/airport-code-analyst.md` - Airport code information
- `./resources/prompt-library/review-classifier.md` - Classify and analyze reviews
- `./resources/prompt-library/tweet-tone-detector.md` - Analyze social media sentiment
- `./resources/prompt-library/pii-purifier.md` - Remove personal information

#### Education & Learning
- `./resources/prompt-library/lesson-planner.md` - Create lesson plans
- `./resources/prompt-library/grading-guru.md` - Grading assistance and rubrics
- `./resources/prompt-library/socratic-sage.md` - Socratic teaching method
- `./resources/prompt-library/trivia-generator.md` - Generate trivia questions

#### Creative & Entertainment
- `./resources/prompt-library/alien-anthropologist.md` - Alien perspective storytelling
- `./resources/prompt-library/dream-interpreter.md` - Interpret dreams creatively
- `./resources/prompt-library/riddle-me-this.md` - Create and solve riddles
- `./resources/prompt-library/sci-fi-scenario-simulator.md` - Simulate sci-fi scenarios
- `./resources/prompt-library/time-travel-consultant.md` - Time travel narratives
- `./resources/prompt-library/futuristic-fashion-advisor.md` - Future fashion trends
- `./resources/prompt-library/vr-fitness-innovator.md` - VR fitness concepts
- `./resources/prompt-library/mood-colorizer.md` - Associate moods with colors
- `./resources/prompt-library/culinary-creator.md` - Recipe creation and cooking tips
- `./resources/prompt-library/hal-the-humorous-helper.md` - Humorous assistance

#### Philosophy & Wellness
- `./resources/prompt-library/philosophical-musings.md` - Explore philosophical concepts
- `./resources/prompt-library/perspectives-ponderer.md` - Consider multiple viewpoints
- `./resources/prompt-library/ethical-dilemma-navigator.md` - Navigate ethical questions
- `./resources/prompt-library/mindfulness-mentor.md` - Mindfulness and meditation guidance
- `./resources/prompt-library/motivational-muse.md` - Motivational content creation

### Platform Documentation
- **Path**: `./docs/intro.md`
- **Summary**: Introduction to Claude platform and capabilities overview.

- **Path**: `./docs/overview.md`
- **Summary**: High-level overview of the Claude Developer Platform architecture.

- **Path**: `./docs/mcp.md`
- **Summary**: Model Context Protocol (MCP) documentation and integration guide.

### Use Case Guides
- **Path**: `./docs/about-claude/use-case-guides/overview.md`
- **Summary**: Industry-specific implementation guides with real-world examples. Practical patterns for common business applications.

- **Path**: `./docs/about-claude/use-case-guides/customer-support-chat.md`
- **Summary**: Building effective customer support chatbots with Claude.

- **Path**: `./docs/about-claude/use-case-guides/content-moderation.md`
- **Summary**: Content moderation strategies and implementation patterns.

- **Path**: `./docs/about-claude/use-case-guides/legal-summarization.md`
- **Summary**: Legal document analysis and summarization with Claude.

- **Path**: `./docs/about-claude/use-case-guides/ticket-routing.md`
- **Summary**: Automated ticket classification and routing systems.

---

## Testing & Evaluation

### Test Framework
- **Path**: `./docs/test-and-evaluate/define-success.md`
- **Summary**: Define success criteria and metrics for AI applications.

- **Path**: `./docs/test-and-evaluate/develop-tests.md`
- **Summary**: Develop comprehensive test suites for Claude integrations.

- **Path**: `./docs/test-and-evaluate/eval-tool.md`
- **Summary**: Evaluation tools and frameworks for measuring performance.

### Strengthen Guardrails
- **Path**: `./docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md`
- **Summary**: Techniques to minimize hallucinations and improve factual accuracy.

- **Path**: `./docs/test-and-evaluate/strengthen-guardrails/increase-consistency.md`
- **Summary**: Methods for achieving consistent responses across similar queries.

- **Path**: `./docs/test-and-evaluate/strengthen-guardrails/keep-claude-in-character.md`
- **Summary**: Maintain consistent personality and behavior in Claude responses.

- **Path**: `./docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks.md`
- **Summary**: Prevent prompt injection and jailbreak attempts.

- **Path**: `./docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak.md`
- **Summary**: Protect system prompts from being revealed in responses.

- **Path**: `./docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md`
- **Summary**: Gracefully handle refusals in streaming responses.

- **Path**: `./docs/test-and-evaluate/strengthen-guardrails/reduce-latency.md`
- **Summary**: Optimize response times and reduce latency in production.

---

## Release Notes & Updates

### Overview
- **Path**: `./release-notes/overview.md`
- **Summary**: Central hub for all Anthropic product updates. Tracks changes across API, Claude apps, and system prompts.

### API Updates
- **Path**: `./release-notes/api.md`
- **Summary**: Latest API enhancements, new features, and bug fixes. Essential for staying current with Claude Developer Platform changes.

### Application Updates
- **Path**: `./release-notes/claude-apps.md`
- **Summary**: Updates to Claude's web and mobile applications. New features, performance improvements, and user experience enhancements.

### System Prompts
- **Path**: `./release-notes/system-prompts.md`
- **Summary**: Changes to default system prompts in Claude applications. Important for understanding model behavior evolution.

### Claude Code Updates
- **Path**: `./release-notes/claude-code.md`
- **Summary**: Release notes and updates specific to Claude Code terminal tool.

---

## Key Topics Index

### Authentication & Security
- API Keys: `./api/overview.md`, `./api/admin-api/apikeys/`
- Error Handling: `./api/errors.md`
- Rate Limits: `./api/rate-limits.md`
- Security Best Practices: `./docs/claude-code/security.md`

### Cost Optimization
- Prompt Caching: `./docs/build-with-claude/prompt-caching.md`
- Batch Processing: `./docs/build-with-claude/batch-processing.md`
- Token Efficiency: `./docs/agents-and-tools/tool-use/token-efficient-tool-use.md`
- Usage Monitoring: `./api/usage-cost-api.md`

### Development Workflows
- Tool Use: `./docs/agents-and-tools/tool-use/overview.md`
- Claude Code: `./docs/claude-code/overview.md`
- Streaming: `./docs/build-with-claude/streaming.md`
- File Handling: `./docs/build-with-claude/files.md`

### Large-Scale Processing
- Context Windows: `./docs/build-with-claude/context-windows.md`
- Batch API: `./docs/build-with-claude/batch-processing.md`
- Long Context Tips: `./docs/build-with-claude/prompt-engineering/long-context-tips.md`

### Model Capabilities
- Extended Thinking: `./docs/build-with-claude/extended-thinking.md`
- Citations: `./docs/build-with-claude/citations.md`
- Multimodal: Vision capabilities across messages API
- Tool Integration: Complete tool ecosystem documentation

### Performance & Scaling
- Service Tiers: `./api/service-tiers.md`
- Rate Limits: `./api/rate-limits.md`
- Regional Deployment: `./api/supported-regions.md`
- Cloud Integration: Bedrock and Vertex AI guides

---

## Cross-References by Use Case

### Building AI Assistants
- Start: `./docs/get-started.md`
- Tool Use: `./docs/agents-and-tools/tool-use/overview.md`
- Prompt Engineering: `./docs/build-with-claude/prompt-engineering/overview.md`
- Examples: `./resources/prompt-library/`

### Enterprise Deployment
- Admin APIs: `./api/administration-api.md`
- Cloud Platforms: `./api/claude-on-amazon-bedrock.md`, `./api/claude-on-vertex-ai.md`
- Security: `./docs/claude-code/security.md`
- Usage Analytics: `./api/usage-cost-api.md`

### Development Automation
- Claude Code: `./docs/claude-code/overview.md`
- Development Tools: `./docs/agents-and-tools/tool-use/bash-tool.md`, `./docs/agents-and-tools/tool-use/text-editor-tool.md`
- Code Examples: `./resources/prompt-library/code-consultant.md`

### Content & Document Processing
- Files API: `./docs/build-with-claude/files.md`
- PDF Support: `./docs/build-with-claude/pdf-support.md`
- Citations: `./docs/build-with-claude/citations.md`
- Long Context: `./docs/build-with-claude/context-windows.md`

This index serves as a comprehensive navigation tool for the entire Anthropic documentation ecosystem. Each entry provides context about the content's purpose and its relationship to other documentation, enabling quick location of relevant information for any development need.