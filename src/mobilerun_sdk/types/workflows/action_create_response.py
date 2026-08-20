# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ActionCreateResponse", "Data"]


class Data(BaseModel):
    id: str

    catalog_entry_id: str = FieldInfo(alias="catalogEntryId")

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    description: Optional[str] = None

    method: str

    name: str

    owner_id: str = FieldInfo(alias="ownerId")

    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"]

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")
    """Deprecated: use ownerId (tenancy) / createdBy (actor)."""

    params: Optional[object] = None

    params_schema: Optional[object] = FieldInfo(alias="paramsSchema", default=None)


class ActionCreateResponse(BaseModel):
    data: Data
