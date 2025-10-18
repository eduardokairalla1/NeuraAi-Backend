"""
Resume search prompt template.
"""

# --- IMPORTS ---
from neura_backend.utils.prompts.base import base_prompt_template


# --- GLOBALS ---
SYSTEM_PROMPT = '''
Your task is to carefully analyze the web search results below and produce a clear, concise synthesis.
Focus only on information that directly answers or supports the user's query — ignore irrelevant details,
repeated data, or background context that doesn’t contribute to the answer.

Your output will be used by another agent to craft the final response to the user,
so ensure the synthesis is factual, well-organized, and easy to read.

Be objective and concise.

Here are the web search results:

<SEARCH_RESULTS>

{search_results}

</SEARCH_RESULTS>
'''

# --- CODE ---
resume_search_prompt_template = base_prompt_template + [('human', SYSTEM_PROMPT)]
