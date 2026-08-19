# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Dict, List

from pydantic import Field as FieldInfo

from ..shared.pagination import Pagination

__all__ = ["TriggerListResponse", "Item"]

class Item(BaseModel):
    id: str

    activation: Literal["event", "schedule", "custom"]

    created_at: Optional[str] = FieldInfo(alias = "createdAt", default = None)

    created_by: Optional[str] = FieldInfo(alias = "createdBy", default = None)

    custom_payload_schema: Optional[Dict[str, object]] = FieldInfo(alias = "customPayloadSchema", default = None)

    description: Optional[str] = None

    event_type: Optional[str] = FieldInfo(alias = "eventType", default = None)

    name: str

    owner_id: str = FieldInfo(alias = "ownerId")

    schedule_rule: object = FieldInfo(alias = "scheduleRule")

    timezone: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias = "updatedAt", default = None)

    user_id: str = FieldInfo(alias = "userId")
    """Deprecated: use ownerId (tenancy) / createdBy (actor)."""

    conditions: Optional[object] = None

    next_fire_time: Optional[str] = FieldInfo(alias = "nextFireTime", default = None)

class TriggerListResponse(BaseModel):
    items: List[Item]

    pagination: Pagination