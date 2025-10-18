"""
HTTP routers.
"""

# --- IMPORTS ---
from fastapi import FastAPI
from neura_backend.routers import system


# --- CODE ---
def mount(app: FastAPI) -> None:
    """
    Mount all routers on application.

    :param app: main app router

    :returns: nothing
    """
    app.include_router(system.router, tags = ['system'])
