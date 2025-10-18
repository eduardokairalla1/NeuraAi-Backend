"""
Container (dependency injection) Schema.
"""

# --- IMPORTS ---
from neura_backend.models import Config
from tavily import AsyncTavilyClient


# --- TYPES ---
from typing import TypedDict


# --- CODE ---
class Container(TypedDict):
    """
    Structure for global application resources.
    """
    config: Config
    tavily_client: AsyncTavilyClient
