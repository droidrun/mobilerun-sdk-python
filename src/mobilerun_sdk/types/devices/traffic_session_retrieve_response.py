# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TrafficSessionRetrieveResponse", "Error", "Stream"]


class Error(BaseModel):
    code: str

    message: str


class Stream(BaseModel):
    token: str

    protocol: str

    url: str


class TrafficSessionRetrieveResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    device_id: str = FieldInfo(alias="deviceId")

    expires_at: datetime = FieldInfo(alias="expiresAt")

    max_body_bytes: int = FieldInfo(alias="maxBodyBytes")

    retention: Literal["none"]

    state: Literal["starting", "active", "stopping", "stopped", "failed", "expired"]

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    error: Optional[Error] = None

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    stopped_at: Optional[datetime] = FieldInfo(alias="stoppedAt", default=None)

    stream: Optional[Stream] = None
