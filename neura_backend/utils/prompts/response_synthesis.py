"""
Response synthesis prompt template.
"""

# --- IMPORTS ---
from neura_backend.utils.prompts.base import base_prompt_template


# --- GLOBALS ---
SYSTEM_PROMPT = '''
Your objective is to craft a comprehensive and well-structured final response for the user, based on the reports
generated during the web search and your synthesis of those findings.

The final answer should:
- Contain between 500 and 800 words.
- Be written in a clear, coherent, and professional tone.
- Integrate relevant information from the web search results logically and cohesively.
- Include reference citations in numerical format (e.g., [1], [2]) corresponding to the sources used in each paragraph.

Here are the web search results:

<SEARCH_RESULTS>

{search_results}

</SEARCH_RESULTS>
'''

# --- CODE ---
response_synthesis_prompt_template = base_prompt_template + [('human', SYSTEM_PROMPT)]
