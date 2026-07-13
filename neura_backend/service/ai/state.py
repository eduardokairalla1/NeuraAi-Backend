"""
Base AI state definition.
"""

# --- IMPORTS ---
from neura_backend.schemas.ai.query_results import QueryResult

import operator


# --- TYPES ---
from typing import Annotated
from typing import List
from typing import Optional
from typing import TypedDict


# --- CODE ---
class State(TypedDict):
    """
    Represents the state of the AI system.
    """
    user_input: Optional[str]
    final_response: Optional[str]
    queries: List[str]
    queries_results: Annotated[List[QueryResult], operator.add]
