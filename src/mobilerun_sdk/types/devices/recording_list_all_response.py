# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecordingListAllResponse", "Item", "ItemDisplay", "ItemVideo"]


class ItemDisplay(BaseModel):
    height: int

    rotation: int

    width: int


class ItemVideo(BaseModel):
    duration_ms: int = FieldInfo(alias="durationMs")

    format: str

    size_bytes: int = FieldInfo(alias="sizeBytes")

    limited: Optional[bool] = None

    limit_reason: Optional[str] = FieldInfo(alias="limitReason", default=None)


class Item(BaseModel):
    id: str

    actions: int

    device_id: str = FieldInfo(alias="deviceId")

    display: ItemDisplay

    expires_at: datetime = FieldInfo(alias="expiresAt")

    name: str

    started_at: datetime = FieldInfo(alias="startedAt")

    status: str

    types: Optional[List[str]] = None

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)

    error: Optional[str] = None

    video: Optional[ItemVideo] = None


class RecordingListAllResponse(BaseModel):
    items: Optional[List[Item]] = None

    next_cursor: str = FieldInfo(alias="nextCursor")

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
