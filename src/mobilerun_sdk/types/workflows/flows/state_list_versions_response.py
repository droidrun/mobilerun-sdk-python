# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["StateListVersionsResponse", "Data"]


class Data(BaseModel):
    execution_id: str = FieldInfo(alias="executionId")
    """Execution that saved this version"""

    saved_at: datetime = FieldInfo(alias="savedAt")

    size_bytes: int = FieldInfo(alias="sizeBytes")

    version: int

    value: Optional[object] = None
    """The saved JSON value"""


class StateListVersionsResponse(BaseModel):
    data: List[Data]
