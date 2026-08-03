# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TriggerUpdateParams", "Conditions", "ScheduleRule", "ScheduleRuleJitter"]


class TriggerUpdateParams(TypedDict, total=False):
    activation: Literal["event", "schedule", "custom"]

    conditions: Conditions

    custom_payload_schema: Annotated[Dict[str, object], PropertyInfo(alias="customPayloadSchema")]

    description: str

    event_type: Annotated[str, PropertyInfo(alias="eventType")]

    name: str

    schedule_rule: Annotated[ScheduleRule, PropertyInfo(alias="scheduleRule")]

    timezone: Optional[str]


class Conditions(TypedDict, total=False):
    all: Iterable[object]

    any: Iterable[object]


class ScheduleRuleJitter(TypedDict, total=False):
    """Optional per-occurrence random window around the nominal schedule time"""

    after_minutes: Annotated[int, PropertyInfo(alias="afterMinutes")]

    before_minutes: Annotated[int, PropertyInfo(alias="beforeMinutes")]


class ScheduleRule(TypedDict, total=False):
    type: Required[Literal["once", "cron", "recurring"]]

    date_time: Annotated[str, PropertyInfo(alias="dateTime")]
    """ISO 8601 datetime (for type=once)"""

    expression: str
    """Cron expression (for type=cron)"""

    jitter: ScheduleRuleJitter
    """Optional per-occurrence random window around the nominal schedule time"""

    rrule: str
    """RRULE string (for type=recurring)"""
