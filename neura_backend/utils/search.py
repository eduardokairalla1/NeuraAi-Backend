"""
Utility functions for performing search operations.
"""

# --- IMPORTS ---
from neura_backend.app import container
from neura_backend.err.search_error import SearchError


# --- CODE ---
async def tavily_search(query: str, max_results: int, max_chars: int) -> tuple[str, str, str]:
    """
    Performs a web search using the Tavily client and extracts content from the results.

    :param query: The search query.
    :param max_results: Maximum number of search results to retrieve.
    :param max_chars: Maximum number of characters to retrieve from the content.

    :return: A tuple containing the title, raw content, and URL of the best search result.

    :raises SearchError: If an error occurs during the search or extraction process.
    """

    # Get Tavily client
    tavily_client = container['tavily_client']

    # Web search
    try:

        # Perform search using Tavily
        search_response = await tavily_client.search(query=query,
                                                     max_results=max_results,
                                                     include_raw_content=True)

        # Check if there are any results
        results = search_response.get('results', [])

        # No results found: raise SearchError
        if not results:
            raise SearchError(f'No search results for query: {query}')

        # Define extraction and url
        raw_content = ''
        title = ''
        url = ''
        extraction = None

        # Try to extract content from each result until successful
        for result in search_response['results']:

            # Get URL from the result
            url = result['url']

            # Perform extraction
            extraction = await tavily_client.extract(urls=url)

            # Extraction yielded results: break the loop
            if len(extraction['results']) > 0:

                # Use extracted content
                raw_content = extraction['results'][0]['raw_content']

                # Set title to the extracted result title
                title = extraction['results'][0]['title']

                # Set url to the extracted result url
                url = extraction['results'][0]['url']

                # Break the loop
                break

        # No accessible URLs found: fallback to search results
        if not extraction or len(extraction['results']) == 0:

            # Define parts from search results
            content_parts = []
            url_parts = []
            title_parts = []

            # Iterate over search results to build content
            for i, result in enumerate(search_response.get('results', [])):

                # Get title, url and content
                title = result.get('title') or ''
                url_ = result.get('url') or ''
                content = (result.get('raw_content') or result.get('content') or '').strip()

                # Append formatted content part
                content_parts.append(
                    f"Result {i+1}:\n"
                    f"Title: {title}\n"
                    f"URL: {url_}\n"
                    f"Content: {content}\n"
                    f"================\n\n"
                )

                # Append formatted url part
                url_parts.append(f"[{i+1}] - ({url_})\n")

                # Append formatted title part
                title_parts.append(f"[{i+1}] - {title}\n")

            # Transform parts into final content and url
            raw_content = ''.join(content_parts).strip()
            url = ''.join(url_parts).strip()
            title = ''.join(title_parts).strip()

        # Content exceeds max chars: truncate
        if len(raw_content) > max_chars:
            raw_content = raw_content[:max_chars] + "\n...[truncated]"

        # Return the final content and url
        return title, raw_content, url

    # Error during search or extraction: raise custom error
    except Exception as e:
        raise SearchError(f'Error during search or extraction: {str(e)}') from e
