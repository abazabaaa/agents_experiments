"""Agent pipeline package."""

from __future__ import annotations

from dotenv import load_dotenv

# Load environment variables from a local .env file before importing submodules.
# This ensures the OpenAI Agents SDK sees ``OPENAI_API_KEY`` and related values
# during import time, which keeps authentication working even when the key is
# not exported globally in the shell environment.
load_dotenv()
