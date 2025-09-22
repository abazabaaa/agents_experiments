# Anthropic Claude Documentation Index

## Overview

This index provides comprehensive navigation for Anthropic's Claude documentation, organized by learning paths and functional areas. The documentation covers Claude's AI models, APIs, tools, and development frameworks to help developers build intelligent applications effectively.

---

## Getting Started

### Quick Start Guide
- **Path**: `../anthropic/docs/get-started.md`
- **Summary**: Complete getting started guide with API setup, first API call examples in multiple languages (Python, TypeScript, Java, cURL). Demonstrates building a simple web search assistant with practical code examples and next steps for exploration.

### Introduction to Claude
- **Path**: `../anthropic/docs/intro.md`
- **Summary**: High-level overview of Claude's capabilities including the latest Claude Opus 4.1 and Claude Sonnet 4 models. Provides entry points for development, prompt library access, and key capabilities demonstration with support resources.

### Building with Claude Overview
- **Path**: `../anthropic/docs/overview.md`
- **Summary**: Comprehensive guide to Claude's enterprise capabilities, implementation workflow, and development lifecycle. Covers security, reliability, and global deployment considerations with detailed feature comparisons and use case examples.

---

## About Claude

### Model Information

#### Model Overview
- **Path**: `../anthropic/docs/about-claude/models/overview.md`
- **Summary**: Complete reference for Claude model family including Claude Opus 4.1, Opus 4, Sonnet 4, and Haiku models. Provides model comparison tables, pricing, capabilities, context windows, and migration guidance between model versions.

#### Choosing the Right Model
- **Path**: `../anthropic/docs/about-claude/models/choosing-a-model.md`
- **Summary**: Strategic guide for model selection based on capabilities, speed, and cost requirements. Includes decision matrix for different use cases and practical guidance for starting with cost-effective vs. capable models.

#### Migrating to Claude 4
- **Path**: `../anthropic/docs/about-claude/models/migrating-to-claude-4.md`
- **Summary**: Step-by-step migration guide from Claude 3.7 to Claude 4 models with API compatibility information and best practices for smooth transitions.

### Pricing and Usage

#### Pricing Guide
- **Path**: `../anthropic/docs/about-claude/pricing.md`
- **Summary**: Comprehensive pricing documentation covering all models, batch processing discounts, prompt caching, tool use costs, and enterprise options. Includes cost calculation examples and optimization strategies for different usage patterns.

#### Model Deprecations
- **Path**: `../anthropic/docs/about-claude/model-deprecations.md`
- **Summary**: Information about deprecated Claude models and migration timelines for maintaining application compatibility.

### Use Cases and Applications

#### Use Case Overview
- **Path**: `../anthropic/docs/about-claude/use-case-guides/overview.md`
- **Summary**: Introduction to production-ready use case guides including ticket routing, customer support, content moderation, and legal document processing with practical implementation examples.

#### Customer Support Chat
- **Path**: `../anthropic/docs/about-claude/use-case-guides/customer-support-chat.md`
- **Summary**: Detailed guide for building intelligent customer support chatbots with context awareness, conversation flow management, and cost optimization strategies.

#### Content Moderation
- **Path**: `../anthropic/docs/about-claude/use-case-guides/content-moderation.md`
- **Summary**: Best practices for implementing content filtering and moderation systems using Claude's safety capabilities and policy enforcement features.

#### Legal Summarization
- **Path**: `../anthropic/docs/about-claude/use-case-guides/legal-summarization.md`
- **Summary**: Specialized guide for legal document processing, key information extraction, and compliance-focused summarization with accuracy and reliability considerations.

#### Ticket Routing
- **Path**: `../anthropic/docs/about-claude/use-case-guides/ticket-routing.md`
- **Summary**: Implementation guide for automated customer support ticket classification and routing at scale with accuracy metrics and workflow optimization.

### Reference Materials

#### Glossary
- **Path**: `../anthropic/docs/about-claude/glossary.md`
- **Summary**: Comprehensive glossary of Claude-specific terms, concepts, and technical terminology for developers and users.

---

## Build with Claude

### Core Features Overview
- **Path**: `../anthropic/docs/build-with-claude/overview.md`
- **Summary**: Complete feature matrix covering core capabilities (context windows, batch processing, citations), tools (bash, code execution, computer use), and availability across platforms with detailed comparison tables.

### Input and Output Handling

#### Vision Capabilities
- **Path**: `../anthropic/docs/build-with-claude/vision.md`
- **Summary**: Comprehensive guide to Claude's multimodal vision capabilities including image processing, cost calculation, quality optimization, and practical examples. Covers base64, URL, and Files API approaches with limitations and best practices.

#### PDF Support
- **Path**: `../anthropic/docs/build-with-claude/pdf-support.md`
- **Summary**: Guide for processing PDF documents including text extraction, visual content analysis, and handling complex document structures with Claude's vision capabilities.

#### Files API
- **Path**: `../anthropic/docs/build-with-claude/files.md`
- **Summary**: Documentation for uploading and managing files with Claude including PDFs, images, and text files for reuse across multiple requests without re-uploading.

#### Multilingual Support
- **Path**: `../anthropic/docs/build-with-claude/multilingual-support.md`
- **Summary**: Guide to Claude's multilingual capabilities including language-specific optimizations, translation best practices, and cross-cultural communication patterns.

### Advanced Reasoning

#### Extended Thinking
- **Path**: `../anthropic/docs/build-with-claude/extended-thinking.md`
- **Summary**: Documentation for Claude's enhanced reasoning capabilities providing transparency into step-by-step thought processes for complex problem solving and decision making.

#### Citations
- **Path**: `../anthropic/docs/build-with-claude/citations.md`
- **Summary**: Guide to implementing source attribution and reference tracking in Claude responses for verifiable, trustworthy outputs with detailed citation formatting.

#### Search Results Integration
- **Path**: `../anthropic/docs/build-with-claude/search-results.md`
- **Summary**: Implementation guide for natural citations in RAG applications with proper source attribution for custom knowledge bases and web search-quality citations.

### Performance and Optimization

#### Context Windows
- **Path**: `../anthropic/docs/build-with-claude/context-windows.md`
- **Summary**: Guide to managing Claude's context windows including the 1M token beta feature, optimization strategies for large documents, and best practices for maintaining conversation context.

#### Prompt Caching
- **Path**: `../anthropic/docs/build-with-claude/prompt-caching.md`
- **Summary**: Cost and latency optimization through prompt caching with 5-minute and 1-hour cache options. Includes implementation strategies and cache invalidation best practices.

#### Batch Processing
- **Path**: `../anthropic/docs/build-with-claude/batch-processing.md`
- **Summary**: Asynchronous processing guide for large volumes of requests with 50% cost savings. Covers batch API usage, monitoring, and optimization for high-throughput applications.

#### Streaming
- **Path**: `../anthropic/docs/build-with-claude/streaming.md`
- **Summary**: Real-time response streaming implementation for improved user experience with lower perceived latency and progressive response delivery.

#### Token Counting
- **Path**: `../anthropic/docs/build-with-claude/token-counting.md`
- **Summary**: Guide to understanding and calculating token usage for cost estimation and optimization before sending requests to Claude.

### Technical Integration

#### Embeddings
- **Path**: `../anthropic/docs/build-with-claude/embeddings.md`
- **Summary**: Guide to using Claude with embedding models for semantic search, document similarity, and vector database integration patterns.

---

## Prompt Engineering

### Core Techniques

#### Prompt Engineering Overview
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/overview.md`
- **Summary**: Comprehensive introduction to prompt engineering methodology including when to use prompting vs. fine-tuning, technique ordering from broad to specialized, and links to interactive tutorials.

#### Be Clear and Direct
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/be-clear-and-direct.md`
- **Summary**: Fundamental technique for clear communication with Claude including specific instruction formatting, detail levels, and avoiding ambiguous language for optimal results.

#### Multishot Prompting
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/multishot-prompting.md`
- **Summary**: Using examples to guide Claude's behavior including few-shot learning, example selection strategies, and balancing specificity with generalization.

#### Chain of Thought
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/chain-of-thought.md`
- **Summary**: Technique for encouraging step-by-step reasoning in complex problem solving with explicit thinking processes and intermediate step validation.

### Advanced Techniques

#### System Prompts
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/system-prompts.md`
- **Summary**: Guide to crafting effective system prompts for role definition, behavior control, and context setting with best practices for personality and expertise assignment.

#### Use XML Tags
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/use-xml-tags.md`
- **Summary**: Structured prompting technique using XML tags for clear input organization, output formatting, and complex instruction hierarchies.

#### Prefill Claude's Response
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/prefill-claudes-response.md`
- **Summary**: Advanced technique for controlling response format and style by providing the beginning of Claude's response to guide output structure and tone.

#### Chain Prompts
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/chain-prompts.md`
- **Summary**: Breaking complex tasks into sequential steps with intermediate validation and error handling for improved reliability and debugging.

### Specialized Guidance

#### Claude 4 Best Practices
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/claude-4-best-practices.md`
- **Summary**: Model-specific optimization techniques for Claude 4 including new capabilities, performance characteristics, and prompt adaptation strategies.

#### Extended Thinking Tips
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/extended-thinking-tips.md`
- **Summary**: Specialized prompting techniques for extended thinking models to maximize reasoning transparency and problem-solving effectiveness.

#### Long Context Tips
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/long-context-tips.md`
- **Summary**: Optimization strategies for working with large context windows including document organization, attention management, and performance considerations.

### Tools and Templates

#### Prompt Generator
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/prompt-generator.md`
- **Summary**: Guide to using Anthropic's prompt generation tools for creating effective prompts with structured templates and iterative improvement processes.

#### Prompt Improver
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/prompt-improver.md`
- **Summary**: Systematic approach to analyzing and improving existing prompts using feedback loops and performance metrics.

#### Prompt Templates and Variables
- **Path**: `../anthropic/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables.md`
- **Summary**: Creating reusable prompt templates with variable substitution for scalable and maintainable prompt engineering workflows.

---

## Agents and Tools

### Core Tool Use

#### Tool Use Overview
- **Path**: `../anthropic/docs/agents-and-tools/tool-use/overview.md`
- **Summary**: Comprehensive introduction to Claude's tool capabilities including client vs. server tools, implementation workflows, and extensive code examples for weather, time, and location tools with pricing information.

#### Implementing Tool Use
- **Path**: `../anthropic/docs/agents-and-tools/tool-use/implement-tool-use.md`
- **Summary**: Detailed implementation guide covering tool definition best practices, error handling, parallel tool use, and troubleshooting with complete code examples and testing scripts.

#### Token Efficient Tool Use
- **Path**: `../anthropic/docs/agents-and-tools/tool-use/token-efficient-tool-use.md`
- **Summary**: Optimization techniques for reducing tool use costs and latency through efficient tool descriptions and parameter handling.

### Specific Tools

#### Computer Use Tool
- **Path**: `../anthropic/docs/agents-and-tools/tool-use/computer-use-tool.md`
- **Summary**: Beta feature for controlling computer interfaces through screenshots and mouse/keyboard commands. Includes setup, safety considerations, and practical automation examples.

#### Code Execution Tool
- **Path**: `../anthropic/docs/agents-and-tools/tool-use/code-execution-tool.md`
- **Summary**: Python code execution in sandboxed environments for data analysis, visualization, and computational tasks with file handling and session management.

#### Bash Tool
- **Path**: `../anthropic/docs/agents-and-tools/tool-use/bash-tool.md`
- **Summary**: System shell interaction for command-line operations, script execution, and system administration tasks with security considerations and best practices.

#### Text Editor Tool
- **Path**: `../anthropic/docs/agents-and-tools/tool-use/text-editor-tool.md`
- **Summary**: File creation and editing capabilities with built-in text editor interface for automated file manipulation and content generation tasks.

#### Web Tools
- **Path**: `../anthropic/docs/agents-and-tools/tool-use/web-search-tool.md`
- **Summary**: Real-time web search capabilities for current information retrieval with search optimization and result processing strategies.

- **Path**: `../anthropic/docs/agents-and-tools/tool-use/web-fetch-tool.md`
- **Summary**: Direct web page and PDF content retrieval for in-depth analysis with content parsing and token management considerations.

### Advanced Tool Features

#### Fine-Grained Tool Streaming
- **Path**: `../anthropic/docs/agents-and-tools/tool-use/fine-grained-tool-streaming.md`
- **Summary**: Low-latency tool parameter streaming without buffering for responsive tool interactions and large parameter handling.

### Integration Platforms

#### Model Context Protocol
- **Path**: `../anthropic/docs/mcp.md`
- **Summary**: Overview of MCP as a standardized protocol for connecting AI models to external data sources and tools with implementation examples across Anthropic products.

#### MCP Connector
- **Path**: `../anthropic/docs/agents-and-tools/mcp-connector.md`
- **Summary**: Direct MCP server integration through the Messages API including authentication, multiple server support, and practical implementation examples.

#### Remote MCP Servers
- **Path**: `../anthropic/docs/agents-and-tools/remote-mcp-servers.md`
- **Summary**: Guide to connecting and managing remote MCP servers for extended functionality and external system integration.

#### Claude for Sheets
- **Path**: `../anthropic/docs/agents-and-tools/claude-for-sheets.md`
- **Summary**: Google Sheets integration for prompt engineering at scale, survey analysis, and spreadsheet-based AI workflows with function examples and troubleshooting.

---

## Claude Code

### Getting Started

#### Claude Code Overview
- **Path**: `../anthropic/docs/claude-code/overview.md`
- **Summary**: Introduction to Anthropic's terminal-based agentic coding tool including key features, installation, and core value propositions for developer productivity and workflow integration.

#### Quickstart Guide
- **Path**: `../anthropic/docs/claude-code/quickstart.md`
- **Summary**: Complete setup guide from installation to first coding session including authentication, basic commands, Git integration, and practical examples for common development tasks.

### Setup and Configuration

#### Setup Guide
- **Path**: `../anthropic/docs/claude-code/setup.md`
- **Summary**: Advanced installation options and configuration for different environments including enterprise setups, custom configurations, and troubleshooting installation issues.

#### Settings and Configuration
- **Path**: `../anthropic/docs/claude-code/settings.md`
- **Summary**: Comprehensive configuration options for personalizing Claude Code including model preferences, behavior settings, and workflow customizations.

#### CLI Reference
- **Path**: `../anthropic/docs/claude-code/cli-reference.md`
- **Summary**: Complete command reference for Claude Code including all CLI options, slash commands, shortcuts, and advanced usage patterns.

### Development Workflows

#### Common Workflows
- **Path**: `../anthropic/docs/claude-code/common-workflows.md`
- **Summary**: Step-by-step guides for typical development tasks including debugging, feature development, code review, and project maintenance using Claude Code.

#### Interactive Mode
- **Path**: `../anthropic/docs/claude-code/interactive-mode.md`
- **Summary**: Guide to Claude Code's conversational interface including session management, context preservation, and effective interaction patterns.

#### Slash Commands
- **Path**: `../anthropic/docs/claude-code/slash-commands.md`
- **Summary**: Built-in commands for enhanced productivity including file operations, Git integration, and workflow automation within Claude Code sessions.

### Integration and Extensibility

#### IDE Integrations
- **Path**: `../anthropic/docs/claude-code/ide-integrations.md`
- **Summary**: Integration guides for popular IDEs and editors including VS Code, IntelliJ, and terminal-based environments with setup instructions and best practices.

#### MCP Integration
- **Path**: `../anthropic/docs/claude-code/mcp.md`
- **Summary**: Model Context Protocol integration for extending Claude Code with custom tools, external data sources, and specialized development workflows.

#### Sub-agents
- **Path**: `../anthropic/docs/claude-code/sub-agents.md`
- **Summary**: Creating and managing specialized agents for specific tasks within Claude Code including configuration, deployment, and use case examples.

#### Hooks System
- **Path**: `../anthropic/docs/claude-code/hooks.md`
- **Summary**: Event-driven automation system for customizing Claude Code behavior including pre/post-commit hooks, build triggers, and workflow automation.

- **Path**: `../anthropic/docs/claude-code/hooks-guide.md`
- **Summary**: Detailed implementation guide for creating custom hooks with practical examples and best practices for different development scenarios.

### Enterprise and Deployment

#### Third-party Integrations
- **Path**: `../anthropic/docs/claude-code/third-party-integrations.md`
- **Summary**: Integration guides for cloud platforms and enterprise services including AWS Bedrock, Google Vertex AI, and custom API endpoints.

#### Amazon Bedrock
- **Path**: `../anthropic/docs/claude-code/amazon-bedrock.md`
- **Summary**: Specific configuration guide for using Claude Code with Amazon Bedrock including authentication, region settings, and enterprise deployment patterns.

#### Google Vertex AI
- **Path**: `../anthropic/docs/claude-code/google-vertex-ai.md`
- **Summary**: Integration guide for Google Cloud's Vertex AI platform including service account setup, permissions, and cloud-native deployment strategies.

#### GitHub Actions
- **Path**: `../anthropic/docs/claude-code/github-actions.md`
- **Summary**: CI/CD integration for automated code review, testing, and deployment using Claude Code in GitHub Actions workflows.

#### GitLab CI/CD
- **Path**: `../anthropic/docs/claude-code/gitlab-ci-cd.md`
- **Summary**: GitLab integration guide for continuous integration and deployment pipelines with Claude Code automation.

### Security and Compliance

#### Security Guide
- **Path**: `../anthropic/docs/claude-code/security.md`
- **Summary**: Security best practices, safeguards, and risk mitigation strategies for enterprise Claude Code deployments including access controls and audit trails.

#### Data Usage and Privacy
- **Path**: `../anthropic/docs/claude-code/data-usage.md`
- **Summary**: Comprehensive guide to data handling, privacy considerations, and compliance requirements for Claude Code in enterprise environments.

#### Legal and Compliance
- **Path**: `../anthropic/docs/claude-code/legal-and-compliance.md`
- **Summary**: Legal considerations, compliance requirements, and regulatory guidance for enterprise Claude Code deployments.

#### IAM and Access Control
- **Path**: `../anthropic/docs/claude-code/iam.md`
- **Summary**: Identity and access management including user authentication, permissions, and credential management for secure Claude Code deployments.

### Monitoring and Management

#### Analytics and Usage
- **Path**: `../anthropic/docs/claude-code/analytics.md`
- **Summary**: Usage analytics, performance monitoring, and insights for understanding Claude Code adoption and optimization opportunities.

#### Monitoring Usage
- **Path**: `../anthropic/docs/claude-code/monitoring-usage.md`
- **Summary**: Tools and techniques for monitoring Claude Code usage, performance metrics, and cost optimization in production environments.

#### Costs and Billing
- **Path**: `../anthropic/docs/claude-code/costs.md`
- **Summary**: Cost management strategies, billing optimization, and usage tracking for enterprise Claude Code deployments.

### Development Container Support

#### Dev Container Guide
- **Path**: `../anthropic/docs/claude-code/devcontainer.md`
- **Summary**: Development container setup for consistent Claude Code environments including Docker configuration, remote development, and team collaboration.

### Advanced Features

#### Memory System
- **Path**: `../anthropic/docs/claude-code/memory.md`
- **Summary**: Project memory and context persistence including CLAUDE.md files, knowledge management, and context optimization strategies.

#### Model Configuration
- **Path**: `../anthropic/docs/claude-code/model-config.md`
- **Summary**: Advanced model configuration options including parameter tuning, behavior customization, and performance optimization for specific use cases.

#### Output Styles
- **Path**: `../anthropic/docs/claude-code/output-styles.md`
- **Summary**: Customizing Claude Code output formatting, verbosity levels, and presentation styles for different workflow preferences.

#### Status Line
- **Path**: `../anthropic/docs/claude-code/statusline.md`
- **Summary**: Status line customization and information display including progress indicators, context awareness, and productivity enhancements.

#### Terminal Configuration
- **Path**: `../anthropic/docs/claude-code/terminal-config.md`
- **Summary**: Terminal optimization for Claude Code including shell integration, prompt customization, and performance tuning.

#### Network Configuration
- **Path**: `../anthropic/docs/claude-code/network-config.md`
- **Summary**: Network settings, proxy configuration, and connectivity options for enterprise and restricted network environments.

#### LLM Gateway
- **Path**: `../anthropic/docs/claude-code/llm-gateway.md`
- **Summary**: Enterprise LLM gateway integration for centralized model access, cost control, and security policy enforcement.

### Troubleshooting

#### Troubleshooting Guide
- **Path**: `../anthropic/docs/claude-code/troubleshooting.md`
- **Summary**: Common issues, error resolution, and debugging strategies for Claude Code including installation problems, authentication issues, and performance optimization.

## Claude Code SDK

### SDK Overview

#### SDK Introduction
- **Path**: `../anthropic/docs/claude-code/sdk/sdk-overview.md`
- **Summary**: Introduction to building custom AI agents with the Claude Code SDK including headless mode, language bindings, and production-ready features for agent development.

#### Headless Mode
- **Path**: `../anthropic/docs/claude-code/sdk/sdk-headless.md`
- **Summary**: CLI automation and scripting capabilities for building non-interactive Claude Code workflows and integration with external systems.

#### TypeScript SDK
- **Path**: `../anthropic/docs/claude-code/sdk/sdk-typescript.md`
- **Summary**: Node.js and web application development with the Claude Code TypeScript SDK including setup, configuration, and practical implementation examples.

#### Python SDK
- **Path**: `../anthropic/docs/claude-code/sdk/sdk-python.md`
- **Summary**: Python development with Claude Code SDK for data science, automation, and application integration with comprehensive code examples.

### SDK Features

#### Sessions Management
- **Path**: `../anthropic/docs/claude-code/sdk/sdk-sessions.md`
- **Summary**: Session lifecycle management including creation, persistence, state management, and cleanup for multi-turn agent interactions.

#### Permissions System
- **Path**: `../anthropic/docs/claude-code/sdk/sdk-permissions.md`
- **Summary**: Fine-grained permission control for SDK-based agents including tool access, file system permissions, and security boundaries.

#### Cost Tracking
- **Path**: `../anthropic/docs/claude-code/sdk/sdk-cost-tracking.md`
- **Summary**: Usage monitoring and cost optimization for SDK-based applications including token counting, billing integration, and budget controls.

#### Custom Tools
- **Path**: `../anthropic/docs/claude-code/sdk/custom-tools.md`
- **Summary**: Creating and integrating custom tools with the Claude Code SDK including tool definitions, implementation patterns, and best practices.

#### System Prompt Modification
- **Path**: `../anthropic/docs/claude-code/sdk/modifying-system-prompts.md`
- **Summary**: Dynamic system prompt management for customizing agent behavior, role definition, and context adaptation in SDK applications.

#### MCP Integration
- **Path**: `../anthropic/docs/claude-code/sdk/sdk-mcp.md`
- **Summary**: Model Context Protocol integration within SDK applications for external tool and data source connectivity.

#### Slash Commands
- **Path**: `../anthropic/docs/claude-code/sdk/sdk-slash-commands.md`
- **Summary**: Implementing custom slash commands in SDK applications for enhanced user interaction and workflow automation.

#### Sub-agents
- **Path**: `../anthropic/docs/claude-code/sdk/subagents.md`
- **Summary**: Creating and managing specialized sub-agents within SDK applications for task delegation and workflow orchestration.

#### Streaming vs Single Mode
- **Path**: `../anthropic/docs/claude-code/sdk/streaming-vs-single-mode.md`
- **Summary**: Understanding different interaction modes for optimal user experience and performance in SDK-based applications.

#### Todo Tracking
- **Path**: `../anthropic/docs/claude-code/sdk/todo-tracking.md`
- **Summary**: Task management and progress tracking within SDK applications for workflow organization and project management.

---

## Testing and Evaluation

### Evaluation Framework

#### Define Success Criteria
- **Path**: `../anthropic/docs/test-and-evaluate/define-success.md`
- **Summary**: Framework for establishing measurable success criteria for LLM applications including quantitative metrics, qualitative scales, and multidimensional evaluation approaches.

#### Develop Tests
- **Path**: `../anthropic/docs/test-and-evaluate/develop-tests.md`
- **Summary**: Creating comprehensive test suites for evaluating Claude applications including test case design, data collection, and validation strategies.

#### Evaluation Tool
- **Path**: `../anthropic/docs/test-and-evaluate/eval-tool.md`
- **Summary**: Anthropic's evaluation tools and methodologies for systematic testing and performance measurement of Claude-based applications.

### Quality Improvement

#### Strengthen Guardrails

##### Handle Streaming Refusals
- **Path**: `../anthropic/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md`
- **Summary**: Managing refusal scenarios in streaming responses including graceful degradation, user communication, and fallback strategies.

##### Increase Consistency
- **Path**: `../anthropic/docs/test-and-evaluate/strengthen-guardrails/increase-consistency.md`
- **Summary**: Techniques for improving response consistency across similar inputs including prompt standardization and output validation.

##### Keep Claude in Character
- **Path**: `../anthropic/docs/test-and-evaluate/strengthen-guardrails/keep-claude-in-character.md`
- **Summary**: Maintaining consistent persona and behavior throughout interactions including role enforcement and character preservation strategies.

##### Mitigate Jailbreaks
- **Path**: `../anthropic/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks.md`
- **Summary**: Security measures for preventing prompt injection and unauthorized behavior modification with detection and prevention strategies.

##### Reduce Hallucinations
- **Path**: `../anthropic/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md`
- **Summary**: Strategies for improving factual accuracy and reducing false information generation including citation requirements and verification processes.

##### Reduce Latency
- **Path**: `../anthropic/docs/test-and-evaluate/strengthen-guardrails/reduce-latency.md`
- **Summary**: Performance optimization techniques for reducing response times including caching strategies, prompt optimization, and infrastructure considerations.

##### Reduce Prompt Leak
- **Path**: `../anthropic/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak.md`
- **Summary**: Preventing exposure of system prompts and sensitive instructions including prompt protection and information boundary management.

---

## Learning Paths

### 🚀 Getting Started Path
1. [Introduction to Claude](./anthropic/docs/intro.md) - Overview and capabilities
2. [Get Started](./anthropic/docs/get-started.md) - First API call and setup
3. [Model Overview](./anthropic/docs/about-claude/models/overview.md) - Choose the right model
4. [Building with Claude](./anthropic/docs/overview.md) - Implementation workflow

### 💡 Prompt Engineering Path
1. [Prompt Engineering Overview](./anthropic/docs/build-with-claude/prompt-engineering/overview.md) - Core concepts
2. [Be Clear and Direct](./anthropic/docs/build-with-claude/prompt-engineering/be-clear-and-direct.md) - Fundamental technique
3. [Multishot Prompting](./anthropic/docs/build-with-claude/prompt-engineering/multishot-prompting.md) - Using examples
4. [Chain of Thought](./anthropic/docs/build-with-claude/prompt-engineering/chain-of-thought.md) - Step-by-step reasoning
5. [System Prompts](./anthropic/docs/build-with-claude/prompt-engineering/system-prompts.md) - Role and behavior definition

### 🔧 Tool Development Path
1. [Tool Use Overview](./anthropic/docs/agents-and-tools/tool-use/overview.md) - Core concepts and examples
2. [Implement Tool Use](./anthropic/docs/agents-and-tools/tool-use/implement-tool-use.md) - Detailed implementation
3. [MCP Overview](./anthropic/docs/mcp.md) - Protocol understanding
4. [MCP Connector](./anthropic/docs/agents-and-tools/mcp-connector.md) - Direct integration
5. [Computer Use Tool](./anthropic/docs/agents-and-tools/tool-use/computer-use-tool.md) - Advanced automation

### 💻 Claude Code Path
1. [Claude Code Overview](./anthropic/docs/claude-code/overview.md) - Introduction and value proposition
2. [Quickstart](./anthropic/docs/claude-code/quickstart.md) - Setup and first session
3. [Common Workflows](./anthropic/docs/claude-code/common-workflows.md) - Practical usage
4. [SDK Overview](./anthropic/docs/claude-code/sdk/sdk-overview.md) - Building custom agents
5. [Security Guide](./anthropic/docs/claude-code/security.md) - Enterprise considerations

### 🏢 Enterprise Implementation Path
1. [Building with Claude](./anthropic/docs/overview.md) - Enterprise capabilities
2. [Pricing Guide](./anthropic/docs/about-claude/pricing.md) - Cost considerations
3. [Security](./anthropic/docs/claude-code/security.md) - Security best practices
4. [Third-party Integrations](./anthropic/docs/claude-code/third-party-integrations.md) - Cloud platforms
5. [Legal and Compliance](./anthropic/docs/claude-code/legal-and-compliance.md) - Regulatory considerations

### 📊 Testing and Optimization Path
1. [Define Success Criteria](./anthropic/docs/test-and-evaluate/define-success.md) - Evaluation framework
2. [Develop Tests](./anthropic/docs/test-and-evaluate/develop-tests.md) - Test suite creation
3. [Prompt Caching](./anthropic/docs/build-with-claude/prompt-caching.md) - Performance optimization
4. [Batch Processing](./anthropic/docs/build-with-claude/batch-processing.md) - Cost optimization
5. [Strengthen Guardrails](./anthropic/docs/test-and-evaluate/strengthen-guardrails/) - Quality improvement

---

## Cross-References

### Model Selection
- [Choosing a Model](./anthropic/docs/about-claude/models/choosing-a-model.md) ↔ [Pricing](./anthropic/docs/about-claude/pricing.md)
- [Model Overview](./anthropic/docs/about-claude/models/overview.md) ↔ [Claude 4 Best Practices](./anthropic/docs/build-with-claude/prompt-engineering/claude-4-best-practices.md)

### Feature Integration
- [Tool Use](./anthropic/docs/agents-and-tools/tool-use/overview.md) ↔ [Claude Code](./anthropic/docs/claude-code/overview.md)
- [MCP](./anthropic/docs/mcp.md) ↔ [MCP Connector](./anthropic/docs/agents-and-tools/mcp-connector.md) ↔ [Claude Code MCP](./anthropic/docs/claude-code/mcp.md)
- [Vision](./anthropic/docs/build-with-claude/vision.md) ↔ [Computer Use](./anthropic/docs/agents-and-tools/tool-use/computer-use-tool.md)

### Enterprise Deployment
- [Security](./anthropic/docs/claude-code/security.md) ↔ [Data Usage](./anthropic/docs/claude-code/data-usage.md) ↔ [IAM](./anthropic/docs/claude-code/iam.md)
- [Amazon Bedrock](./anthropic/docs/claude-code/amazon-bedrock.md) ↔ [Google Vertex AI](./anthropic/docs/claude-code/google-vertex-ai.md)

### Development Workflows
- [Prompt Engineering](./anthropic/docs/build-with-claude/prompt-engineering/overview.md) ↔ [Testing](./anthropic/docs/test-and-evaluate/define-success.md)
- [Claude Code SDK](./anthropic/docs/claude-code/sdk/sdk-overview.md) ↔ [Custom Tools](./anthropic/docs/claude-code/sdk/custom-tools.md)

---

## Quick Reference

### Essential Starting Points
- **New to Claude**: [Introduction](./anthropic/docs/intro.md) → [Get Started](./anthropic/docs/get-started.md)
- **API Development**: [Building with Claude](./anthropic/docs/overview.md) → [Tool Use](./anthropic/docs/agents-and-tools/tool-use/overview.md)
- **Terminal Coding**: [Claude Code Overview](./anthropic/docs/claude-code/overview.md) → [Quickstart](./anthropic/docs/claude-code/quickstart.md)
- **Enterprise Deployment**: [Security](./anthropic/docs/claude-code/security.md) → [Third-party Integrations](./anthropic/docs/claude-code/third-party-integrations.md)

### Key Technical Guides
- **Performance**: [Prompt Caching](./anthropic/docs/build-with-claude/prompt-caching.md), [Batch Processing](./anthropic/docs/build-with-claude/batch-processing.md)
- **Quality**: [Strengthen Guardrails](./anthropic/docs/test-and-evaluate/strengthen-guardrails/), [Testing](./anthropic/docs/test-and-evaluate/define-success.md)
- **Integration**: [MCP](./anthropic/docs/mcp.md), [Tools](./anthropic/docs/agents-and-tools/tool-use/overview.md)
- **Extensibility**: [SDK](./anthropic/docs/claude-code/sdk/sdk-overview.md), [Custom Tools](./anthropic/docs/claude-code/sdk/custom-tools.md)

This index serves as your comprehensive navigation guide to building intelligent applications with Claude, from initial concept to production deployment.