# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecordingStatusResponse", "Display", "Video"]


class Display(BaseModel):
    height: int

    rotation: int

    width: int


class Video(BaseModel):
    duration_ms: int = FieldInfo(alias="durationMs")

    format: str

    size_bytes: int = FieldInfo(alias="sizeBytes")

    limited: Optional[bool] = None

    limit_reason: Optional[str] = FieldInfo(alias="limitReason", default=None)


class RecordingStatusResponse(BaseModel):
    id: str

    actions: int

    device_id: str = FieldInfo(alias="deviceId")

    display: Display

    expires_at: datetime = FieldInfo(alias="expiresAt")

    name: str

    started_at: datetime = FieldInfo(alias="startedAt")

    status: str

    types: Optional[List[str]] = None

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)

    error: Optional[str] = None

    video: Optional[Video] = None
