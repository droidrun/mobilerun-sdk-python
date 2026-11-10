# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["StateListResponse", "Data"]


class Data(BaseModel):
    key: str

    saved_at: datetime = FieldInfo(alias="savedAt")

    size_bytes: int = FieldInfo(alias="sizeBytes")

    version: int
    """Newest saved version of this key"""


class StateListResponse(BaseModel):
    data: List[Data]
