"""
HTTP routers.
"""

# --- IMPORTS ---
from fastapi import FastAPI
from neura_backend.routers import search
from neura_backend.routers import system


# --- CODE ---
def mount(app: FastAPI) -> None:
    """
    Mount all routers on application.

    :param app: main app router

    :returns: nothing
    """
    app.include_router(system.router, tags = ['system'])
    app.include_router(search.router, tags = ['search'])
