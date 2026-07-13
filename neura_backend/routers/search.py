"""
System endpoints.
"""

# --- IMPORTS ---
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from neura_backend.schemas.endpoints.search_payload import SearchPayload
from neura_backend.service.ai.graph import web_search_agent
from neura_backend.service.ai.state import State


# --- GLOBAL ---
# Router instance
router = APIRouter()


# --- CODE ---
@router.post('/search', response_model = dict)
async def search(payload: SearchPayload) -> JSONResponse:
    """
    Performs a search llm operation.

    :param payload: The search payload.

    :return: The JSON response with search results.
    """

    # Get user message from payload
    message = payload.message

    # Create initial state for the agent
    state: State = {
        'user_input': message
    }

    # Call the web search agent
    search_results = await web_search_agent.ainvoke(state)

    # Build response
    response = {
        'response': search_results['final_response'],
        'executed_queries': search_results['queries'],
    }

    # Return JSON response
    return JSONResponse(content=response)
