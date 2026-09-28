# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "EventDryRunResponse",
    "Data",
    "DataMatchedFlow",
    "DataMatchedFlowAction",
    "DataMatchedFlowFlow",
    "DataMatchedFlowFlowDelivery",
    "DataMatchedFlowFlowDeliveryRecording",
    "DataMatchedFlowFlowRecordingPolicy",
    "DataMatchedFlowGates",
    "DataMatchedFlowTrigger",
    "DataValidation",
    "DataValidationError",
]


class DataMatchedFlowAction(BaseModel):
    continue_on_error: bool = FieldInfo(alias="continueOnError")

    flow_action_id: str = FieldInfo(alias="flowActionId")

    method: str

    name: str

    recording_enabled: bool = FieldInfo(alias="recordingEnabled")

    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api"]

    children: Optional[List[object]] = None
    """
    Nested child actions (loop/branch bodies), each the same shape as a
    ResolvedAction.
    """

    params: Optional[Dict[str, object]] = None


class DataMatchedFlowFlowDeliveryRecording(BaseModel):
    filename: str


class DataMatchedFlowFlowDelivery(BaseModel):
    destination: Literal["one_drive", "google_drive"]

    folder: Optional[str] = None

    recording: Optional[DataMatchedFlowFlowDeliveryRecording] = None

    screenshots: Optional[object] = None


class DataMatchedFlowFlowRecordingPolicy(BaseModel):
    mode: Literal["off", "flow", "selected_steps"]


class DataMatchedFlowFlow(BaseModel):
    id: str

    archived_at: Optional[str] = FieldInfo(alias="archivedAt", default=None)

    blocked_at: Optional[str] = FieldInfo(alias="blockedAt", default=None)

    consecutive_failures: int = FieldInfo(alias="consecutiveFailures")

    cooldown_scope: Literal["flow", "device"] = FieldInfo(alias="cooldownScope")

    cooldown_seconds: Optional[int] = FieldInfo(alias="cooldownSeconds", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    delivery: Optional[DataMatchedFlowFlowDelivery] = None

    description: Optional[str] = None

    device_ids: List[str] = FieldInfo(alias="deviceIds")

    enabled: bool
    """
    Compatibility projection of lifecycleStatus; true only when lifecycleStatus is
    enabled.
    """

    health_monitoring_enabled: bool = FieldInfo(alias="healthMonitoringEnabled")

    last_failure_at: Optional[str] = FieldInfo(alias="lastFailureAt", default=None)

    last_failure_code: Optional[
        Literal["device_not_found", "permission_denied", "client_error", "transient", "logic", "invalid_config"]
    ] = FieldInfo(alias="lastFailureCode", default=None)

    last_triggered_at: Optional[str] = FieldInfo(alias="lastTriggeredAt", default=None)

    lifecycle_status: Literal["enabled", "disabled", "archived"] = FieldInfo(alias="lifecycleStatus")

    name: str

    notify_on_failure: bool = FieldInfo(alias="notifyOnFailure")

    notify_on_success: bool = FieldInfo(alias="notifyOnSuccess")

    notify_webhook_id: Optional[str] = FieldInfo(alias="notifyWebhookId", default=None)

    owner_id: str = FieldInfo(alias="ownerId")

    recording_enabled: bool = FieldInfo(alias="recordingEnabled")
    """
    Deprecated: use recordingPolicy.mode ("flow" = recordingEnabled=true, "off" =
    recordingEnabled=false).
    """

    recording_policy: DataMatchedFlowFlowRecordingPolicy = FieldInfo(alias="recordingPolicy")

    self_healing_enabled: bool = FieldInfo(alias="selfHealingEnabled")

    self_healing_max_attempts: int = FieldInfo(alias="selfHealingMaxAttempts")

    status: Literal["healthy", "failing", "blocked"]

    template_resolution_version: int = FieldInfo(alias="templateResolutionVersion")
    """Template-resolver semantics this flow runs under (MVA-23).

    1 = legacy (missing/forbidden/null all resolve to ''). 2 = typed
    (missing/forbidden throw, a whole-token null stays JSON null). Existing flows
    stay 1; new flows default to 2.
    """

    trigger_id: str = FieldInfo(alias="triggerId")

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")
    """Deprecated: use ownerId (tenancy) / createdBy (actor)."""


class DataMatchedFlowGates(BaseModel):
    blocked: bool

    cooldown_active: Optional[bool] = FieldInfo(alias="cooldownActive", default=None)

    device_attached: bool = FieldInfo(alias="deviceAttached")

    device_ids: List[str] = FieldInfo(alias="deviceIds")

    enabled: bool


class DataMatchedFlowTrigger(BaseModel):
    id: str

    activation: Literal["event", "schedule", "custom"]

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    custom_payload_schema: Optional[Dict[str, object]] = FieldInfo(alias="customPayloadSchema", default=None)

    description: Optional[str] = None

    event_type: Optional[str] = FieldInfo(alias="eventType", default=None)

    name: str

    owner_id: str = FieldInfo(alias="ownerId")

    schedule_rule: object = FieldInfo(alias="scheduleRule")

    timezone: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")
    """Deprecated: use ownerId (tenancy) / createdBy (actor)."""

    conditions: Optional[object] = None

    next_fire_time: Optional[str] = FieldInfo(alias="nextFireTime", default=None)


class DataMatchedFlow(BaseModel):
    actions: List[DataMatchedFlowAction]

    flow: DataMatchedFlowFlow

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
