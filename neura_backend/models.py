"""
Data models.
"""

# --- IMPORTS ---
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import Any
from typing import Dict
from typing import Literal


# --- CODE ---
# Config model
class Config(BaseSettings):
    """
    Application configuration.
    """
    # --- APP CONFIGS ---
    USER_MESSAGE_LENGTH_LIMIT: int = 1500

    # --- AI CONFIGS ---
    OPENAI_API_KEY: str
    OPENAI_PLANNER_MODEL: str
    OPENAI_SEARCHER_MODEL: str
    OPENAI_WRITER_MODEL: str

    # --- TAVILY CONFIGS ---
    TAVILY_API_KEY: str

    # --- SEARCH CONFIGS ---
    MAX_URL_SEARCH_PER_QUERY: int = 3
    MAX_CHARS_PER_CONTENT_SEARCH: int = 50000

    class Config:
        """
        Pydantic settings configuration.
        """
        env_file = ".env"


# Health model
class Health(BaseModel):
    """
    System health status.
    """
    status: Literal['OK', 'WARNING', 'FAILURE', 'UNKNOWN'] = 'UNKNOWN'


# Info model
class Info(BaseModel):
    """
    System information.
    """
    name: str
    description: str
    version: str
    extra: Dict[str, Any]


# --- Forward references ---
Config.model_rebuild()
Health.model_rebuild()
Info.model_rebuild()
