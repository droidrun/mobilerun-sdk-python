# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NumberBindingListResponse", "Item"]


class Item(BaseModel):
    bound_at: datetime = FieldInfo(alias="boundAt")

    device_id: str = FieldInfo(alias="deviceId")

    device_name: str = FieldInfo(alias="deviceName")

    number_id: str = FieldInfo(alias="numberId")


class NumberBindingListResponse(BaseModel):
    items: Optional[List[Item]] = None

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
