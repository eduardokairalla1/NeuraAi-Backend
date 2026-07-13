"""
Schemas for search endpoint payload.
"""

# --- IMPORTS ---
from neura_backend.app import container
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from pydantic import field_validator


# --- CODE ---
class SearchPayload(BaseModel):
    """
    Schema for search endpoint payload.
    """
    message: str


    @field_validator('message')
    def validate_message(cls, message: str) -> str:
        """
        Validates the message length.

        :param message: The message string to validate.

        :return: The validated message string.

        :raises ValueError: If the message exceeds the length limit.
        """

        # Message length exceeds limit: raise 'Bad Request' error
        if len(message.strip()) > container['config'].USER_MESSAGE_LENGTH_LIMIT:
            raise HTTPException(status_code=400, detail='Message exceeds the length limit.')

        # Return validated message
        return message
