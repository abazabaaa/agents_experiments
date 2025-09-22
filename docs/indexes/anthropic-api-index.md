# Anthropic API Documentation Index

> Comprehensive index for Claude API documentation, covering core messaging APIs, administrative endpoints, batch processing, cloud integrations, and developer tools.

This index provides organized access to all Anthropic API documentation, with detailed summaries and cross-references to help developers quickly find relevant information for their use cases.

## Table of Contents

- [Core API Reference](#core-api-reference)
- [Admin API & Organization Management](#admin-api--organization-management)
- [Batch Processing](#batch-processing)
- [Files & Document Processing](#files--document-processing)
- [Cloud Platform Integrations](#cloud-platform-integrations)
- [Client SDKs & Developer Tools](#client-sdks--developer-tools)
- [Service Information & Monitoring](#service-information--monitoring)
- [Developer Resources](#developer-resources)

---

## Core API Reference

### Messages API
- **Path**: `../anthropic/api/messages.md`
- **Summary**: Complete reference for the Messages API, Claude's primary interface for text and multimodal conversations. Covers all parameters including model selection, token limits, streaming, system prompts, and conversation management with detailed OpenAPI specifications.
- **Related**: `../anthropic/api/messages-examples.md`, `../anthropic/api/handling-stop-reasons.md`

- **Path**: `../anthropic/api/messages-examples.md`
- **Summary**: Practical examples demonstrating Messages API usage including basic requests, multi-turn conversations, vision inputs with images, prefilled responses for guided outputs, and tool use patterns. Essential for understanding real-world implementation patterns.
- **Related**: `../anthropic/api/messages.md`, `../anthropic/api/client-sdks.md`

- **Path**: `../anthropic/api/handling-stop-reasons.md`
- **Summary**: Explains different stop reasons (end_turn, max_tokens, stop_sequence, tool_use) and how to properly handle them in applications to manage conversation flow and implement robust error handling.

- **Path**: `../anthropic/api/messages-count-tokens.md`
- **Summary**: Token counting API for estimating costs and managing rate limits before sending requests. Includes detailed breakdown of input, output, and cached token calculations with practical examples.

### Models API
- **Path**: `../anthropic/api/models.md`
- **Summary**: Endpoint for retrieving specific model information including display names, creation dates, and capabilities. Essential for model discovery and resolving aliases to specific model IDs.
- **Related**: `../anthropic/api/models-list.md`

- **Path**: `../anthropic/api/models-list.md`
- **Summary**: Lists all available Claude models with their IDs, capabilities, and specifications. Critical reference for choosing the right model for specific use cases and understanding model progression.

### API Fundamentals
- **Path**: `../anthropic/api/overview.md`
- **Summary**: Essential starting point covering API authentication, request/response formats, size limits, and basic usage patterns. Includes code examples in multiple languages and explains core concepts like API keys and workspaces.

- **Path**: `../anthropic/api/versioning.md`
- **Summary**: API versioning strategy and change management policy. Explains required anthropic-version header, backwards compatibility guarantees, and version history including streaming event format changes.

- **Path**: `../anthropic/api/beta-headers.md`
- **Summary**: How to access beta features using anthropic-beta headers. Covers feature flags, multiple beta usage, and integration with client SDKs for accessing experimental capabilities.

---

## Admin API & Organization Management

### Admin API Overview
- **Path**: `../anthropic/api/administration-api.md`
- **Summary**: Comprehensive guide to programmatic organization management including user roles, workspace administration, API key management, and organizational access control. Requires special Admin API keys for enterprise operations.
- **Related**: `../anthropic/api/usage-cost-api.md`, `../anthropic/api/claude-code-analytics-api.md`

### API Keys Management
- **Path**: `../anthropic/api/admin-api/apikeys/list-api-keys.md`
- **Summary**: Endpoint for listing organization API keys with filtering by status, workspace, and creation date. Essential for API key auditing and management workflows.

- **Path**: `../anthropic/api/admin-api/apikeys/get-api-key.md`
- **Summary**: Retrieve detailed information about specific API keys including usage statistics, permissions, and metadata for security and compliance monitoring.

- **Path**: `../anthropic/api/admin-api/apikeys/update-api-key.md`
- **Summary**: Modify API key properties including name, status (active/inactive), and metadata. Critical for key lifecycle management and security operations.

### User & Organization Management
- **Path**: `../anthropic/api/admin-api/users/list-users.md`
- **Summary**: List organization members with role information, filtering capabilities, and pagination. Essential for user auditing and role management workflows.

- **Path**: `../anthropic/api/admin-api/users/get-user.md`
- **Summary**: Retrieve detailed user information including roles, workspace memberships, and activity status for individual user management.

- **Path**: `../anthropic/api/admin-api/users/update-user.md`
- **Summary**: Modify user roles (user, developer, billing, admin) and permissions. Core endpoint for user lifecycle management and access control.

- **Path**: `../anthropic/api/admin-api/users/remove-user.md`
- **Summary**: Remove users from organization with proper cleanup of associated resources. Includes safety constraints for admin role removal.

- **Path**: `../anthropic/api/admin-api/organization/get-me.md`
- **Summary**: Retrieve current organization information including ID, name, and metadata. Useful for confirming Admin API key scope and organization identity.

### Invitation Management
- **Path**: `../anthropic/api/admin-api/invites/create-invite.md`
- **Summary**: Send organization invitations with role assignments and expiration management. Streamlines user onboarding workflows with proper role provisioning.

- **Path**: `../anthropic/api/admin-api/invites/list-invites.md`
- **Summary**: Manage pending invitations with status tracking, filtering, and bulk operations. Essential for invitation lifecycle management.

- **Path**: `../anthropic/api/admin-api/invites/get-invite.md`
- **Summary**: Retrieve detailed invitation information including status, expiration, and recipient details for invitation tracking.

- **Path**: `../anthropic/api/admin-api/invites/delete-invite.md`
- **Summary**: Cancel pending invitations with proper cleanup. Important for managing invitation security and preventing unauthorized access.

### Workspace Management
- **Path**: `../anthropic/api/admin-api/workspaces/list-workspaces.md`
- **Summary**: List organization workspaces with filtering by archive status and creation date. Essential for workspace organization and resource allocation.

- **Path**: `../anthropic/api/admin-api/workspaces/create-workspace.md`
- **Summary**: Create new workspaces for resource organization and access control. Enables team-based API key and usage management.

- **Path**: `../anthropic/api/admin-api/workspaces/get-workspace.md`
- **Summary**: Retrieve detailed workspace information including members, settings, and usage statistics for workspace management.

- **Path**: `../anthropic/api/admin-api/workspaces/update-workspace.md`
- **Summary**: Modify workspace properties including name, description, and configuration settings for organizational management.

- **Path**: `../anthropic/api/admin-api/workspaces/archive-workspace.md`
- **Summary**: Archive workspaces while preserving data and API keys. Important for workspace lifecycle management and organization cleanup.

### Workspace Member Management
- **Path**: `../anthropic/api/admin-api/workspace_members/list-workspace-members.md`
- **Summary**: List workspace members with role information and filtering capabilities. Essential for workspace-level access control and auditing.

- **Path**: `../anthropic/api/admin-api/workspace_members/create-workspace-member.md`
- **Summary**: Add users to workspaces with specific roles (workspace_admin, workspace_developer, workspace_user). Core functionality for team access management.

- **Path**: `../anthropic/api/admin-api/workspace_members/get-workspace-member.md`
- **Summary**: Retrieve detailed member information within workspace context including role and permissions for individual access management.

- **Path**: `../anthropic/api/admin-api/workspace_members/update-workspace-member.md`
- **Summary**: Modify workspace member roles and permissions. Critical for maintaining proper access control as team roles evolve.

- **Path**: `../anthropic/api/admin-api/workspace_members/delete-workspace-member.md`
- **Summary**: Remove members from workspaces with proper access revocation. Essential for offboarding and access control management.

### Usage & Cost Reporting
- **Path**: `../anthropic/api/usage-cost-api.md`
- **Summary**: Comprehensive API for accessing detailed usage and cost data with granular filtering by workspace, model, and time periods. Essential for cost optimization, billing reconciliation, and rate limit management with partner platform integrations.
- **Related**: `../anthropic/api/admin-api/usage-cost/get-messages-usage-report.md`, `../anthropic/api/admin-api/usage-cost/get-cost-report.md`

- **Path**: `../anthropic/api/admin-api/usage-cost/get-messages-usage-report.md`
- **Summary**: Detailed usage reporting endpoint with token breakdowns, grouping capabilities, and time series data. Supports filtering by model, workspace, service tier, and provides cache efficiency metrics.

- **Path**: `../anthropic/api/admin-api/usage-cost/get-cost-report.md`
- **Summary**: Cost reporting in USD with service-level breakdowns including token usage, web search, and code execution costs. Essential for financial tracking and chargeback operations.

### Claude Code Analytics
- **Path**: `../anthropic/api/claude-code-analytics-api.md`
- **Summary**: Specialized analytics API for Claude Code usage providing productivity metrics, session data, code generation statistics, and developer activity insights. Essential for measuring development team productivity and Claude Code adoption.

- **Path**: `../anthropic/api/admin-api/claude-code/get-claude-code-usage-report.md`
- **Summary**: Detailed Claude Code usage reports with daily aggregated metrics including sessions, lines of code, commits, pull requests, and cost data broken down by user and model.

---

## Batch Processing

### Message Batches Overview
- **Path**: `../anthropic/api/messages-batch-examples.md`
- **Summary**: Practical examples for implementing batch processing workflows including request formatting, error handling, and result retrieval patterns. Essential for understanding asynchronous processing implementation.
- **Related**: `../anthropic/api/creating-message-batches.md`, `../anthropic/api/retrieving-message-batch-results.md`

### Batch Management Operations
- **Path**: `../anthropic/api/creating-message-batches.md`
- **Summary**: Create batch requests for processing up to 10,000 messages asynchronously with 50% cost savings. Includes request formatting, custom IDs, and batch submission patterns for high-volume applications.

- **Path**: `../anthropic/api/listing-message-batches.md`
- **Summary**: List and filter batch requests by status, creation date, and other criteria. Essential for monitoring batch processing workflows and managing large-scale operations.

- **Path**: `../anthropic/api/retrieving-message-batches.md`
- **Summary**: Get detailed information about specific batch requests including processing status, completion metrics, and metadata for batch lifecycle management.

- **Path**: `../anthropic/api/retrieving-message-batch-results.md`
- **Summary**: Access processed batch results with individual message responses, error handling, and success/failure tracking. Critical for implementing robust batch processing workflows.

- **Path**: `../anthropic/api/canceling-message-batches.md`
- **Summary**: Cancel pending or in-progress batch requests with proper resource cleanup. Important for managing processing resources and handling changed requirements.

- **Path**: `../anthropic/api/deleting-message-batches.md`
- **Summary**: Remove completed batch requests and associated data for cleanup and storage management. Essential for maintaining organized batch processing history.

---

## Files & Document Processing

### File Management API
- **Path**: `../anthropic/api/files-create.md`
- **Summary**: Upload files up to 500MB including PDFs, images, and documents for processing with Claude. Supports multipart uploads and returns file metadata for reference in messages.

- **Path**: `../anthropic/api/files-list.md`
- **Summary**: List uploaded files with filtering and pagination capabilities. Essential for file management and reference in message conversations.

- **Path**: `../anthropic/api/files-metadata.md`
- **Summary**: Retrieve detailed file information including size, type, upload date, and processing status for file lifecycle management.

- **Path**: `../anthropic/api/files-content.md`
- **Summary**: Access file content and processing results including text extraction and analysis data for integration with message workflows.

- **Path**: `../anthropic/api/files-delete.md`
- **Summary**: Remove uploaded files with proper cleanup of associated resources. Important for managing storage costs and data retention compliance.

---

## Cloud Platform Integrations

### Amazon Bedrock Integration
- **Path**: `../anthropic/api/claude-on-amazon-bedrock.md`
- **Summary**: Complete integration guide for accessing Claude through AWS Bedrock including authentication, model selection, request formatting, and feature support differences. Covers specialized Bedrock model names and PDF processing capabilities.

### Google Cloud Vertex AI Integration
- **Path**: `../anthropic/api/claude-on-vertex-ai.md`
- **Summary**: Integration guide for Google Cloud Vertex AI access including authentication, project setup, model availability by region, and request format differences from direct API usage.

---

## Client SDKs & Developer Tools

### Official SDKs
- **Path**: `../anthropic/api/client-sdks.md`
- **Summary**: Comprehensive guide to official Anthropic SDKs in Python, TypeScript, Java, Go, C#, Ruby, and PHP. Includes installation, usage examples, model constants, and beta feature access patterns for all supported languages.

- **Path**: `../anthropic/api/openai-sdk.md`
- **Summary**: OpenAI SDK compatibility layer for testing and migration purposes. Covers supported features, limitations, system message handling, and differences from native Claude API for gradual migration scenarios.

### Prompt Development Tools
- **Path**: `../anthropic/api/prompt-tools-generate.md`
- **Summary**: Experimental API for generating well-structured prompts from task descriptions. Returns ready-to-use message formats and assistant prefills to jumpstart prompt engineering workflows.

- **Path**: `../anthropic/api/prompt-tools-improve.md`
- **Summary**: API for enhancing existing prompts with better structure, clarity, and effectiveness. Useful for optimizing prompt performance and consistency across applications.

- **Path**: `../anthropic/api/prompt-tools-templatize.md`
- **Summary**: Convert prompts into reusable templates with variable placeholders. Essential for creating maintainable prompt libraries and standardizing prompt patterns across teams.

---

## Service Information & Monitoring

### Service Levels & Pricing
- **Path**: `../anthropic/api/service-tiers.md`
- **Summary**: Detailed explanation of Priority Tier vs Standard Tier service levels including availability guarantees, cost controls, automatic fallback, and commitment options. Essential for production deployment planning.

- **Path**: `../anthropic/api/rate-limits.md`
- **Summary**: Comprehensive rate limiting documentation including usage tiers, spend limits, token-based limits (RPM, ITPM, OTPM), tier advancement requirements, and monitoring capabilities. Critical for capacity planning and optimization.

### Error Handling & Monitoring
- **Path**: `../anthropic/api/errors.md`
- **Summary**: Complete error reference covering HTTP status codes, error types, request size limits, and proper error handling patterns. Includes request ID tracking for support and debugging workflows.

- **Path**: `../anthropic/api/ip-addresses.md`
- **Summary**: IP address ranges and networking information for firewall configuration and network security planning in enterprise environments.

- **Path**: `../anthropic/api/supported-regions.md`
- **Summary**: Geographic availability and data residency information for Claude API services. Important for compliance and latency optimization planning.

---

## Developer Resources

### Migration & Integration Guides
- **Path**: `../anthropic/api/migrating-from-text-completions-to-messages.md`
- **Summary**: Migration guide from legacy text completion APIs to the modern Messages API including pattern translations, parameter mapping, and best practices for updating existing integrations.

### Support & Documentation
- **Path**: `../anthropic/api/getting-help.md`
- **Summary**: Support resources, documentation links, community channels, and escalation procedures for technical assistance and issue resolution.

---

## Key Integration Patterns

### Authentication Flow
1. Start with `../anthropic/api/overview.md` for API key setup
2. Review `../anthropic/api/administration-api.md` for organization management
3. Use `../anthropic/api/admin-api/apikeys/` endpoints for key lifecycle management

### Message Processing Workflow
1. Begin with `../anthropic/api/messages-examples.md` for basic patterns
2. Implement error handling using `../anthropic/api/errors.md`
3. Add batch processing with `../anthropic/api/creating-message-batches.md`
4. Monitor usage with `../anthropic/api/usage-cost-api.md`

### Production Deployment
1. Configure service tiers using `../anthropic/api/service-tiers.md`
2. Set up rate limiting with `../anthropic/api/rate-limits.md`
3. Implement monitoring with `../anthropic/api/administration-api.md`
4. Plan capacity with usage and cost APIs

### Cloud Integration
1. Choose platform: `../anthropic/api/claude-on-amazon-bedrock.md` or `../anthropic/api/claude-on-vertex-ai.md`
2. Configure authentication and model access
3. Adapt request formats for platform-specific requirements
4. Enable logging and monitoring as needed

This index provides comprehensive navigation for the Anthropic API documentation, organized by functionality and use case to help developers quickly find relevant information for their specific implementation needs.