"""
Service entry point.
"""

# --- IMPORTS ---
from contextlib import asynccontextmanager
from fastapi import FastAPI
from neura_backend.app import app
from neura_backend.events import on_shutdown
from neura_backend.events import on_startup


# --- CODE ---
@asynccontextmanager
async def lifespan(application: FastAPI):
    """
    Handles startup and shutdown events for the application.
    """
    # Startup tasks
    on_startup(application)

    # Run the app
    try:
        yield

    # Shutdown tasks
    finally:
        on_shutdown(application)

# Attach lifespan to the app
app.router.lifespan_context = lifespan
