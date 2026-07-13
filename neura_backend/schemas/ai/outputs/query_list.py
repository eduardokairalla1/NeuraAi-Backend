"""
Custom LLM output for a list of queries.
"""

# --- IMPORTS ---
from pydantic import BaseModel


# --- TYPES ---
from typing import List


# --- CODE ---
class QueryList(BaseModel):
    """
    Custom LLM output for a list of queries.
    """
    queries: List[str]
