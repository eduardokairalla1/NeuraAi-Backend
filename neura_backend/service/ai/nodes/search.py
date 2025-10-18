"""
Node to perform a single search and summarize the result.
"""

# --- IMPORTS ---
from neura_backend.app import container
from neura_backend.err.node_error import NodeError
from neura_backend.schemas.ai.query_results import QueryResult
from neura_backend.utils.prompts.resume_search import resume_search_prompt_template
from neura_backend.utils.search import tavily_search


# --- TYPES ---
from typing import Dict
from typing import List


# --- CODE ---
async def single_search(data: dict) -> Dict[str, List[QueryResult]]:
    """
    Performs a single search for the given query and summarizes the result.

    :param data: Dictionary containing 'query' and 'user_input'.

    :return: A dictionary containing the summarized search result.
    """

    # Extract query and user_input from data
    query = data['query']
    user_input = data['user_input']

    # Perform Tavily search
    title, raw_content, url = await tavily_search(
        query=query,
        max_results=container['config'].MAX_URL_SEARCH_PER_QUERY,
        max_chars=container['config'].MAX_CHARS_PER_CONTENT_SEARCH
    )

    # Get searcher LLM
    llm = container['searcher_llm']

    # Format prompt for resume search
    prompt = resume_search_prompt_template.format_messages(user_input=user_input, search_results=raw_content)

    # Invoke LLM
    try:
        llm_response = await llm.ainvoke(prompt)

    # Error during LLM invocation: raise custom error
    except Exception as e:
        raise NodeError(f'Error during single search: {str(e)}') from e

    # Create QueryResult object with the summarized content
    query_results = QueryResult(title=title,
                                url=url,
                                resume=llm_response.content)

    # Return the query results
    return {'queries_results': [query_results]}
