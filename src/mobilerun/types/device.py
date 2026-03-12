# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Device"]


class Device(BaseModel):
    id: str

    assigned_at: Optional[datetime] = FieldInfo(alias="assignedAt", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    state: str

    state_message: str = FieldInfo(alias="stateMessage")

    stream_url: str = FieldInfo(alias="streamUrl")

    task_count: int = FieldInfo(alias="taskCount")

    terminates_at: Optional[datetime] = FieldInfo(alias="terminatesAt", default=None)

    type: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    stream_token: Optional[str] = FieldInfo(alias="streamToken", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
