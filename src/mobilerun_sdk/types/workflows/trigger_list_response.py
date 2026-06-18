# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["TriggerListResponse", "Item", "ItemScheduleRule"]


class ItemScheduleRule(BaseModel):
    type: Literal["once", "cron", "recurring"]

    date_time: Optional[str] = FieldInfo(alias="dateTime", default=None)
    """ISO 8601 datetime (for type=once)"""

    expression: Optional[str] = None
    """Cron expression (for type=cron)"""

    rrule: Optional[str] = None
    """RRULE string (for type=recurring)"""


class Item(BaseModel):
    id: str

    activation: Literal["event", "schedule", "custom"]

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    custom_payload_schema: Optional[Dict[str, object]] = FieldInfo(alias="customPayloadSchema", default=None)

    description: Optional[str] = None

    event_type: Optional[str] = FieldInfo(alias="eventType", default=None)

    name: str

    schedule_rule: Optional[ItemScheduleRule] = FieldInfo(alias="scheduleRule", default=None)

    timezone: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")

    conditions: Optional[object] = None

    next_fire_time: Optional[str] = FieldInfo(alias="nextFireTime", default=None)


class TriggerListResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
