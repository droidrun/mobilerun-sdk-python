# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["ActionCatalogListResponse", "Item"]


class Item(BaseModel):
    id: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    method: str

    name: str

    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"]

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    params_schema: Optional[object] = FieldInfo(alias="paramsSchema", default=None)


class ActionCatalogListResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
