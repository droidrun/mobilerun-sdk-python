# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from pydantic import Field as FieldInfo

from typing import Optional, List

from datetime import datetime

from typing_extensions import TypeAliasType, TypeAlias

__all__ = ["RecordingListResponse", "RecordingListResponseItem", "RecordingListResponseItemDisplay", "RecordingListResponseItemVideo"]

class RecordingListResponseItemDisplay(BaseModel):
    height: int

    rotation: int

    width: int

class RecordingListResponseItemVideo(BaseModel):
    duration_ms: int = FieldInfo(alias = "durationMs")

    format: str

    size_bytes: int = FieldInfo(alias = "sizeBytes")

    limited: Optional[bool] = None

    limit_reason: Optional[str] = FieldInfo(alias = "limitReason", default = None)

class RecordingListResponseItem(BaseModel):
    id: str

    actions: int

    device_id: str = FieldInfo(alias = "deviceId")

    display: RecordingListResponseItemDisplay

    expires_at: datetime = FieldInfo(alias = "expiresAt")

    name: str

    started_at: datetime = FieldInfo(alias = "startedAt")

    status: str

    types: Optional[List[str]] = None

    schema_: Optional[str] = FieldInfo(alias = "$schema", default = None)
    """A URL to the JSON Schema for this object."""

    ended_at: Optional[datetime] = FieldInfo(alias = "endedAt", default = None)

    error: Optional[str] = None

    video: Optional[RecordingListResponseItemVideo] = None

RecordingListResponse: TypeAlias = List[RecordingListResponseItem]