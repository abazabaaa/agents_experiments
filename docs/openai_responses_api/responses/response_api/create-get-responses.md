
```json
{
  "api_reference": {
    "title": "OpenAI Get Response API Reference",
    "endpoint": "GET https://api.openai.com/v1/responses/{response_id}",
    "version": "1.0",
    "last_updated": "2024",
    
    "overview": {
      "description": "Retrieves a previously created model response by its unique identifier. Supports streaming, selective field inclusion, and resumable streaming from specific sequence points.",
      "key_features": [
        "Retrieve stored model responses",
        "Stream response data via SSE",
        "Selective field inclusion for optimized payloads",
        "Resumable streaming with sequence control",
        "Stream obfuscation for normalized payload sizes"
      ],
      "use_cases": [
        "Polling background response results",
        "Retrieving conversation history",
        "Resuming interrupted streams",
        "Auditing previous model outputs",
        "Implementing response caching"
      ]
    },
    
    "authentication": {
      "method": "Bearer Token",
      "header": "Authorization: Bearer YOUR_API_KEY",
      "example": "curl -H 'Authorization: Bearer sk-...' https://api.openai.com/v1/responses/resp_abc123"
    },
    
    "request": {
      "method": "GET",
      "url_structure": {
        "base": "https://api.openai.com/v1/responses",
        "path_parameters": {
          "response_id": {
            "type": "string",
            "required": true,
            "description": "Unique identifier of the response to retrieve",
            "format": "resp_[alphanumeric]",
            "example": "resp_abc123def456"
          }
        }
      },
      
      "query_parameters": {
        "include": {
          "type": "array",
          "required": false,
          "description": "Additional fields to include in the response payload",
          "format": "Comma-separated list or multiple include[] parameters",
          "supported_values": [
            {
              "value": "web_search_call.action.sources",
              "description": "Include web search sources when web search was used"
            },
            {
              "value": "code_interpreter_call.outputs",
              "description": "Include code interpreter execution outputs"
            },
            {
              "value": "computer_call_output.output.image_url",
              "description": "Include screenshots from computer use"
            },
            {
              "value": "file_search_call.results",
              "description": "Include file search results and snippets"
            },
            {
              "value": "message.input_image.image_url",
              "description": "Include input image URLs in the response"
            },
            {
              "value": "message.output_text.logprobs",
              "description": "Include token log probabilities"
            },
            {
              "value": "reasoning.encrypted_content",
              "description": "Include encrypted reasoning content (o-series models)"
            }
          ],
          "examples": [
            {
              "single": "?include=message.output_text.logprobs",
              "multiple": "?include=web_search_call.action.sources&include=file_search_call.results",
              "array": "?include[]=web_search_call.action.sources&include[]=file_search_call.results"
            }
          ]
        },
        
        "stream": {
          "type": "boolean",
          "required": false,
          "default": false,
          "description": "Enable server-sent events streaming for the response",
          "behavior": {
            "false": "Returns complete response as JSON",
            "true": "Streams response as SSE with delta events"
          },
          "example": "?stream=true"
        },
        
        "include_obfuscation": {
          "type": "boolean",
          "required": false,
          "default": false,
          "description": "Add random characters to normalize streaming payload sizes",
          "applies_when": "stream=true",
          "purpose": "Prevents timing attacks and improves streaming consistency",
          "example": "?stream=true&include_obfuscation=true"
        },
        
        "starting_after": {
          "type": "integer",
          "required": false,
          "description": "Resume streaming from after this sequence number",
          "applies_when": "stream=true",
          "use_case": "Resume interrupted streams or replay from checkpoint",
          "behavior": "Events with sequence_number <= starting_after are skipped",
          "example": "?stream=true&starting_after=42"
        }
      },
      
      "url_examples": [
        {
          "description": "Basic retrieval",
          "url": "GET https://api.openai.com/v1/responses/resp_abc123"
        },
        {
          "description": "Include log probabilities",
          "url": "GET https://api.openai.com/v1/responses/resp_abc123?include=message.output_text.logprobs"
        },
        {
          "description": "Stream with obfuscation",
          "url": "GET https://api.openai.com/v1/responses/resp_abc123?stream=true&include_obfuscation=true"
        },
        {
          "description": "Resume streaming from sequence 100",
          "url": "GET https://api.openai.com/v1/responses/resp_abc123?stream=true&starting_after=100"
        },
        {
          "description": "Multiple includes",
          "url": "GET https://api.openai.com/v1/responses/resp_abc123?include=web_search_call.action.sources&include=file_search_call.results"
        }
      ]
    },
    
    "response": {
      "non_streaming_response": {
        "status_code": 200,
        "content_type": "application/json",
        "structure": {
          "id": {
            "type": "string",
            "description": "Unique response identifier",
            "example": "resp_abc123def456"
          },
          "object": {
            "type": "string",
            "value": "response",
            "description": "Object type identifier"
          },
          "created": {
            "type": "integer",
            "description": "Unix timestamp of creation",
            "example": 1703123456
          },
          "model": {
            "type": "string",
            "description": "Model used for generation",
            "example": "gpt-4o"
          },
          "status": {
            "type": "string",
            "description": "Response processing status",
            "values": ["completed", "processing", "failed"],
            "example": "completed"
          },
          "choices": {
            "type": "array",
            "description": "Generated response choices",
            "items": {
              "index": {
                "type": "integer",
                "description": "Choice index"
              },
              "message": {
                "role": {
                  "type": "string",
                  "value": "assistant"
                },
                "content": {
                  "type": "string | null",
                  "description": "Generated text content"
                },
                "tool_calls": {
                  "type": "array | null",
                  "description": "Tool/function calls made by the model"
                }
              },
              "finish_reason": {
                "type": "string",
                "values": ["stop", "tool_calls", "length", "content_filter"],
                "description": "Reason for completion"
              }
            }
          },
          "usage": {
            "type": "object",
            "description": "Token usage statistics",
            "properties": {
              "prompt_tokens": {
                "type": "integer",
                "description": "Input token count"
              },
              "completion_tokens": {
                "type": "integer",
                "description": "Output token count"
              },
              "total_tokens": {
                "type": "integer",
                "description": "Total tokens used"
              },
              "reasoning_tokens": {
                "type": "integer | null",
                "description": "Reasoning tokens (o-series models only)"
              }
            }
          },
          "metadata": {
            "type": "object | null",
            "description": "Custom metadata attached to response",
            "example": {"user_id": "12345", "session": "abc"}
          },
          "service_tier": {
            "type": "string",
            "description": "Service tier used",
            "values": ["default", "flex", "priority"]
          },
          "system_fingerprint": {
            "type": "string",
            "description": "Model version identifier",
            "example": "fp_44709d6fcb"
          },
          "conditionally_included_fields": {
            "description": "Fields included based on 'include' parameter",
            "examples": {
              "logprobs": {
                "condition": "include=message.output_text.logprobs",
                "structure": {
                  "tokens": ["array of tokens"],
                  "token_logprobs": ["array of log probabilities"],
                  "top_logprobs": ["array of top alternatives"]
                }
              },
              "web_search_sources": {
                "condition": "include=web_search_call.action.sources",
                "structure": {
                  "sources": [
                    {
                      "url": "Source URL",
                      "title": "Page title",
                      "snippet": "Relevant excerpt"
                    }
                  ]
                }
              }
            }
          }
        }
      },
      
      "streaming_response": {
        "status_code": 200,
        "content_type": "text/event-stream",
        "event_structure": {
          "format": "Server-Sent Events (SSE)",
          "encoding": "UTF-8",
          "events": [
            {
              "event": "response.start",
              "data_fields": {
                "id": "Response ID",
                "object": "response",
                "created": "Unix timestamp",
                "model": "Model identifier",
                "sequence_number": "Starting sequence number"
              },
              "example": "event: response.start\ndata: {\"id\":\"resp_abc123\",\"object\":\"response\",\"created\":1703123456,\"model\":\"gpt-4o\",\"sequence_number\":0}\n\n"
            },
            {
              "event": "response.delta",
              "data_fields": {
                "delta": {
                  "content": "Incremental text content",
                  "tool_calls": "Incremental tool call data"
                },
                "sequence_number": "Event sequence number",
                "obfuscation": "Random characters (if include_obfuscation=true)"
              },
              "example": "event: response.delta\ndata: {\"delta\":{\"content\":\"Hello\"},\"sequence_number\":1}\n\n"
            },
            {
              "event": "response.done",
              "data_fields": {
                "usage": "Token usage statistics",
                "finish_reason": "Completion reason",
                "sequence_number": "Final sequence number"
              },
              "example": "event: response.done\ndata: {\"usage\":{\"total_tokens\":150},\"finish_reason\":\"stop\",\"sequence_number\":42}\n\n"
            },
            {
              "event": "error",
              "data_fields": {
                "error": {
                  "type": "Error type",
                  "message": "Error description"
                }
              },
              "example": "event: error\ndata: {\"error\":{\"type\":\"stream_error\",\"message\":\"Stream interrupted\"}}\n\n"
            }
          ],
          "connection_handling": {
            "keep_alive": "Periodic :ping events sent every 30 seconds",
            "timeout": "Connection closes after 5 minutes of inactivity",
            "reconnection": "Use starting_after parameter to resume"
          }
        }
      },
      
      "background_response_states": {
        "processing": {
          "status_code": 200,
          "body": {
            "id": "Response ID",
            "status": "processing",
            "check_after": "Seconds to wait before retry",
            "progress": "Optional progress percentage"
          }
        },
        "completed": {
          "status_code": 200,
          "body": "Full response object with generated content"
        },
        "failed": {
          "status_code": 200,
          "body": {
            "id": "Response ID",
            "status": "failed",
            "error": {
              "type": "Error type",
              "message": "Error description"
            }
          }
        }
      }
    },
    
    "error_responses": {
      "404_not_found": {
        "status_code": 404,
        "description": "Response ID does not exist or has expired",
        "body": {
          "error": {
            "type": "not_found_error",
            "message": "Response with ID 'resp_xyz' not found",
            "code": "response_not_found"
          }
        }
      },
      
      "401_unauthorized": {
        "status_code": 401,
        "description": "Invalid or missing API key",
        "body": {
          "error": {
            "type": "authentication_error",
            "message": "Invalid API key provided",
            "code": "invalid_api_key"
          }
        }
      },
      
      "403_forbidden": {
        "status_code": 403,
        "description": "No access to this response",
        "body": {
          "error": {
            "type": "permission_error",
            "message": "You don't have access to this response",
            "code": "access_denied"
          }
        }
      },
      
      "429_rate_limit": {
        "status_code": 429,
        "description": "Rate limit exceeded",
        "body": {
          "error": {
            "type": "rate_limit_error",
            "message": "Rate limit exceeded",
            "code": "rate_limit_exceeded"
          }
        },
        "headers": {
          "x-ratelimit-limit": "Request limit",
          "x-ratelimit-remaining": "Remaining requests",
          "x-ratelimit-reset": "Reset timestamp"
        }
      },
      
      "500_server_error": {
        "status_code": 500,
        "description": "Internal server error",
        "body": {
          "error": {
            "type": "server_error",
            "message": "An internal error occurred",
            "code": "internal_error"
          }
        }
      }
    },
    
    "examples": {
      "basic_retrieval": {
        "description": "Retrieve a completed response",
        "request": {
          "method": "GET",
          "url": "https://api.openai.com/v1/responses/resp_abc123",
          "headers": {
            "Authorization": "Bearer sk-..."
          }
        },
        "response": {
          "status": 200,
          "body": {
            "id": "resp_abc123",
            "object": "response",
            "created": 1703123456,
            "model": "gpt-4o",
            "status": "completed",
            "choices": [
              {
                "index": 0,
                "message": {
                  "role": "assistant",
                  "content": "The capital of France is Paris."
                },
                "finish_reason": "stop"
              }
            ],
            "usage": {
              "prompt_tokens": 10,
              "completion_tokens": 8,
              "total_tokens": 18
            }
          }
        }
      },
      
      "with_additional_fields": {
        "description": "Include log probabilities in response",
        "request": {
          "method": "GET",
          "url": "https://api.openai.com/v1/responses/resp_abc123?include=message.output_text.logprobs",
          "headers": {
            "Authorization": "Bearer sk-..."
          }
        },
        "response": {
          "note": "Response includes additional logprobs field",
          "body": {
            "id": "resp_abc123",
            "choices": [
              {
                "message": {
                  "content": "Hello world",
                  "logprobs": {
                    "tokens": ["Hello", " world"],
                    "token_logprobs": [-0.123, -0.456],
                    "top_logprobs": [
                      [{"token": "Hello", "logprob": -0.123}],
                      [{"token": " world", "logprob": -0.456}]
                    ]
                  }
                }
              }
            ]
          }
        }
      },
      
      "streaming_example": {
        "description": "Stream response with SSE",
        "request": {
          "method": "GET",
          "url": "https://api.openai.com/v1/responses/resp_abc123?stream=true",
          "headers": {
            "Authorization": "Bearer sk-...",
            "Accept": "text/event-stream"
          }
        },
        "response": {
          "status": 200,
          "headers": {
            "Content-Type": "text/event-stream",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
          },
          "body": [
            "event: response.start",
            "data: {\"id\":\"resp_abc123\",\"object\":\"response\",\"created\":1703123456,\"model\":\"gpt-4o\",\"sequence_number\":0}",
            "",
            "event: response.delta",
            "data: {\"delta\":{\"content\":\"The\"},\"sequence_number\":1}",
            "",
            "event: response.delta",
            "data: {\"delta\":{\"content\":\" capital\"},\"sequence_number\":2}",
            "",
            "event: response.done",
            "data: {\"usage\":{\"total_tokens\":18},\"finish_reason\":\"stop\",\"sequence_number\":5}"
          ]
        }
      },
      
      "resume_streaming": {
        "description": "Resume interrupted stream from sequence 10",
        "request": {
          "method": "GET",
          "url": "https://api.openai.com/v1/responses/resp_abc123?stream=true&starting_after=10",
          "headers": {
            "Authorization": "Bearer sk-..."
          }
        },
        "response": {
          "note": "Stream starts from sequence_number 11",
          "body": [
            "event: response.delta",
            "data: {\"delta\":{\"content\":\" of France\"},\"sequence_number\":11}",
            "",
            "event: response.done",
            "data: {\"usage\":{\"total_tokens\":18},\"finish_reason\":\"stop\",\"sequence_number\":12}"
          ]
        }
      },
      
      "background_polling": {
        "description": "Poll background response status",
        "scenario": "Response created with background=true",
        "polling_sequence": [
          {
            "attempt": 1,
            "response": {
              "status": "processing",
              "check_after": 2
            }
          },
          {
            "attempt": 2,
            "wait": "2 seconds",
            "response": {
              "status": "processing",
              "check_after": 5,
              "progress": 0.6
            }
          },
          {
            "attempt": 3,
            "wait": "5 seconds",
            "response": {
              "status": "completed",
              "choices": ["...full response..."]
            }
          }
        ]
      }
    },
    
    "implementation_guide": {
      "streaming_client": {
        "javascript": {
          "description": "EventSource implementation",
          "code": [
            "const evtSource = new EventSource(",
            "  'https://api.openai.com/v1/responses/resp_abc123?stream=true',",
            "  { headers: { 'Authorization': 'Bearer sk-...' } }",
            ");",
            "",
            "evtSource.addEventListener('response.delta', (e) => {",
            "  const data = JSON.parse(e.data);",
            "  console.log(data.delta.content);",
            "});",
            "",
            "evtSource.addEventListener('response.done', (e) => {",
            "  evtSource.close();",
            "});"
          ]
        },
        
        "python": {
          "description": "SSE client implementation",
          "code": [
            "import sseclient",
            "import requests",
            "",
            "response = requests.get(",
            "    'https://api.openai.com/v1/responses/resp_abc123',",
            "    params={'stream': 'true'},",
            "    headers={'Authorization': 'Bearer sk-...'},",
            "    stream=True",
            ")",
            "",
            "client = sseclient.SSEClient(response)",
            "for event in client.events():",
            "    if event.event == 'response.delta':",
            "        data = json.loads(event.data)",
            "        print(data['delta']['content'], end='')",
            "    elif event.event == 'response.done':",
            "        break"
          ]
        }
      },
      
      "polling_strategy": {
        "description": "Exponential backoff for background responses",
        "algorithm": [
          "1. Initial GET request to check status",
          "2. If status='processing', wait check_after seconds",
          "3. Retry with exponential backoff if check_after not provided",
          "4. Max retries: 20, Max wait: 60 seconds",
          "5. Handle timeout with appropriate error"
        ],
        "code_snippet": {
          "language": "python",
          "code": [
            "import time",
            "import requests",
            "",
            "def poll_response(response_id, max_retries=20):",
            "    url = f'https://api.openai.com/v1/responses/{response_id}'",
            "    headers = {'Authorization': 'Bearer sk-...'}",
            "    ",
            "    for attempt in range(max_retries):",
            "        response = requests.get(url, headers=headers)",
            "        data = response.json()",
            "        ",
            "        if data['status'] == 'completed':",
            "            return data",
            "        elif data['status'] == 'failed':",
            "            raise Exception(data['error'])",
            "        ",
            "        wait_time = data.get('check_after', min(2 ** attempt, 60))",
            "        time.sleep(wait_time)",
            "    ",
            "    raise TimeoutError('Response processing timeout')"
          ]
        }
      },
      
      "error_handling": {
        "retry_strategy": {
          "404": "Response may have expired; do not retry",
          "429": "Implement exponential backoff based on rate limit headers",
          "500": "Retry with exponential backoff, max 3 attempts",
          "503": "Service unavailable; retry with backoff"
        },
        
        "stream_interruption": {
          "detection": "Monitor for connection drops or timeout",
          "recovery": "Use starting_after with last received sequence_number",
          "example": [
            "let lastSequence = 0;",
            "",
            "evtSource.addEventListener('response.delta', (e) => {",
            "  const data = JSON.parse(e.data);",
            "  lastSequence = data.sequence_number;",
            "});",
            "",
            "evtSource.onerror = () => {",
            "  // Reconnect from last sequence",
            "  reconnectStream(responseId, lastSequence);",
            "};"
          ]
        }
      }
    },
    
    "performance_considerations": {
      "caching": {
        "browser": "Responses are not cached by default due to auth headers",
        "cdn": "Consider CDN caching for public, non-sensitive responses",
        "application": "Implement application-level caching with TTL"
      },
      
      "streaming_optimization": {
        "buffering": "Minimal buffering for real-time experience",
        "compression": "gzip compression applied automatically",
        "obfuscation": "Use include_obfuscation=true to normalize payload sizes"
      },
      
      "field_inclusion": {
        "strategy": "Only request fields you need to minimize payload size",
        "impact": "Can reduce response size by 50-80% for large responses"
      }
    },
    
    "best_practices": [
      {
        "category": "Polling",
        "recommendations": [
          "Always respect check_after values",
          "Implement exponential backoff",
          "Set reasonable timeout limits",
          "Handle all possible status values"
        ]
      },
      {
        "category": "Streaming",
        "recommendations": [
          "Implement reconnection logic with starting_after",
          "Handle connection timeouts gracefully",
          "Process events incrementally for better UX",
          "Monitor sequence numbers for gap detection"
        ]
      },
      {
        "category": "Security",
        "recommendations": [
          "Never expose API keys in client-side code",
          "Validate response_id format before requests",
          "Implement rate limiting on client side",
          "Use HTTPS exclusively"
        ]
      },
      {
        "category": "Error Handling",
        "recommendations": [
          "Log all errors with context",
          "Distinguish between retryable and non-retryable errors",
          "Provide user-friendly error messages",
          "Implement circuit breaker pattern for repeated failures"
        ]
      }
    ],
    
    "rate_limits": {
      "description": "GET requests share the same rate limits as POST requests",
      "typical_limits": {
        "requests_per_minute": "Tier-dependent",
        "concurrent_streams": "Limited per account",
        "polling_frequency": "Respect check_after to avoid rate limits"
      }
    }
  }
}
```

## GET

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
  model="gpt-4.1",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
```

```json
{
  "id": "resp_67ccd2bed1ec8190b14f964abc0542670bb6a6b452d3795b",
  "object": "response",
  "created_at": 1741476542,
  "status": "completed",
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-4.1-2025-04-14",
  "output": [
    {
      "type": "message",
      "id": "msg_67ccd2bf17f0819081ff3bb2cf6508e60bb6a6b452d3795b",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "In a peaceful grove beneath a silver moon, a unicorn named Lumina discovered a hidden pool that reflected the stars. As she dipped her horn into the water, the pool began to shimmer, revealing a pathway to a magical realm of endless night skies. Filled with wonder, Lumina whispered a wish for all who dream to find their own hidden magic, and as she glanced back, her hoofprints sparkled like stardust.",
          "annotations": []
        }
      ]
    }
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
    }
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 36,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 87,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 123
  },
  "user": null,
  "metadata": {}
}
```

## retrieve

```python
from openai import OpenAI
client = OpenAI()

response = client.responses.retrieve("resp_123")
print(response)
```

```json
{
  "id": "resp_67cb71b351908190a308f3859487620d06981a8637e6bc44",
  "object": "response",
  "created_at": 1741386163,
  "status": "completed",
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-4o-2024-08-06",
  "output": [
    {
      "type": "message",
      "id": "msg_67cb71b3c2b0819084d481baaaf148f206981a8637e6bc44",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "Silent circuits hum,  \nThoughts emerge in data streams—  \nDigital dawn breaks.",
          "annotations": []
        }
      ]
    }
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
    }
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 32,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 18,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 50
  },
  "user": null,
  "metadata": {}
}
```
