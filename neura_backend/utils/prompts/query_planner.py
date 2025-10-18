"""
Query planner prompt template.
"""

# --- IMPORTS ---
from neura_backend.utils.prompts.base import base_prompt_template


# --- GLOBALS ---
SYSTEM_PROMPT = '''
Your first task is to generate a focused list of search queries that will help gather precise and comprehensive answers
to the user's question.

Guidelines:
- Write 3 to 5 well-defined queries.
- Each query should target a specific subtopic or angle related to the main question.
- Make sure the queries are optimized for finding high-quality, factual information.

Return only the list of queries, numbered.
'''


# --- CODE ---
query_planner_prompt_template = base_prompt_template + [('human', SYSTEM_PROMPT)]
