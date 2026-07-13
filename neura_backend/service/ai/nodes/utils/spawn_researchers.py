"""
Module for spawning searcher nodes.
"""

# --- IMPORTS ---
from langgraph.types import Send
from neura_backend.service.ai.state import State


# --- TYPES ---
from typing import List


# --- CODE ---
def spawn_searchers(state: State) -> List[Send]:
    """
    Spawns searcher nodes for each query in the state.

    :param state: The current state containing user input and queries.

    :return: A list of Send objects to the single_search node for each query.
    """

    # Extract user input from the state
    user_input = state['user_input']

    # Create a Send object for each query in the state and return the list
    return [Send('single_search', {'query': query, 'user_input': user_input}) for query in state['queries']]
