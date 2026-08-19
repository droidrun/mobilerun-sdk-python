# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Dict, List

from pydantic import Field as FieldInfo

from typing_extensions import Literal

from .shared.pagination import Pagination

__all__ = ["AppEventListResponse", "Item"]

class Item(BaseModel):
    id: str

    created_at: Optional[str] = FieldInfo(alias = "createdAt", default = None)

    created_by: Optional[str] = FieldInfo(alias = "createdBy", default = None)

    device_id: Optional[str] = FieldInfo(alias = "deviceId", default = None)

    event_type: str = FieldInfo(alias = "eventType")

    occurred_at: Optional[str] = FieldInfo(alias = "occurredAt", default = None)

    owner_id: str = FieldInfo(alias = "ownerId")

    payload: Dict[str, object]

    raw_event_id: Optional[str] = FieldInfo(alias = "rawEventId", default = None)

    source: Literal["app", "system", "device", "webhook"]

    user_id: str = FieldInfo(alias = "userId")
    """Deprecated: use ownerId (tenancy) / createdBy (actor)."""

class AppEventListResponse(BaseModel):
    items: List[Item]

    pagination: Pagination