# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScreenshotListResponse", "Item"]


class Item(BaseModel):
    id: str

    captured_at: datetime = FieldInfo(alias="capturedAt")

    device_id: str = FieldInfo(alias="deviceId")

    expires_at: datetime = FieldInfo(alias="expiresAt")

    recording_id: Optional[str] = FieldInfo(alias="recordingId", default=None)

    size_bytes: int = FieldInfo(alias="sizeBytes")


class ScreenshotListResponse(BaseModel):
    items: Optional[List[Item]] = None

    next_cursor: str = FieldInfo(alias="nextCursor")

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
