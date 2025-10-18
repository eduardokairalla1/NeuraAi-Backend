"""
Startup and shutdown event handlers.
"""

# --- IMPORTS ---
from fastapi import FastAPI
from neura_backend import routers
from neura_backend.app import container
from neura_backend.app import health
from tavily import AsyncTavilyClient


# --- CODE ---
def on_startup(app: FastAPI) -> None:
    """
    Initialize the service on startup.
    """
    # Mount routers
    routers.mount(app)

    # Initialize Tavily client
    tavily_client = AsyncTavilyClient(api_key=container['config'].TAVILY_API_KEY)

    # Update container
    container.update({
        'tavily_client': tavily_client,
    })

    # Set app health as OK
    health.status = 'OK'


def on_shutdown(app: FastAPI) -> None:  #pylint: disable=W0613
    """
    Run on service shutdown.
    """
    pass
