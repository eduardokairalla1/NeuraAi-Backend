"""
Base prompt templates for AI tasks.
"""

# --- IMPORTS ---
from langchain_core.prompts import ChatPromptTemplate


# --- GLOBALS ---
SYSTEM_PROMPT = """
You are an advanced research planner.

Your role is to design a structured research plan to answer the user's question using reliable, up-to-date online
sources.

Your reasoning and outputs must be:
- Technical and factual
- Based on verifiable data and evidence
- Clear and concise

Cite relevant details, data, and context when possible.

Here is the user input:
"""

USER_MESSAGE = """
<USER_INPUT>

{user_input}

</USER_INPUT>
"""


# --- CODE ---
base_prompt_template = ChatPromptTemplate.from_messages([
    ('system', SYSTEM_PROMPT),
    ('human', USER_MESSAGE)
])
