"""
Search Error.
"""

# --- IMPORTS ---
from neura_backend.err.neura_backend_error import NeuraBackendError


# --- CODE ---
class SearchError(NeuraBackendError):
    """
    Search Error.
    """
    message = 'Search Error'
