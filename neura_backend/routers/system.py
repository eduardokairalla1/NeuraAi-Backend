"""
System endpoints.
"""

# --- IMPORTS ---
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from neura_backend.app import health
from neura_backend.app import info
from neura_backend.models import Health
from neura_backend.models import Info


# --- GLOBAL ---
# Router instance
router = APIRouter()


# --- CODE ---
# Health endpoint
@router.get('/health', response_model = Health)
def get_health() -> JSONResponse:
    """
    Returns the current system health status.
    """
    return JSONResponse(health.model_dump())


# Info endpoint
@router.get('/info', response_model = Info)
def get_info() -> JSONResponse:
    """
    Returns system information.
    """
    return JSONResponse(info.model_dump())
