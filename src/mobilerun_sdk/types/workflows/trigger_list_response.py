# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["TriggerListResponse", "Item", "ItemScheduleRule", "ItemScheduleRuleJitter"]


class ItemScheduleRuleJitter(BaseModel):
    """Optional per-occurrence random window around the nominal schedule time"""

    after_minutes: Optional[int] = FieldInfo(alias="afterMinutes", default=None)

    before_minutes: Optional[int] = FieldInfo(alias="beforeMinutes", default=None)


class ItemScheduleRule(BaseModel):
    type: Literal["once", "cron", "recurring"]

    date_time: Optional[str] = FieldInfo(alias="dateTime", default=None)
    """ISO 8601 datetime (for type=once)"""

    expression: Optional[str] = None
    """Cron expression (for type=cron)"""

    jitter: Optional[ItemScheduleRuleJitter] = None
    """Optional per-occurrence random window around the nominal schedule time"""

    rrule: Optional[str] = None
    """RRULE string (for type=recurring)"""


class Item(BaseModel):
    id: str

    activation: Literal["event", "schedule", "custom"]

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    custom_payload_schema: Optional[Dict[str, object]] = FieldInfo(alias="customPayloadSchema", default=None)

    description: Optional[str] = None

    event_type: Optional[str] = FieldInfo(alias="eventType", default=None)

    name: str

    owner_id: str = FieldInfo(alias="ownerId")

    schedule_rule: ItemScheduleRule = FieldInfo(alias="scheduleRule")

    timezone: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")
    """Deprecated: use ownerId (tenancy) / createdBy (actor)."""

    conditions: Optional[object] = None

    next_fire_time: Optional[str] = FieldInfo(alias="nextFireTime", default=None)


class TriggerListResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
