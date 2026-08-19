# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Dict

from pydantic import Field as FieldInfo

from typing_extensions import Literal

__all__ = ["TriggerCreateResponse", "Data", "DataScheduleRule", "DataScheduleRuleJitter"]

class DataScheduleRuleJitter(BaseModel):
    """Optional per-occurrence random window around the nominal schedule time"""
    after_minutes: Optional[int] = FieldInfo(alias = "afterMinutes", default = None)

    before_minutes: Optional[int] = FieldInfo(alias = "beforeMinutes", default = None)

class DataScheduleRule(BaseModel):
    type: Literal["once", "cron", "recurring"]

    date_time: Optional[str] = FieldInfo(alias = "dateTime", default = None)
    """ISO 8601 datetime (for type=once)"""

    expression: Optional[str] = None
    """Cron expression (for type=cron)"""

    jitter: Optional[DataScheduleRuleJitter] = None
    """Optional per-occurrence random window around the nominal schedule time"""

    rrule: Optional[str] = None
    """RRULE string (for type=recurring)"""

class Data(BaseModel):
    id: str

    activation: Literal["event", "schedule", "custom"]

    created_at: Optional[str] = FieldInfo(alias = "createdAt", default = None)

    created_by: Optional[str] = FieldInfo(alias = "createdBy", default = None)

    custom_payload_schema: Optional[Dict[str, object]] = FieldInfo(alias = "customPayloadSchema", default = None)

    description: Optional[str] = None

    event_type: Optional[str] = FieldInfo(alias = "eventType", default = None)

    name: str

    owner_id: str = FieldInfo(alias = "ownerId")

    schedule_rule: DataScheduleRule = FieldInfo(alias = "scheduleRule")

    timezone: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias = "updatedAt", default = None)

    user_id: str = FieldInfo(alias = "userId")
    """Deprecated: use ownerId (tenancy) / createdBy (actor)."""

    conditions: Optional[object] = None

    next_fire_time: Optional[str] = FieldInfo(alias = "nextFireTime", default = None)

class TriggerCreateResponse(BaseModel):
    data: Data