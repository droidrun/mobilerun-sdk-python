# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowDryRunResponse", "Data", "DataAction", "DataGates", "DataValidation", "DataValidationError"]


class DataAction(BaseModel):
    continue_on_error: bool = FieldInfo(alias="continueOnError")

    method: str

    name: str

    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"]

    children: Optional[List[object]] = None
    """
    Nested child actions (loop/branch bodies), each the same shape as a
    ResolvedAction.
    """

    params: Optional[Dict[str, object]] = None


class DataGates(BaseModel):
    blocked: bool

    cooldown_active: Optional[bool] = FieldInfo(alias="cooldownActive", default=None)

    device_attached: bool = FieldInfo(alias="deviceAttached")

    device_ids: List[str] = FieldInfo(alias="deviceIds")

    enabled: bool


class DataValidationError(BaseModel):
    field: str

    message: str


class DataValidation(BaseModel):
    valid: bool

    errors: Optional[List[DataValidationError]] = None


class Data(BaseModel):
    actions: List[DataAction]

    activation: Literal["event", "schedule", "custom"]

    conditions_passed: Optional[bool] = FieldInfo(alias="conditionsPassed", default=None)

    gates: DataGates

    next_fire_time: Optional[str] = FieldInfo(alias="nextFireTime", default=None)

    rate_limited: bool = FieldInfo(alias="rateLimited")

    validation: DataValidation

    would_fire: bool = FieldInfo(alias="wouldFire")


class FlowDryRunResponse(BaseModel):
    data: Data
