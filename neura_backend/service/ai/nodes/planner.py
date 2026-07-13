"""
Node to plan queries based on user input.
"""

# --- IMPORTS ---
from neura_backend.app import container
from neura_backend.err.node_error import NodeError
from neura_backend.utils.prompts.query_planner import query_planner_prompt_template


# --- TYPES ---
from neura_backend.schemas.ai.outputs.query_list import QueryList
from neura_backend.service.ai.state import State


# --- CODE ---
async def plan_query(state: State) -> State:
    """
    Plans queries based on user input and updates the state with the list of queries.

    :param state: The current state containing user input.

    :return: Updated state with planned queries.
    """

    # Format LLM prompt with user input
    prompt = query_planner_prompt_template.format_messages(user_input=state['user_input'])

    # Define LLM with structured output
    llm = container['planner_llm'].with_structured_output(schema=QueryList, include_raw=True)

    # Invoke LLM
    try:
        response = await llm.ainvoke(prompt)

    # Error during LLM invocation: raise custom error
    except Exception as e:
        raise NodeError(f'Error during query planning: {str(e)}') from e

    # Update state with the list of queries
    state['queries'] = response['parsed'].queries

    # Return updated state
    return state
