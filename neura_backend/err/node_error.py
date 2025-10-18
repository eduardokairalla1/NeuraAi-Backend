"""
Node Error.
"""

# --- IMPORTS ---
from neura_backend.err.neura_backend_error import NeuraBackendError


# --- CODE ---
class NodeError(NeuraBackendError):
    """
    Node Error.
    """
    message = 'Node Error'
