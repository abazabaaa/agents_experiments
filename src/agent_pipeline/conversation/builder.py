"""Utilities for constructing OpenAI Agents SDK conversation payloads."""

from __future__ import annotations

from collections.abc import Iterable, MutableSequence, Sequence
from dataclasses import dataclass, field

MessageDict = dict[str, str]
Conversation = list[MessageDict]
AgentInput = str | Sequence[MessageDict]


def user_message(content: str) -> MessageDict:
    """Create a user-role message."""

    return {"role": "user", "content": content}


def developer_message(content: str) -> MessageDict:
    """Create a developer-role message."""

    return {"role": "developer", "content": content}


def assistant_message(content: str) -> MessageDict:
    """Create an assistant-role message."""

    return {"role": "assistant", "content": content}


@dataclass
class ConversationBuilder:
    """Mutable helper for assembling message lists."""

    items: MutableSequence[MessageDict] = field(default_factory=list)

    def add(self, role: str, content: str) -> None:
        self.items.append({"role": role, "content": content})

    def add_user(self, content: str) -> None:
        self.items.append(user_message(content))

    def add_developer(self, content: str) -> None:
        self.items.append(developer_message(content))

    def add_assistant(self, content: str) -> None:
        self.items.append(assistant_message(content))

    def extend(self, messages: Iterable[MessageDict]) -> None:
        self.items.extend(messages)

    def build(self) -> Conversation:
        return list(self.items)


def ensure_conversation(agent_input: AgentInput) -> Conversation:
    """Normalise agent input into a list of message dictionaries."""

    if isinstance(agent_input, str):
        return [user_message(agent_input)]
    return list(agent_input)
