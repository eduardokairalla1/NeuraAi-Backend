"""
Node to write the final response.
"""

# --- IMPORTS ---
from neura_backend.app import container
from neura_backend.err.node_error import NodeError
from neura_backend.service.ai.state import State
from neura_backend.utils.prompts.response_synthesis import response_synthesis_prompt_template


# --- CODE ---
async def final_writer(state: State) -> State:
    """
    Writes the final response based on the collected query results.

    :param state: The current state containing user input and query results.

    :return: Updated state with the final response.
    """

    # Build search results
    search_results = '\n'.join([
        f'[{i+1}]\n\n'
        f'Title: {result.title}\n'
        f'URL: {result.url}\n'
        f'Content: {result.resume}\n'
        f'=========================='
        for i, result in enumerate(state['queries_results'])
    ])

    # Build references
    references = '\n'.join(
        [f'[{i+1}] - [{result.title}]({result.url})' for i, result in enumerate(state['queries_results'])]
    )

    # Extract user input
    user_input = state['user_input']

    # Format prompt
    prompt = response_synthesis_prompt_template.format_messages(user_input=user_input, search_results=search_results)

    # Get writer LLM
    llm = container['writer_llm']

    # Invoke LLM
    try:
        result = await llm.ainvoke(prompt)

    # Error during LLM invocation: raise custom error
    except Exception as e:
        raise NodeError(f'Error during final writing: {str(e)}') from e

    # Build final response with references
    final_response = result.content + '\n\n References:\n' + references

    # Update state with the final response
    state['final_response'] = final_response

    # Return updated state
    return state
