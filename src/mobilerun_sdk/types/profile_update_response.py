# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from pydantic import Field as FieldInfo

from .shared.device_spec import DeviceSpec

from typing import Optional

__all__ = ["ProfileUpdateResponse"]

class ProfileUpdateResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias = "createdAt")

    name: str

    owner_id: str = FieldInfo(alias = "ownerId")

    spec: DeviceSpec

    updated_at: datetime = FieldInfo(alias = "updatedAt")

    user_id: str = FieldInfo(alias = "userId")
    """Deprecated: use ownerId/createdBy."""

    schema_: Optional[str] = FieldInfo(alias = "$schema", default = None)
    """A URL to the JSON Schema for this object."""

    created_by: Optional[str] = FieldInfo(alias = "createdBy", default = None)