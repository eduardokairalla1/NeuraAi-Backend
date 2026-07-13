"""
Individual query results schema.
"""

# --- IMPORTS ---
from pydantic import BaseModel


# --- TYPES ---
from typing import Optional


# --- CODE ---
class QueryResult(BaseModel):
    """
    Schema for individual query results.
    """
    title: Optional[str] = None
    url: Optional[str] = None
    resume: Optional[str] = None
