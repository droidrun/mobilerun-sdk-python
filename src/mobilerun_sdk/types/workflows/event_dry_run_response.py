# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..flow import Flow
from ..._models import BaseModel

__all__ = [
    "EventDryRunResponse",
    "Data",
    "DataMatchedFlow",
    "DataMatchedFlowAction",
    "DataMatchedFlowGates",
    "DataMatchedFlowTrigger",
    "DataMatchedFlowTriggerScheduleRule",
    "DataValidation",
    "DataValidationError",
]


class DataMatchedFlowAction(BaseModel):
    continue_on_error: bool = FieldInfo(alias="continueOnError")

    method: str

    name: str

    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"]

    children: Optional[List[Optional[object]]] = None
    """
    Nested child actions (loop/branch bodies), each the same shape as a
    ResolvedAction.
    """

    params: Optional[Dict[str, Optional[object]]] = None


class DataMatchedFlowGates(BaseModel):
    blocked: bool

    cooldown_active: Optional[bool] = FieldInfo(alias="cooldownActive", default=None)

    device_attached: bool = FieldInfo(alias="deviceAttached")

    device_ids: List[str] = FieldInfo(alias="deviceIds")

    enabled: bool


class DataMatchedFlowTriggerScheduleRule(BaseModel):
    type: Literal["once", "cron", "recurring"]

    date_time: Optional[str] = FieldInfo(alias="dateTime", default=None)
    """ISO 8601 datetime (for type=once)"""

    expression: Optional[str] = None
    """Cron expression (for type=cron)"""

    rrule: Optional[str] = None
    """RRULE string (for type=recurring)"""


class DataMatchedFlowTrigger(BaseModel):
    id: str

    activation: Literal["event", "schedule", "custom"]

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    custom_payload_schema: Optional[Dict[str, object]] = FieldInfo(alias="customPayloadSchema", default=None)

    description: Optional[str] = None

    event_type: Optional[str] = FieldInfo(alias="eventType", default=None)

    name: str

    schedule_rule: Optional[DataMatchedFlowTriggerScheduleRule] = FieldInfo(alias="scheduleRule", default=None)

    timezone: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")

    conditions: Optional[object] = None

    next_fire_time: Optional[str] = FieldInfo(alias="nextFireTime", default=None)


class DataMatchedFlow(BaseModel):
    actions: List[DataMatchedFlowAction]

    flow: Flow

    gates: DataMatchedFlowGates

    trigger: DataMatchedFlowTrigger

    would_fire: bool = FieldInfo(alias="wouldFire")


class DataValidationError(BaseModel):
    field: str

    message: str


class DataValidation(BaseModel):
    valid: bool

    errors: Optional[List[DataValidationError]] = None


class Data(BaseModel):
    matched_flows: List[DataMatchedFlow] = FieldInfo(alias="matchedFlows")

    validation: DataValidation


class EventDryRunResponse(BaseModel):
    data: Data
