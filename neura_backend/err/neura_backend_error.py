"""
Base Neura backend error.
"""

# --- TYPES ---
from typing import Any


# --- GLOBAL ---
DEFAULT_MESSAGE = 'Generic Neura backend error'


# --- ERROR CLASS ---
class NeuraBackendError(Exception):
    """
    Base Neura backend error.
    """
    message = DEFAULT_MESSAGE

    def __init__(self, *args: Any) -> None:
        """
        Initialize a Neura backend error.

        :param *args: Optional additional context or details for the error.

        :returns: None.
        """
        super().__init__(self.message, *args)
