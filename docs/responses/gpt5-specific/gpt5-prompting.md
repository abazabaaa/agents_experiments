
# GPT‑5 Prompting Guide

*Version: 2025‑08‑29*  

---

## Overview

GPT‑5 delivers **significant improvements** in agentic task performance, coding, raw intelligence, and steerability. This guide provides practical prompting tips to extract the best possible outputs, covering:

- Agentic workflow predictability  
- Controlling model eagerness  
- Tool‑calling preambles  
- Reasoning effort & the Responses API  
- Maximizing coding performance (frontend & backend)  
- Steering, verbosity, and instruction‑following  
- Minimal reasoning & markdown formatting  
- Metaprompting  
- Appendices (developer instructions, tool definitions, test prompts)

---

## Agentic Workflow Predictability

We trained GPT‑5 with developers in mind, emphasizing **tool calling, instruction following,** and **long‑context understanding**. For agentic and tool‑calling flows, we recommend the **Responses API**: it persists reasoning across tool calls, reduces token usage, and improves latency.

### Controlling Agentic Eagerness

GPT‑5 can operate anywhere on the spectrum from highly proactive to tightly constrained. Adjust its behavior with the following patterns.

#### Prompting for Less Eagerness

- **Lower `reasoning_effort`** (e.g., `low` or `medium`).
- Provide explicit context‑gathering criteria:

```xml
<context_gathering>
Goal: Get enough context fast. Parallelize discovery and stop as soon as you can act.
Method:
- Start broad, then fan out to focused subqueries.
- In parallel, launch varied queries; read top hits per query.
- Deduplicate paths and cache; don’t repeat queries.
- Avoid over‑searching. If needed, run targeted searches in one parallel batch.
Early stop criteria:
- You can name exact content to change.
- Top hits converge (~70%) on one area/path.
Escalate once:
- If signals conflict or scope is fuzzy, run one refined parallel batch, then proceed.
Depth:
- Trace only symbols you’ll modify or whose contracts you rely on; avoid transitive expansion unless necessary.
Loop:
- Batch search → minimal plan → complete task.
- Search again only if validation fails or new unknowns appear. Prefer acting over more searching.
</context_gathering>
```

- **Budgeted tool calls** (e.g., max 2 calls):

```xml
<context_gathering>
- Search depth: very low
- Bias strongly toward providing a correct answer quickly, even if not fully correct.
- Usually, an absolute maximum of 2 tool calls.
- If more time is needed, update the user with findings and open questions; proceed only after confirmation.
</context_gathering>
```

- Add an **escape hatch** clause such as “even if it might not be fully correct”.

#### Prompting for More Eagerness

- Increase `reasoning_effort`.
- Use a persistence directive:

```xml
<persistence>
You are an agent – keep going until the user's query is completely resolved before ending your turn.
Only terminate when you are sure the problem is solved.
Never stop or hand back to the user when you encounter uncertainty – research or deduce a reasonable approach and continue.
Do not ask the human to confirm assumptions; decide, proceed, and document for the user after you finish acting.
</persistence>
```

- Define **stop conditions** per tool (e.g., lower uncertainty for checkout, higher for search).

### Tool Preambles

Tool preambles improve transparency. Control their frequency and detail with a prompt such as:

```xml
<tool_preambles>
- Rephrase the user's goal clearly before any tool call.
- Outline a structured plan of logical steps.
- Narrate each file edit succinctly, marking progress.
- Summarize completed work distinct from the upfront plan.
</tool_preambles>
```

**Example preamble output** (truncated for brevity):

```json
{
  "id": "rs_6888f6d0606c819aa8205ecee386963f0e683233d39188e7",
  "type": "reasoning",
  "summary": [
    {
      "type": "summary_text",
      "text": "**Determining weather response**\n\nI need to answer the user's question about the weather in San Francisco..."
    }
  ]
},
{
  "id": "msg_6888f6d83acc819a978b51e772f0a5f40e683233d39188e7",
  "type": "message",
  "status": "completed",
  "content": [
    {
      "type": "output_text",
      "text": "I’m going to check a live weather service..."
    }
  ],
  "role": "assistant"
},
{
  "id": "fc_6888f6d86e28819aaaa1ba69cca766b70e683233d39188e7",
  "type": "function_call",
  "status": "completed",
  "arguments": "{\"location\":\"San Francisco, CA\",\"unit\":\"f\"}",
  "call_id": "call_XOnF4B9DvB8EJVB3JvWnGg83",
  "name": "get_weather"
}
```

### Reasoning Effort

- **`reasoning_effort` values:** `minimal`, `low`, `medium` (default), `high`.
- Use higher effort for complex, multi‑step tasks; lower effort for latency‑sensitive workflows.
- Break separable tasks into distinct agent turns to keep reasoning traces manageable.

### Reusing Reasoning Context with the Responses API

- Include `previous_response_id` to pass prior reasoning items.
- Benefits observed: **+4.3 %** in Tau‑Bench Retail scores, reduced token usage, and lower latency.

---

## Maximizing Coding Performance

GPT‑5 excels at both **large‑scale refactors** and **zero‑to‑one** app generation.

### Frontend App Development

**Recommended stack (TypeScript ecosystem):**

| Category | Recommended Choices |
|----------|----------------------|
| Frameworks | Next.js, React, HTML |
| Styling / UI | Tailwind CSS, shadcn/ui, Radix Themes |
| Icons | Material Symbols, Heroicons, Lucide |
| Animation | Motion |
| Fonts | Inter, Geist, Mona Sans, IBM Plex Sans, Manrope |

#### Zero‑to‑One App Generation

Use a self‑reflection rubric to guide quality:

```xml
<self_reflection>
- First, spend time designing a rubric (5‑7 categories) for a world‑class web app. Keep it internal.
- Then, iterate on the solution, constantly checking against the rubric.
- If the answer fails any rubric category, restart the process.
</self_reflection>
```

#### Matching Existing Codebase Standards

Provide a concise set of **code‑editing rules**:

```xml
<code_editing_rules>
<guiding_principles>
- Clarity & Reuse
- Consistency (design system, tokens)
- Simplicity
- Demo‑Orientation
- Visual Quality
</guiding_principles>

<frontend_stack_defaults>
Framework: Next.js (TS)
Styling: TailwindCSS
UI: shadcn/ui
Icons: Lucide
State: Zustand
Directory Structure:
```

/src
  /app
    /api/<route>/route.ts
  /pages
  /components
  /hooks
  /lib
  /stores
  /types
  /styles

```
</frontend_stack_defaults>

<ui_ux_best_practices>
- Limit typography to 4–5 sizes.
- Use a neutral base color + up to 2 accents.
- Spacing multiples of 4.
- Skeletons / `animate-pulse` for loading.
- Accessibility via semantic HTML & ARIA.
</ui_ux_best_practices>
</code_editing_rules>
```

### Cursor’s GPT‑5 Prompt Tuning (Case Study)

- **Verbosity control:** Global low verbosity, but high verbosity for code‑tool outputs.
- **Autonomy boost:** Explicitly allow proactive code edits; rely on undo/reject UI for safety.
- **Reduced over‑search:** Softened “be thorough” language to prevent unnecessary tool calls.
- **Structured XML specs:** `<context_understanding>` tags improve instruction adherence.

---

## Optimizing Intelligence & Instruction‑Following

### Steering

- **Verbosity parameter:** Controls final answer length (independent of `reasoning_effort`).
- **Natural‑language overrides** for context‑specific verbosity (e.g., “be verbose only when writing code”).

### Instruction Following

- Avoid contradictory or vague directions; resolve hierarchy before deployment.
- Example of a conflict (appointment scheduling) and its resolution provided in the guide.

### Minimal Reasoning

- Best for latency‑critical use‑cases.
- Tips:
  1. Start with a concise thought‑summary bullet list.
  2. Use detailed tool‑calling preambles.
  3. Disambiguate tool instructions.
  4. Provide extensive planning prompts (see “planning snippet” below).

**Planning snippet example:**

```text
Remember, you are an agent – keep going until the user's query is completely resolved before ending your turn. Decompose the query into all required sub‑requests, and confirm each is completed. Do not stop after completing only part of the request. Only terminate when you are sure the problem is solved. Plan extensively before making function calls, and reflect on each outcome to ensure full resolution.
```

### Markdown Formatting

- GPT‑5 does **not** output Markdown by default. Use a prompt like:

```text
- Use Markdown **only where semantically correct** (inline code, code fences, lists, tables).
- In assistant messages, backtick file, directory, function, and class names.
- Use `\( … \)` for inline math and `\[ … \]` for block math.
```

- Re‑insert the instruction every 3–5 user messages if consistency degrades.

### Metaprompting

Leverage GPT‑5 to improve its own prompts:

```text
When asked to optimize prompts, give answers from your own perspective – explain what specific phrases could be added to, or deleted from, this prompt to more consistently elicit the desired behavior or prevent the undesired behavior.
Here's a prompt: [PROMPT]
The desired behavior is [...] but instead it [...]
While keeping the existing prompt as intact as possible, suggest minimal edits/additions.
```

---

## Appendix

### SWE‑Bench Verified Developer Instructions

```text
In this environment, you can run `bash -lc <apply_patch_command>` to execute a diff/patch against a file.
A valid <apply_patch_command> looks like:
apply_patch << 'PATCH'
*** Begin Patch
[YOUR_PATCH]
*** End Patch
PATCH
Always verify changes thoroughly; hidden tests may exist. Make as many tool calls as needed, but ensure 100 % correctness before ending.
```

### Agentic Coding Tool Definitions

```text
## Set 1: 4 functions, no terminal
apply_patch = (_: {patch: string}) => any;
read_file = (_: {path: string, line_start?: number, line_end?: number}) => any;
list_files = (_: {path?: string, depth?: number}) => any;
find_matches = (_: {query: string, path?: string, max_results?: number}) => any;

## Set 2: 2 functions, terminal‑native
run = (_: {command: string[], session_id?: string, working_dir?: string, ms_timeout?: number, environment?: object, run_as_user?: string}) => any;
send_input = (_: {session_id: string, text: string, wait_ms?: number}) => any;
```

### Taubench‑Retail Minimal Reasoning Instructions

*(Condensed – full version in the guide)*

- Authenticate the user first (email or name + ZIP).  
- Only act on the authenticated user.  
- Obtain explicit confirmation before any state‑changing action.  
- Use a single tool call per turn; never mix a response with a tool call.  
- Transfer to a human only when the request is out of scope.

### Terminal‑Bench Prompt (Full)

```text
Please resolve the user's task by editing and testing the code files in your current code execution session.
You are a deployed coding agent. Your session is backed by a container designed for you to modify and run code.
...
(Full prompt omitted for brevity – see original guide for complete specifications)
```

---

*End of Document*
