# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.meta import Meta
from .shared.device_spec import DeviceSpec

__all__ = ["ProfileListResponse", "Item"]


class Item(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    owner_id: str = FieldInfo(alias="ownerId")

    spec: DeviceSpec

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user_id: str = FieldInfo(alias="userId")
    """Deprecated: use ownerId/createdBy."""

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)


class ProfileListResponse(BaseModel):
    items: Optional[List[Item]] = None

    pagination: Meta

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
