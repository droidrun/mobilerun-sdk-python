# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ConversationMarkReadResponse", "Data"]


class Data(BaseModel):
    updated: int


class ConversationMarkReadResponse(BaseModel):
    data: Data
