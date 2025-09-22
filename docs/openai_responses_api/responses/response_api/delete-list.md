{
  "module_name": "openai.responses",
  "overview": "The `openai.responses` module provides endpoints for managing model responses in the OpenAI API. This module enables you to delete responses, cancel in-progress background responses, and retrieve input items associated with responses.",
  "key_features": [
    "Delete existing model responses",
    "Cancel background responses that are still processing",
    "List and paginate through input items for a given response",
    "Support for pagination and sorting of input items"
  ],
  "functions": {
    "delete_response": {
      "description": "Deletes a model response with the specified ID. This permanently removes the response resource from the system.",
      "endpoint": "DELETE https://api.openai.com/v1/responses/{response_id}",
      "parameters": {
        "response_id": {
          "type": "string",
          "required": true,
          "description": "The unique identifier of the response to delete"
        }
      },
      "returns": {
        "type": "SuccessMessage",
        "description": "A success message confirming the response was deleted"
      },
      "example": {
        "code": "import openai\n\n# Delete a response\nresult = openai.responses.delete_response(\n    response_id=\"resp_abc123\"\n)\nprint(result)  # SuccessMessage indicating deletion",
        "description": "Delete a response by its ID"
      },
      "use_cases": [
        "Clean up completed responses that are no longer needed",
        "Remove responses to free up resources",
        "Delete test or invalid responses"
      ]
    },
    "cancel_response": {
      "description": "Cancels a model response that is currently being processed. This function only works for responses that were created with the `background` parameter set to `true`.",
      "endpoint": "POST https://api.openai.com/v1/responses/{response_id}/cancel",
      "parameters": {
        "response_id": {
          "type": "string",
          "required": true,
          "description": "The unique identifier of the response to cancel"
        }
      },
      "returns": {
        "type": "Response",
        "description": "A Response object representing the cancelled response with updated status"
      },
      "example": {
        "code": "import openai\n\n# Cancel a background response in progress\ncancelled_response = openai.responses.cancel_response(\n    response_id=\"resp_xyz789\"\n)\nprint(f\"Response status: {cancelled_response.status}\")",
        "description": "Cancel a background response that's still processing"
      },
      "important_notes": [
        "Only works for responses created with background=true",
        "Cannot cancel responses that have already completed",
        "Returns the Response object with updated cancellation status"
      ],
      "use_cases": [
        "Stop long-running background processes",
        "Cancel responses when requirements change",
        "Abort responses that are taking too long"
      ]
    },
    "list_input_items": {
      "description": "Retrieves a paginated list of input items associated with a specific response. Supports pagination for large result sets and customizable sorting order.",
      "endpoint": "GET https://api.openai.com/v1/responses/{response_id}/input_items",
      "parameters": {
        "response_id": {
          "type": "string",
          "required": true,
          "description": "The unique identifier of the response to retrieve input items for"
        },
        "after": {
          "type": "string",
          "required": false,
          "default": null,
          "description": "Cursor for pagination - an item ID to list items after"
        },
        "include": {
          "type": "array",
          "required": false,
          "default": null,
          "description": "Additional fields to include in the response (see Response creation include parameter)"
        },
        "limit": {
          "type": "integer",
          "required": false,
          "default": 20,
          "description": "Maximum number of items to return (1-100)"
        },
        "order": {
          "type": "string",
          "required": false,
          "default": "desc",
          "description": "Sort order for results - 'asc' for ascending or 'desc' for descending"
        }
      },
      "returns": {
        "type": "List[InputItem]",
        "description": "A list of input item objects associated with the response"
      },
      "pagination_example": {
        "code": "import openai\n\n# Get first page of input items\nfirst_page = openai.responses.list_input_items(\n    response_id=\"resp_123456\",\n    limit=50,\n    order=\"asc\"\n)\n\n# Get next page using cursor\nif first_page:\n    next_page = openai.responses.list_input_items(\n        response_id=\"resp_123456\",\n        after=first_page[-1].id,\n        limit=50,\n        order=\"asc\"\n    )",
        "description": "Paginate through input items using the after parameter"
      },
      "full_example": {
        "code": "import openai\n\n# List all input items with additional fields\ninput_items = openai.responses.list_input_items(\n    response_id=\"resp_123456\",\n    include=[\"metadata\", \"timestamps\"],\n    limit=25,\n    order=\"desc\"\n)\n\n# Process each input item\nfor item in input_items:\n    print(f\"Item ID: {item.id}\")\n    print(f\"Content: {item.content}\")",
        "description": "Retrieve input items with additional fields included"
      },
      "use_cases": [
        "Review input data that was processed in a response",
        "Audit or debug response generation",
        "Export input items for analysis",
        "Verify input data integrity"
      ]
    }
  },
  "common_patterns": {
    "error_handling": {
      "code": "import openai\nfrom openai import OpenAIError\n\ntry:\n    # Attempt to cancel a response\n    response = openai.responses.cancel_response(\"resp_123\")\nexcept OpenAIError as e:\n    print(f\"Error: {e}\")\n    # Handle cases where response doesn't exist or can't be cancelled",
      "description": "Proper error handling for response operations"
    },
    "batch_operations": {
      "code": "import openai\n\ndef process_response_batch(response_ids):\n    \"\"\"Process multiple responses\"\"\"\n    results = []\n    for resp_id in response_ids:\n        try:\n            # Get input items for each response\n            items = openai.responses.list_input_items(\n                response_id=resp_id,\n                limit=100\n            )\n            results.append({\n                'response_id': resp_id,\n                'item_count': len(items),\n                'items': items\n            })\n        except Exception as e:\n            results.append({\n                'response_id': resp_id,\n                'error': str(e)\n            })\n    return results",
      "description": "Processing multiple responses in batch"
    },
    "pagination_helper": {
      "code": "def get_all_input_items(response_id):\n    \"\"\"Retrieve all input items using pagination\"\"\"\n    all_items = []\n    after = None\n    \n    while True:\n        items = openai.responses.list_input_items(\n            response_id=response_id,\n            after=after,\n            limit=100\n        )\n        \n        if not items:\n            break\n            \n        all_items.extend(items)\n        after = items[-1].id\n        \n        if len(items) < 100:\n            break\n    \n    return all_items",
      "description": "Helper function to retrieve all input items with automatic pagination"
    }
  },
  "best_practices": [
    "Always handle exceptions when deleting or cancelling responses as they may no longer exist",
    "Use pagination when retrieving large sets of input items to avoid timeouts",
    "Check response status before attempting to cancel - only background responses can be cancelled",
    "Store response IDs for later reference if you need to manage responses programmatically",
    "Use the 'include' parameter efficiently to minimize data transfer when listing input items",
    "Implement retry logic for transient failures in response operations"
  ],
  "related_modules": [
    "openai.completions - For creating model responses",
    "openai.models - For model selection and configuration",
    "openai.errors - For handling API exceptions"
  ]
}

```python
from openai import OpenAI
client = OpenAI()

response = client.responses.delete("resp_123")
print(response)
```

```json
{
  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
}
```

```python
from openai import OpenAI
client = OpenAI()

response = client.responses.cancel("resp_123")
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

```python
from openai import OpenAI
client = OpenAI()

response = client.responses.input_items.list("resp_123")
print(response.data)
```

```json
{
  "object": "list",
  "data": [
    {
      "id": "msg_abc123",
      "type": "message",
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "Tell me a three sentence bedtime story about a unicorn."
        }
      ]
    }
  ],
  "first_id": "msg_abc123",
  "last_id": "msg_abc123",
  "has_more": false
}
```
