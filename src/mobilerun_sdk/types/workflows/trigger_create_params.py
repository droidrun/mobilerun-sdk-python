# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TriggerCreateParams", "Conditions", "ScheduleRule", "ScheduleRuleJitter"]


class TriggerCreateParams(TypedDict, total=False):
    activation: Required[Literal["event", "schedule", "custom"]]

    name: Required[str]

    conditions: Conditions

    custom_payload_schema: Annotated[Dict[str, object], PropertyInfo(alias="customPayloadSchema")]
    """Optional JSON Schema for validating payloads sent to this custom trigger"""

    description: str

    event_type: Annotated[str, PropertyInfo(alias="eventType")]

    schedule_rule: Annotated[ScheduleRule, PropertyInfo(alias="scheduleRule")]

    timezone: str


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
