# Anthropic Examples Index

This comprehensive index organizes Anthropic's example code and applications by skill level and use case, providing clear navigation for developers building with Claude.

## Overview

The Anthropic examples repository contains production-ready applications, educational guides, and implementation patterns spanning from beginner tutorials to advanced AI workflows. Examples are organized by complexity and demonstrate real-world applications across domains like customer support, financial analysis, content generation, and agent systems.

---

## 🎯 Production Applications

### Customer Support Systems
- **Path**: `../anthropic/examples/customer-support-agent/`
- **Summary**: Full-stack Next.js application demonstrating AI-powered customer support with Amazon Bedrock knowledge base integration. Features real-time thinking display, mood detection, customizable UI components, and AWS Amplify deployment configuration.
- **Key Files**: `../anthropic/examples/customer-support-agent/README.md`, `./customer-support-agent/components/ChatArea.tsx`
- **Complexity**: Advanced
- **Technologies**: Next.js, TypeScript, AWS Bedrock, Amplify, shadcn/ui

### Financial Data Analyst
- **Path**: `../anthropic/examples/financial-data-analyst/`
- **Summary**: Interactive data visualization platform combining Claude's analytical capabilities with chart generation. Supports multi-format file uploads (PDF, CSV, images) and generates dynamic visualizations including line charts, bar charts, pie charts, and area charts.
- **Key Files**: `../anthropic/examples/financial-data-analyst/README.md`, `./financial-data-analyst/app/page.tsx`
- **Complexity**: Advanced
- **Technologies**: Next.js, Recharts, PDF.js, Anthropic SDK

---

## 🤖 Agent Patterns & Implementations

### Core Agent Framework
- **Path**: `../anthropic/examples/agents/`
- **Summary**: Educational reference implementation demonstrating agent fundamentals with <300 lines of core logic. Shows tool execution loops, MCP server integration, and message history management. Not production-ready but excellent for learning.
- **Key Files**: `../anthropic/examples/agents/agent.py`, `./agents/README.md`, `./agents/agent_demo.ipynb`
- **Complexity**: Intermediate
- **Technologies**: Python, MCP Protocol, async/await

### Agent Design Patterns
- **Path**: `../anthropic/examples/patterns/agents/`
- **Summary**: Implementation patterns from Anthropic's "Building Effective Agents" research. Demonstrates prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer workflows with practical examples.
- **Key Files**: `../anthropic/examples/patterns/agents/basic_workflows.ipynb`, `./patterns/agents/orchestrator_workers.ipynb`, `./patterns/agents/evaluator_optimizer.ipynb`
- **Complexity**: Advanced
- **Technologies**: Concurrent processing, multi-LLM coordination

---

## 🛠️ Tool Use & Integration

### Tool Use Fundamentals
- **Path**: `../anthropic/examples/tool_use/customer_service_agent.ipynb`
- **Summary**: Step-by-step tutorial for creating customer service chatbots with client-side tools. Demonstrates tool definition, synthetic data simulation, and tool result processing patterns.
- **Complexity**: Beginner to Intermediate

### Advanced Tool Patterns
- **Path**: `../anthropic/examples/tool_use/`
- **Summary**: Complete collection of tool use patterns including parallel tool execution, tool choice strategies, structured JSON extraction, Pydantic integration, vision with tools, and memory management.
- **Key Files**: `../anthropic/examples/tool_use/parallel_tools_claude_3_7_sonnet.ipynb`, `./tool_use/tool_choice.ipynb`, `./tool_use/extracting_structured_json.ipynb`, `./tool_use/memory_cookbook.ipynb`
- **Complexity**: Intermediate to Advanced

### Calculator and Mathematical Tools
- **Path**: `../anthropic/examples/tool_use/calculator_tool.ipynb`
- **Summary**: Demonstrates mathematical computation capabilities through tool integration, showing how to extend Claude's reasoning with external calculation engines.
- **Complexity**: Beginner

---

## 🎨 Multimodal & Vision

### Vision Fundamentals
- **Path**: `../anthropic/examples/multimodal/getting_started_with_vision.ipynb`
- **Summary**: Introduction to passing images to Claude via base64 encoding and URLs. Covers basic image analysis, description generation, and multimodal prompt construction.
- **Complexity**: Beginner

### Advanced Vision Techniques
- **Path**: `../anthropic/examples/multimodal/`
- **Summary**: Comprehensive vision capabilities including best practices, text transcription from images, chart/graph analysis, PowerPoint processing, and sub-agent coordination for complex visual tasks.
- **Key Files**: `../anthropic/examples/multimodal/best_practices_for_vision.ipynb`, `./multimodal/reading_charts_graphs_powerpoints.ipynb`, `./multimodal/using_sub_agents.ipynb`
- **Complexity**: Intermediate to Advanced

---

## 📚 Core Skills & Techniques

### Classification Systems
- **Path**: `../anthropic/examples/skills/classification/guide.ipynb`
- **Summary**: Comprehensive guide to building classification systems for complex business rules and limited training data scenarios. Covers RAG integration, prompt engineering, chain-of-thought reasoning, and evaluation with insurance support ticket examples.
- **Examples**: `./skills/classification/evaluation/`, `./skills/classification/data/`
- **Complexity**: Intermediate to Advanced

### Retrieval-Augmented Generation (RAG)
- **Path**: `../anthropic/examples/skills/retrieval_augmented_generation/guide.ipynb`
- **Summary**: Complete RAG system implementation with performance optimization techniques. Demonstrates basic RAG, summary indexing, re-ranking, and comprehensive evaluation methodologies achieving 71% → 81% accuracy improvements.
- **Examples**: `./skills/retrieval_augmented_generation/evaluation/`
- **Complexity**: Advanced

### Contextual Retrieval Enhancement
- **Path**: `../anthropic/examples/skills/contextual-embeddings/guide.ipynb`
- **Summary**: Advanced RAG improvement technique using contextual embeddings to reduce retrieval failure rates by 35%. Includes BM25 hybrid search, prompt caching optimization, and AWS Lambda deployment code.
- **Examples**: `./skills/contextual-embeddings/contextual-rag-lambda-function/`
- **Complexity**: Advanced

### Document Summarization
- **Path**: `../anthropic/examples/skills/summarization/guide.ipynb`
- **Summary**: Legal document summarization with multi-shot learning, domain-specific guidance, meta-summarization for multiple documents, and summary-indexed RAG approaches. Includes comprehensive evaluation frameworks.
- **Examples**: `./skills/summarization/data/`, `./skills/summarization/evaluation/`
- **Complexity**: Intermediate to Advanced

### Text-to-SQL Generation
- **Path**: `../anthropic/examples/skills/text_to_sql/guide.ipynb`
- **Summary**: Natural language to SQL conversion with progressive prompt improvement techniques. Covers basic prompting, few-shot examples, chain-of-thought reasoning, RAG for complex schemas, and self-improvement loops.
- **Examples**: `./skills/text_to_sql/evaluation/`
- **Complexity**: Intermediate to Advanced

---

## 🧪 Advanced Features & Capabilities

### Extended Thinking
- **Path**: `../anthropic/examples/extended_thinking/`
- **Summary**: Demonstrates Claude's extended reasoning capabilities for complex problem-solving. Shows both standalone extended thinking and integration with tool use for enhanced analytical workflows.
- **Key Files**: `../anthropic/examples/extended_thinking/extended_thinking.ipynb`, `./extended_thinking/extended_thinking_with_tool_use.ipynb`
- **Complexity**: Advanced

### Fine-tuning Integration
- **Path**: `../anthropic/examples/finetuning/finetuning_on_bedrock.ipynb`
- **Summary**: Guide for fine-tuning Claude models on AWS Bedrock, including dataset preparation, training configuration, and deployment strategies for domain-specific adaptations.
- **Complexity**: Advanced

### Observability & Monitoring
- **Path**: `../anthropic/examples/observability/usage_cost_api.ipynb`
- **Summary**: Implementation patterns for monitoring Claude API usage, cost tracking, and performance metrics essential for production deployments.
- **Complexity**: Intermediate

### Tool Evaluation Framework
- **Path**: `../anthropic/examples/tool_evaluation/tool_evaluation.ipynb`
- **Summary**: Systematic approach to evaluating tool use performance, measuring accuracy, and optimizing tool selection strategies for complex agent workflows.
- **Complexity**: Advanced

---

## 🔧 Utilities & Techniques

### Evaluation & Testing
- **Path**: `../anthropic/examples/misc/building_evals.ipynb`
- **Summary**: Comprehensive guide to building evaluation systems with code-based, human, and model-based grading approaches. Essential for measuring and improving Claude's performance on specific tasks.
- **Complexity**: Intermediate

### Content Generation Utilities
- **Path**: `../anthropic/examples/misc/`
- **Summary**: Collection of practical utilities including PDF summarization, test case generation, metaprompting, SQL query generation, citations, content moderation, and batch processing techniques.
- **Key Files**: `../anthropic/examples/misc/pdf_upload_summarization.ipynb`, `./misc/generate_test_cases.ipynb`, `./misc/metaprompt.ipynb`
- **Complexity**: Beginner to Intermediate

### Prompt Optimization Techniques
- **Path**: `../anthropic/examples/misc/prompt_caching.ipynb`, `./misc/speculative_prompt_caching.ipynb`
- **Summary**: Advanced prompt caching strategies for cost optimization and latency reduction in production environments. Includes speculative caching for improved performance.
- **Complexity**: Intermediate to Advanced

### Web Integration
- **Path**: `../anthropic/examples/misc/read_web_pages_with_haiku.ipynb`
- **Summary**: Demonstrates web content processing with Claude Haiku for cost-effective information extraction and analysis from web pages.
- **Complexity**: Beginner to Intermediate

---

## 📊 Learning Progression Guide

### Beginner Path
1. Start with `./multimodal/getting_started_with_vision.ipynb` for basic Claude interaction
2. Explore `./tool_use/customer_service_agent.ipynb` for tool use fundamentals
3. Try `./misc/building_evals.ipynb` to understand evaluation concepts

### Intermediate Path
1. Work through `./skills/classification/guide.ipynb` for practical AI applications
2. Study `./agents/agent_demo.ipynb` for agent concepts
3. Implement `./skills/summarization/guide.ipynb` for document processing

### Advanced Path
1. Master `./skills/retrieval_augmented_generation/guide.ipynb` for RAG systems
2. Explore `./patterns/agents/` for sophisticated agent architectures
3. Deploy `./customer-support-agent/` or `./financial-data-analyst/` for production experience

---

## 🏗️ Architecture Patterns

### Client-Side Applications
- Next.js applications with TypeScript
- shadcn/ui component libraries
- Real-time streaming interfaces
- AWS/cloud service integration

### Agent Systems
- Tool execution loops
- MCP protocol integration
- Async/await patterns
- Message history management

### Evaluation Systems
- Multi-modal grading approaches
- Promptfoo integration
- Performance benchmarking
- Cost optimization strategies

---

## 📈 Performance & Optimization

### Cost Optimization
- Prompt caching implementations (77% token savings demonstrated)
- Model selection strategies (Haiku vs Sonnet trade-offs)
- Batch processing techniques

### Accuracy Improvements
- RAG performance: 71% → 81% accuracy
- Contextual embeddings: 35% failure rate reduction
- Classification systems: 95%+ accuracy on complex tasks

### Production Readiness
- AWS deployment configurations
- Error handling and fallback strategies
- Scalability considerations
- Monitoring and observability

---

## 🔗 Related Resources

### External Dependencies
- **Voyage AI**: Embedding models for RAG systems
- **AWS Bedrock**: Knowledge base integration
- **Promptfoo**: Evaluation framework
- **MCP Protocol**: Tool integration standard

### Documentation Links
- Individual README files in each directory provide detailed setup instructions
- Evaluation directories contain comprehensive testing frameworks
- Lambda function code available for AWS deployments

This index serves as your navigation guide through Anthropic's comprehensive example collection. Each entry provides the essential context needed to quickly identify relevant examples for your specific use case and skill level.