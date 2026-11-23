# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FlowDryRunResponse",
    "Data",
    "DataAction",
    "DataGates",
    "DataTestRun",
    "DataTestRunBlocker",
    "DataValidation",
    "DataValidationError",
]


class DataAction(BaseModel):
    continue_on_error: bool = FieldInfo(alias="continueOnError")

    flow_action_id: str = FieldInfo(alias="flowActionId")

    key: str

    method: str
    """Deprecated: use uses."""

    name: str

    recording_enabled: bool = FieldInfo(alias="recordingEnabled")

    service: Literal[
        "tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api", "triggers_api", "sandbox_api"
    ]
    """Deprecated: use uses."""

    uses: Optional[str] = None
    """Authored step name; null when this step has no name.

    Includes hidden executable steps.
    """

    children: Optional[List[object]] = None
    """
    Nested child actions (loop/branch bodies), each the same shape as a
    ResolvedAction, including nullable uses and deprecated service/method.
    """

    params: Optional[Dict[str, object]] = None


class DataGates(BaseModel):
    blocked: bool

    cooldown_active: Optional[bool] = FieldInfo(alias="cooldownActive", default=None)

    device_attached: bool = FieldInfo(alias="deviceAttached")

    device_ids: List[str] = FieldInfo(alias="deviceIds")

    enabled: bool


class DataTestRunBlocker(BaseModel):
    code: Literal["validation", "conditions_not_met", "no_device", "rate_limited", "deploy_in_progress"]
    """
    Blocking reason: invalid payload, failed conditions, required device absent,
    account rate limit reached, or a deployment of the flow in progress,
    respectively.
    """

    field: Optional[str] = None
    """Validation error field path, in the same format as validation.errors[].field."""


class DataTestRun(BaseModel):
    blockers: List[DataTestRunBlocker]
    """Reasons a manual test cannot start; empty when ready is true."""

    missing_inputs: List[str] = FieldInfo(alias="missingInputs")
    """
    Absent required or referenced input paths to supply at test time; empty for
    stored schedule inputs.
    """

    ready: bool
    """
    Whether verification can start, allowing paused or blocked flows and inputs
    supplied at test time.
    """


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

    test_run: DataTestRun = FieldInfo(alias="testRun")

    validation: DataValidation

    would_fire: bool = FieldInfo(alias="wouldFire")


class FlowDryRunResponse(BaseModel):
    data: Data
