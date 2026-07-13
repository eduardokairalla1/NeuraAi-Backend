"""
Global service objects.
"""

# --- IMPORTS ---
from fastapi import FastAPI
from neura_backend.models import Config
from neura_backend.models import Health
from neura_backend.models import Info
from neura_backend.schemas.container import Container


# --- CODE ---
# FastAPI app
app = FastAPI(
    title = 'Neura AI Backend',
    description = 'This is Neura AI service'
)

# Configuration
config = Config()

# Info
info = Info(
    name = app.title,
    description = app.description,
    version = app.version,
    extra = {}
)

# System health
health = Health()

# Dependency injection
container: Container = {
    'config': config,
}
