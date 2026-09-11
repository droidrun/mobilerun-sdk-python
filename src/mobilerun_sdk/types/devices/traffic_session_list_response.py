# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.meta import Meta

__all__ = ["TrafficSessionListResponse", "Item", "ItemError", "ItemStream"]


class ItemError(BaseModel):
    code: str

    message: str


class ItemStream(BaseModel):
    token: str

    protocol: str

    url: str


class Item(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    device_id: str = FieldInfo(alias="deviceId")

    expires_at: datetime = FieldInfo(alias="expiresAt")

    max_body_bytes: int = FieldInfo(alias="maxBodyBytes")

    retention: Literal["none"]

    state: Literal["starting", "active", "stopping", "stopped", "failed", "expired"]

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    error: Optional[ItemError] = None

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    stopped_at: Optional[datetime] = FieldInfo(alias="stoppedAt", default=None)

    stream: Optional[ItemStream] = None


class TrafficSessionListResponse(BaseModel):
    items: Optional[List[Item]] = None

    pagination: Meta

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
