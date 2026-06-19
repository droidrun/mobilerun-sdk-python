# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...shared.pagination import Pagination

__all__ = ["CatalogListResponse", "Item"]


class Item(BaseModel):
    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    event_type: str = FieldInfo(alias="eventType")

    label: str

    source: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    payload_schema: Optional[object] = FieldInfo(alias="payloadSchema", default=None)


class CatalogListResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
