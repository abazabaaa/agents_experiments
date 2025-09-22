"""
## What is the Responses API?

The Responses API is a new way to interact with OpenAI models, designed to be simpler and more flexible than previous APIs. It makes it easy to build advanced AI applications that use multiple tools, handle multi-turn conversations, and work with different types of data (not just text).

Unlike older APIs—such as Chat Completions, which were built mainly for text, or the Assistants API, which can require a lot of setup—the Responses API is built from the ground up for:

- Seamless multi-turn interactions (carry on a conversation across several steps in a single API call)
- Easy access to powerful hosted tools (like file search, web search, and code interpreter)
- Fine-grained control over the context you send to the model

As AI models become more capable of complex, long-running reasoning, developers need an API that is both asynchronous and stateful. The Responses API is designed to meet these needs.

In this guide, you'll see some of the new features the Responses API offers, along with practical examples to help you get started.
"""

"""
## Basics
By design, on the surface, the Responses API is very similar to the Completions API.
"""

import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4o-mini",
    input="tell me a joke",
)

print(response.output[0].content[0].text)

# Output: Why did the scarecrow win an award?
#
# Because he was outstanding in his field!

"""
One key feature of the Response API is that it is stateful. This means that you do not have to manage the state of the conversation by yourself, the API will handle it for you. For example, you can retrieve the response at any time and it will include the full conversation history.
"""

fetched_response = client.responses.retrieve(response_id=response.id)

print(fetched_response.output[0].content[0].text)

# Output: Why did the scarecrow win an award?
#
# Because he was outstanding in his field!

"""
You can continue the conversation by referring to the previous response.
"""

response_two = client.responses.create(
    model="gpt-4o-mini", input="tell me another", previous_response_id=response.id
)

print(response_two.output[0].content[0].text)

# Output: Why don't skeletons fight each other?
#
# They don't have the guts!

"""
You can of course manage the context yourself. But one benefit of OpenAI maintaining the context for you is that you can fork the response at any point and continue the conversation from that point.
"""

response_two_forked = client.responses.create(
    model="gpt-4o-mini",
    input="I didn't like that joke, tell me another and tell me the difference between the two jokes",
    previous_response_id=response.id,  # Forking and continuing from the first response
)

output_text = response_two_forked.output[0].content[0].text
print(output_text)

# Output: Sure! Here's another joke:
#
# Why don't scientists trust atoms?
#
# Because they make up everything!
#
# **Difference:** The first joke plays on a pun involving "outstanding" in a literal sense versus being exceptional, while the second joke relies on a play on words about atoms "making up" matter versus fabricating stories. Each joke uses wordplay, but they target different concepts (farming vs. science).

"""
## Hosted Tools

Another benefit of the Responses API is that it adds support for hosted tools like `file_search` and `web_search`. Instead of manually calling the tools, simply pass in the tools and the API will decide which tool to use and use it.

Here is an example of using the `web_search` tool to incorporate web search results into the response.
"""

response = client.responses.create(
    model="gpt-4o",  # or another supported model
    input="What's the latest news about AI?",
    tools=[{"type": "web_search"}],
)

import json

print(json.dumps(response.output, default=lambda o: o.__dict__, indent=2))

# Output:
# [
#   {
#     "id": "ws_67bd64fe91f081919bec069ad65797f1",
#     "status": "completed",
#     "type": "web_search_call"
#   },
#   {
#     "id": "msg_67bd6502568c8191a2cbb154fa3fbf4c",
#     "content": [
#       {
#         "annotations": [
#           {
#             "index": null,
#             "title": "Huawei improves AI chip production in boost for China's tech goals",
#             "type": "url_citation",
#             "url": "https://www.ft.com/content/f46b7f6d-62ed-4b64-8ad7-2417e5ab34f6?utm_source=chatgpt.com"
#           },
#           ...additional citations...
#         ],
#         "text": "As of February 25, 2025, several significant developments have emerged in the field of artificial intelligence (AI):...",
#         "type": "output_text",
#         "logprobs": null
#       }
#     ],
#     "role": "assistant",
#     "type": "message"
#   }
# ]

"""
## Multimodal, Tool-augmented conversation

The Responses API natively supports text, images, and audio modalities.
Tying everything together, we can build a fully multimodal, tool-augmented interaction with one API call through the responses API.
"""


from IPython.display import Image, display

# Display the image from the provided URL
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/2880px-Cat_August_2010-4.jpg"
display(Image(url=url, width=400))

response_multimodal = client.responses.create(
    model="gpt-4o",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Come up with keywords related to the image, and search on the web using the search tool for any news related to the keywords"
                    ", summarize the findings and cite the sources.",
                },
                {
                    "type": "input_image",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/2880px-Cat_August_2010-4.jpg",
                },
            ],
        }
    ],
    tools=[{"type": "web_search"}],
)

# Output: <IPython.core.display.Image object>

import json

print(json.dumps(response_multimodal.__dict__, default=lambda o: o.__dict__, indent=4))

# Output:
# {
#     "id": "resp_67bd65392a088191a3b802a61f4fba14",
#     "created_at": 1740465465.0,
#     "error": null,
#     "metadata": {},
#     "model": "gpt-4o-2024-08-06",
#     "object": "response",
#     "output": [
#         {
#             "id": "msg_67bd653ab9cc81918db973f0c1af9fbb",
#             "content": [
#                 {
#                     "annotations": [],
#                     "text": "Based on the image of a cat, some relevant keywords could be:\n\n- Cat\n- Feline\n- Pet\n- Animal care\n- Cat behavior\n\nI'll search for recent news related to these keywords.",
#                     "type": "output_text",
#                     "logprobs": null
#                 }
#             ],
#             "role": "assistant",
#             "type": "message"
#         },
#         {
#             "id": "ws_67bd653c7a548191af86757fbbca96e1",
#             "status": "completed",
#             "type": "web_search_call"
#         },
#         {
#             "id": "msg_67bd653f34fc8191989241b2659fd1b5",
#             "content": [
#                 {
#                     "annotations": [
#                         {
#                             "index": null,
#                             "title": "Cat miraculously survives 3 weeks trapped in sofa during family's cross-country move",
#                             "type": "url_citation",
#                             "url": "https://nypost.com/2025/02/24/us-news/cat-miraculously-survives-3-weeks-trapped-in-sofa-during-familys-cross-country-move/?utm_source=chatgpt.com"
#                         },
#                         ...additional citations...
#                     ],
#                     "text": "Here are some recent news stories related to cats:...",
#                     "type": "output_text",
#                     "logprobs": null
#                 }
#             ],
#             "role": "assistant",
#             "type": "message"
#         }
#     ],
#     ...additional fields...
# }

"""
In the above example, we were able to use the `web_search` tool to search the web for news related to the image in one API call instead of multiple round trips that would be required if we were using the Chat Completions API.
"""

"""
With the responses API
🔥 a single API call can handle:

✅ Analyze a given image using a multimodal input.

✅ Perform web search via the `web_search` hosted tool

✅ Summarize the results.

In contrast, With Chat Completions API would require multiple steps, each requiring a round trip to the API:

1️⃣ Upload image and get analysis → 1 request

2️⃣ Extract info, call external web search → manual step + tool execution

3️⃣ Re-submit tool results for summarization → another request

See the following diagram for a side by side visualized comparison!

![Responses vs Completions](../../images/comparisons.png)


We are very excited for you to try out the Responses API and see how it can simplify your code and make it easier to build complex, multimodal, tool-augmented interactions!
"""
