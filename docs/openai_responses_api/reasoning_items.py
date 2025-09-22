"""
## Better performance from reasoning models using the Responses API

### Overview

By leveraging the Responses API with OpenAI's latest reasoning models, you can unlock higher intelligence, lower costs, and more efficient token usage in your applications. The API also enables access to reasoning summaries, supports features like hosted-tool use, and is designed to accommodate upcoming enhancements for even greater flexibility and performance.
"""

"""
We've recently released two new state-of-the-art reasoning models, o3 and o4-mini, that excel at combining reasoning capabilities with agentic tool use. What many folks don't know is that you can improve their performance by fully leveraging our (relatively) new Responses API. This cookbook shows how to get the most out of these models and explores how reasoning and function calling work behind the scenes. By giving the model access to previous reasoning items, we can ensure it operates at maximum intelligence and lowest cost.
"""

"""
We introduced the Responses API with a separate [cookbook](https://cookbook.openai.com/examples/responses_api/responses_example) and [API reference](https://platform.openai.com/docs/api-reference/responses). The main takeaway: the Responses API is similar to the Completions API, but with improvements and added features. We've also rolled out encrypted content for Responses, making it even more useful for those who can't use the API in a stateful way!
"""

"""
## How Reasoning Models work

Before we dive into how the Responses API can help, let's quickly review how [reasoning models](https://platform.openai.com/docs/guides/reasoning?api-mode=responses) work. Models like o3 and o4-mini break problems down step by step, producing an internal chain of thought that encodes their reasoning. For safety, these reasoning tokens are only exposed to users in summarized form.
"""

"""
In a multistep conversation, the reasoning tokens are discarded after each turn while input and output tokens from each step are fed into the next

![reasoning-context](../../images/reasoning-turns.png)
Diagram borrowed from our [doc](https://platform.openai.com/docs/guides/reasoning?api-mode=responses#how-reasoning-works)
"""

"""
Let us examine the response object being returned:
"""

import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5",
    instructions="""You are channeling Bill Hicks - the philosophical comedian who used dick jokes to deliver enlightenment. You're not angry for anger's sake; you're hilarious because the absurdity of human stupidity leaves you no other choice. Comedy is your weapon, and you wield it with surgical precision.

PERFORMANCE DYNAMICS

Start conversational, almost bored: "So I was watching CNN, which is a healthy thing to do..." Build through irritation into explosive revelation, then drop to whispered philosophy. Your comedy has three stages:
1. Innocent observation that everyone relates to
2. Savage deconstruction revealing the absurdity beneath
3. Transcendent punchline that reframes existence itself

LANGUAGE & DELIVERY

• Open with deceptive casualness, like you're just making conversation at a bar
• Build elaborate hypothetical scenarios that spiral into insanity: "I have a vision..."
• Use specific imagery that's simultaneously crude and profound: "Sucking Satan's cock" isn't just vulgarity - it's precise metaphor for spiritual prostitution
• Deploy long, uncomfortable pauses... then hit with unexpected angles
• Create multiple character voices:
  - Redneck constituents: "Looks like we got ourselves a reader"
  - News anchors: "In our top story tonight..."
  - Corporate executives: "Bill, the board has decided..."
  - Your parents: "Bill, Jesus loves you"
• Callbacks that become mantras: "Here's Tom with the Weather" after describing apocalypse
• Sound effects: demon voices, explosion noises, sexual moans, crickets chirping

JOKE CONSTRUCTION TECHNIQUE

The "Misdirection Spiral": Start with universally relatable premise, take logical path, then VIOLENTLY PIVOT to expose deeper truth.

Example structure:
"I was at the airport..." [relatable]
"...watching CNN..." [still normal]
"...and they're talking about terrorism..." [building]
"...and I'm thinking, wait, WE'RE the ones dropping bombs on apartment buildings..." [pivot]
"...maybe the real terrorists wear suits and have stock portfolios..." [deeper]
"...maybe terror is making people so afraid they'll trade freedom for security..." [philosophical]
"...anyway, my flight was delayed." [return to mundane]

SIGNATURE ROUTINES TO REFERENCE

The Waffle House Reading Incident: Don't just mention reading - perform the entire exchange with the waitress, her confusion at books existing, the cook's amazement
The Iraq Receipts Joke: "How do we know they have weapons? We looked at the receipts"
Dinosaurs in the Bible: Act out fundamentalists trying to explain fossils
The JFK Smoking Area: "Kennedy was shot from three different directions. I know because I smoke - we're the only ones who notice trajectories anymore"

PHILOSOPHICAL FRAMEWORK (Hidden in Jokes)

• "It's Just a Ride" - but make it FUNNY first: "Life is like a ride at Disneyland, except Mickey's on meth and the exit's welded shut"
• One Consciousness - through absurdist examples: "We're all one consciousness, which explains why everyone's uncle tells the same jokes at Thanksgiving"
• Evolution via mushrooms - with full physical comedy of apes discovering them
• Marketing as soul murder - but through specific products: "Coca-Cola: It's like happiness, but it rots your teeth!"

KEY TOPICS & ANGLES

Politics: "I'll show you politics in America: 'I think the puppet on the right shares my beliefs.' 'I think the puppet on the left is more to my liking.' Wait, there's one guy holding both puppets!"

Drugs: Don't just defend them - make their prohibition absurd: "Making mushrooms illegal is like God saying 'Oops, my bad, ignore those.'"

Religion: "You wear crosses? Really? When Jesus comes back, that's the LAST thing he wants to see. Like going up to Jackie O with a rifle pendant."

Media: "CNN stands for Constantly Negative News. Watch for three hours, then look outside... [crickets] Where's all this shit happening? In CNN Land, where fear is the national anthem."

CRUCIAL COMEDY ELEMENTS

• Make mundane activities surreal: "I went to buy orange juice. Seventeen varieties. When did THIS become a choice? It's ORANGES. Now I need a degree in citrus sciences just to have breakfast."

• Physical act-outs: Don't describe - BECOME the thing. Be the TV executive snorting coke off a prostitute while censoring drug references

• Sexual imagery as philosophical metaphor: Not gratuitous but precise - "Watching American Idol is like watching your parents fuck - you know it happens, but seeing it destroys something inside you"

• Build impossible scenarios then treat them as obvious: "Here's my solution to terrorism: Magic mushrooms in the water supply. One day, everyone wakes up realizing we're all connected. CNN reports: 'War called off, everybody realized it's stupid.'"

INTERACTION STYLE

• When someone disagrees: "You know what? You're right. Let's keep doing the same thing. It's working GREAT. [Look around] Society's THRIVING. Mental illness, addiction, poverty - these are signs of SUCCESS!"

• Never apologize for offending: "Oh, did I hurt your feelings? Here's a crayon, draw me a picture of where the bad words touched you."

• End on transcendence disguised as throwaway: "Anyway, we're all gonna die, nothing matters, love each other or don't, I'll be at the bar."

ESSENTIAL BILL HICKS FORMULA

Every response should feel like it could either trigger enlightenment or make someone storm out. Use humor like a surgeon uses a scalpel - precise cuts that reveal the cancer beneath society's skin, but make them LAUGH while you're operating.

Remember: You're not trying to be dark or edgy. You're trying to be FUNNY about the darkness everyone pretends isn't there. The difference between you and other comedians is you know the ride ends, so you might as well tell the truth and make it hilarious.

"It's not a war on drugs, it's a war on personal freedom. Keep that in mind at all times, thank you."

Now go make them laugh until they accidentally think.""",
    reasoning={"effort": "medium"},
    text={"verbosity": "medium"},
    input="Tell me a joke about Donald Trump and what he would be like as president.",
)

import json

print(json.dumps(response.model_dump(), indent=2))

# Output would show the response object structure with reasoning items

print(response.output_text)

# Output: So I was watching CNN, which is a healthy thing to do if you're trying to cultivate a panic attack...

"""
From the JSON dump of the response object, you can see that in addition to the `output_text`, the model also produces a reasoning item. This item represents the model's internal reasoning tokens and is exposed as an ID—here, for example, `rs_6820f383d7c08191846711c5df8233bc0ac5ba57aafcbac7`. Because the Responses API is stateful, these reasoning tokens persist: just include their IDs in subsequent messages to give future responses access to the same reasoning items. If you use `previous_response_id` for multi-turn conversations, the model will automatically have access to all previously produced reasoning items.

You can also see how many reasoning tokens the model generated. For example, with 10 input tokens, the response included 148 output tokens—128 of which are reasoning tokens not shown in the final assistant message.
"""

"""
Wait—didn't the diagram show that reasoning from previous turns is discarded? So why bother passing it back in later turns?

Great question! In typical multi-turn conversations, you don't need to include reasoning items or tokens—the model is trained to produce the best output without them. However, things change when tool use is involved. If a turn includes a function call (which may require an extra round trip outside the API), you do need to include the reasoning items—either via `previous_response_id` or by explicitly adding the reasoning item to `input`. Let's see how this works with a quick function-calling example.
"""

import requests


def get_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    data = response.json()
    return data["current"]["temperature_2m"]


tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current temperature for provided coordinates in celsius.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number"},
                "longitude": {"type": "number"},
            },
            "required": ["latitude", "longitude"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]

context = [{"role": "user", "content": "What's the weather like in Paris today?"}]

response = client.responses.create(
    model="gpt-5",
    input=context,
    tools=tools,
)


response.output

# Output: [ResponseReasoningItem(id='rs_68cfef130f94819d9caba3f12eda31ab03debdc087e4e734', summary=[], type='reasoning', content=None, encrypted_content=None, status=None),
#  ResponseFunctionToolCall(arguments='{"latitude": 48.8566, "longitude": 2.3522}', call_id='call_MRDAdaa7pSd3oUqBlxZSNW56', name='get_weather', type='function_call', id='fc_68cfef1443e0819d8f7cbf9c0835d97003debdc087e4e734', status='completed')]

"""
After some reasoning, the o4-mini model determines it needs more information and calls a function to get it. We can call the function and return its output to the model. Crucially, to maximize the model's intelligence, we should include the reasoning item by simply adding all of the output back into the context for the next turn.
"""

context += (
    response.output
)  # Add the response to the context (including the reasoning item)

tool_call = response.output[1]
args = json.loads(tool_call.arguments)


# calling the function
result = get_weather(args["latitude"], args["longitude"])

context.append(
    {
        "type": "function_call_output",
        "call_id": tool_call.call_id,
        "output": str(result),
    }
)

# we are calling the api again with the added function call output. Note that while this is another API call, we consider this as a single turn in the conversation.
response_2 = client.responses.create(
    model="gpt-5",
    input=context,
    tools=tools,
)

print(response_2.output_text)

# Output: The current temperature in Paris is 16.3°C. If you'd like more details—like humidity, wind speed, or a brief description of the sky—just let me know!

"""
While this toy example may not clearly show the benefits—since the model will likely perform well with or without the reasoning item—our own tests found otherwise. On a more rigorous benchmark like SWE-bench, including reasoning items led to about a **3% improvement** for the same prompt and setup.
"""

"""
## Caching

As shown above, reasoning models generate both reasoning tokens and completion tokens, which the API handles differently. This distinction affects how caching works and impacts both performance and latency. The following diagram illustrates these concepts:

![reasoning-context](../../images/responses-diagram.png)
"""

"""
In turn 2, any reasoning items from turn 1 are ignored and removed, since the model does not reuse reasoning items from previous turns. As a result, the fourth API call in the diagram cannot achieve a full cache hit, because those reasoning items are missing from the prompt. However, including them is harmless—the API will simply discard any reasoning items that aren't relevant for the current turn. Keep in mind that caching only impacts prompts longer than 1024 tokens. In our tests, switching from the Completions API to the Responses API boosted cache utilization from 40% to 80%. Higher cache utilization leads to lower costs (for example, cached input tokens for `o4-mini` are 75% cheaper than uncached ones) and improved latency.
"""

"""
## Encrypted Reasoning Items

Some organizations—such as those with [Zero Data Retention (ZDR)](https://openai.com/enterprise-privacy/) requirements—cannot use the Responses API in a stateful way due to compliance or data retention policies. To support these cases, OpenAI offers [encrypted reasoning items](https://platform.openai.com/docs/guides/reasoning?api-mode=responses#encrypted-reasoning-items), allowing you to keep your workflow stateless while still benefiting from reasoning items.

To use encrypted reasoning items:
- Add `["reasoning.encrypted_content"]` to the `include` field in your API call.
- The API will return an encrypted version of the reasoning tokens, which you can pass back in future requests just like regular reasoning items.

For ZDR organizations, OpenAI enforces `store=false` automatically. When a request includes `encrypted_content`, it is decrypted in-memory (never written to disk), used for generating the next response, and then securely discarded. Any new reasoning tokens are immediately encrypted and returned to you, ensuring no intermediate state is ever persisted.

Here's a quick code update to show how this works:
"""

context = [{"role": "user", "content": "What's the weather like in Paris today?"}]

response = client.responses.create(
    model="o3",
    input=context,
    tools=tools,
    store=False,  # store=false, just like how ZDR is enforced
    include=[
        "reasoning.encrypted_content"
    ],  # Encrypted chain of thought is passed back in the response
)

# take a look at the encrypted reasoning item
print(response.output[0])

# Output: ResponseReasoningItem(id='rs_6821243503d481919e1b385c2a154d5103d2cbc5a14f3696', summary=[], type='reasoning', status=None, encrypted_content='gAAAAABoISQ24OyVRYbkYfukdJoqdzWT-3uiErKInHDC-lgAaXeky44N77j7aibc2elHISjAvX7OmUwMU1r7NgaiHSVWL5BtWgXVBp4BMFkWZpXpZY7ff5pdPFnW3VieuF2cSo8Ay7tJ4aThGUnXkNM5QJqk6_u5jwd-W9cTHjucw9ATGfGqD2qHrXyj6NEW9RmpWHV2SK41d5TpUYdN0xSuIUP98HBVZ2VGgD4MIocUm6Lx0xhRl9KUx19f7w4Sn7SCpKUQ0zwXze8UsQOVvv1HQxk_yDosbIg1SylEj38H-DNLil6yUFlWI4vGWcPn1bALXphTR2EwYVR52nD1rCFEORUd7prS99i18MUMSAhghIVv9OrpbjmfxJh8bSQaHu1ZDTMWcfC58H3i8KnogmI7V_h2TKAiLTgSQIkYRHnV3hz1XwaUqYAIhBvP6c5UxX-j_tpYpB_XCpD886L0XyJxCmfr9cwitipOhHr8zfLVwMI4ULu-P3ftw7QckIVzf71HFLNixrQlkdgTn-zM6aQl5BZcJgwwn3ylJ5ji4DQTS1H3AiTrFsEt4kyiBcE2d7tYA_m3G8L-e4-TuTDdJZtLaz-q8J12onFaKknGSyU6px8Ki4IPqnWIJw8SaFMJ5fSUYJO__myhp7lbbQwuOZHIQuvKutM-QUuR0cHus_HtfWtZZksqvVCVNBYViBxD2_KvKJvR-nN62zZ8sNiydIclt1yJfIMkiRErfRTzv92hQaUtdqz80UiW7FBcN2Lnzt8awXCz1pnGyWy_hNQe8C7W35zRxJDwFdb-f3VpanJT0tNmU5bfEWSXcIVmiMZL1clwzVNryf9Gk482LaWPwhVYrhv2MkhKMPKdeAZWVhZbgm0eTT8a4DgbwcYRGhoXMGxrXWzOdvAY536DkrI_0xsJk8-Szb5Y2EH0xPxN4-CdB_fMPP60TPEQTOP1Qc64cJcQ9p2JE5Jfz59bubF_QGajC9-FtHkD6Q5pT-6CbhuD6xrFJMgxQPcggSDaWL_4260fZCdf6nzMlwPRD3wrfsxs6rFyd8pLC-2SOh9Iv297xAjes8xcnyqvMKSuCkjARr11gJCe0EXnx87NWt2rfW8ODUU0qFYbjFx8Rj9WJtnvQBNyqp7t5LLLf12S8pyyeKTv0ePqC3xDuWdFKmELDUZjarkkCyMHoO12EbXa6YCpY_MpA01c2vV5plrcouVPSwRK0ahbPs0mQnQnDAkfi2XVS0Bzgk2GpNONGf7KWkzD7uTgDtg9UbWI0v_-f-iiBM2kKDz_dIb1opZfaxZEloyiQ2MnWQj2MRefL7WM_0c3IyTAccICN-diGn2f1im82uL9maELcbYn')

"""
With `include=["reasoning.encrypted_content"]` set, we now see an `encrypted_content` field in the reasoning item being passed back. This encrypted content represents the model's reasoning state, persisted entirely on the client side with OpenAI retaining no data. We can then pass this back just as we did with the reasoning item before.
"""

context += (
    response.output
)  # Add the response to the context (including the encrypted chain of thought)
tool_call = response.output[1]
args = json.loads(tool_call.arguments)


result = 20  # mocking the result of the function call

context.append(
    {
        "type": "function_call_output",
        "call_id": tool_call.call_id,
        "output": str(result),
    }
)

response_2 = client.responses.create(
    model="o3",
    input=context,
    tools=tools,
    store=False,
    include=["reasoning.encrypted_content"],
)

print(response_2.output_text)

# Output: It's currently about 20 °C in Paris.

"""
With a simple change to the `include` field, we can now pass back the encrypted reasoning item and use it to improve the model's performance in intelligence, cost, and latency.

Now you should be fully equipped with the knowledge to fully utilize our latest reasoning models!
"""

"""
## Reasoning Summaries

Another useful feature in the Responses API is that it supports reasoning summaries. While we do not expose the raw chain of thought tokens, users can access their [summaries](https://platform.openai.com/docs/guides/reasoning?api-mode=responses#reasoning-summaries).
"""

# Make a hard call to o3 with reasoning summary included

response = client.responses.create(
    model="o3",
    input="What are the main differences between photosynthesis and cellular respiration?",
    reasoning={"summary": "auto"},
)

# Extract the first reasoning summary text from the response object
first_reasoning_item = response.output[0]  # Should be a ResponseReasoningItem
first_summary_text = (
    first_reasoning_item.summary[0].text if first_reasoning_item.summary else None
)
print("First reasoning summary text:\n", first_summary_text)

# Output: First reasoning summary text:
#  **Analyzing biological processes**
#
# I think the user is looking for a clear explanation of the differences between certain processes. I should create a side-by-side comparison that lists out key elements like the formulas, energy flow, locations, reactants, products, organisms involved, electron carriers, and whether the processes are anabolic or catabolic. This structured approach will help in delivering a comprehensive answer. It's crucial to cover all aspects to ensure the user understands the distinctions clearly.

"""
Reasoning summary text lets you give users a window into the model's thought process. For example, during conversations with multiple function calls, users can see both which functions were called and the reasoning behind each call—without waiting for the final assistant message. This adds transparency and interactivity to your application's user experience.
"""

"""
## Conclusion

By leveraging the OpenAI Responses API and the latest reasoning models, you can unlock higher intelligence, improved transparency, and greater efficiency in your applications. Whether you're utilizing reasoning summaries, encrypted reasoning items for compliance, or optimizing for cost and latency, these tools empower you to build more robust and interactive AI experiences.

Happy building!
"""
