# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ModelListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Model identifier"""

    owned_by: str
    """Model owner/provider"""

    created: Optional[int] = None
    """Creation timestamp"""

    object: Optional[str] = None
    """Object type"""


class ModelListResponse(BaseModel):
    data: List[Data]
    """Available models"""

    object: Optional[str] = None
    """Object type"""
