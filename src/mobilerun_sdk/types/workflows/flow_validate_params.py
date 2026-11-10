# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "FlowValidateParams",
    "Variant0",
    "Variant0Action",
    "Variant0ActionFlowActionInput",
    "Variant0ActionFlowActionInputChild",
    "Variant0ActionFlowActionInputChildOverrides",
    "Variant0ActionFlowActionInputOverrides",
    "Variant0ActionFlowDraftActionInput",
    "Variant0ActionFlowDraftActionInputDraft",
    "Variant0ActionFlowDraftActionInputOverrides",
    "Variant0Delivery",
    "Variant0DeliveryRecording",
    "Variant0RecordingPolicy",
    "Variant1",
    "Variant1Draft",
    "Variant1DraftAction",
    "Variant1DraftFlow",
    "Variant1DraftFlowDelivery",
    "Variant1DraftFlowDeliveryRecording",
    "Variant1DraftFlowRecordingPolicy",
    "Variant1Contract",
    "Variant1ContractMeta",
    "Variant1ContractMetaFlow",
    "Variant1ContractMetaSink",
    "Variant1ContractMetaTrigger",
    "Variant1ContractMetaTriggerScheduleRule",
    "Variant1ContractMetaTriggerScheduleRuleJitter",
    "Variant1ContractMetaCloudAction",
    "Variant1Verify",
]


class Variant0(TypedDict, total=False):
    actions: Required[Iterable[Variant0Action]]

    name: Required[str]

    cooldown_scope: Annotated[Literal["flow", "device"], PropertyInfo(alias="cooldownScope")]

    cooldown_seconds: Annotated[Optional[int], PropertyInfo(alias="cooldownSeconds")]

    delivery: Variant0Delivery

    description: str

    device_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="deviceIds")]

    enabled: bool

    health_monitoring_enabled: Annotated[bool, PropertyInfo(alias="healthMonitoringEnabled")]

    notify_on_failure: Annotated[bool, PropertyInfo(alias="notifyOnFailure")]

    notify_on_success: Annotated[bool, PropertyInfo(alias="notifyOnSuccess")]

    notify_webhook_id: Annotated[Optional[str], PropertyInfo(alias="notifyWebhookId")]

    owner_wake: Annotated[Literal["final", "off"], PropertyInfo(alias="ownerWake")]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]

    recording_policy: Annotated[Variant0RecordingPolicy, PropertyInfo(alias="recordingPolicy")]

    self_healing_enabled: Annotated[bool, PropertyInfo(alias="selfHealingEnabled")]

    self_healing_max_attempts: Annotated[int, PropertyInfo(alias="selfHealingMaxAttempts")]

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]


class Variant0ActionFlowActionInputChildOverrides(TypedDict, total=False):
    params: Dict[str, object]


class Variant0ActionFlowActionInputChild(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    position: Required[int]

    continue_on_error: Annotated[bool, PropertyInfo(alias="continueOnError")]

    key: str
    """
    Stable identifier used by template resolution v2+ to address this step as
    {{key.field}}. Omitted keys are derived from the step name whenever a flow is
    created. For template resolution v3, replacing an existing flow's full action
    tree requires every step to carry an explicit key — a missing key is rejected
    there, not derived, so a name change can never silently move a step's key.
    """

    name_override: Annotated[str, PropertyInfo(alias="nameOverride")]

    overrides: Optional[Variant0ActionFlowActionInputChildOverrides]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]


class Variant0ActionFlowActionInputOverrides(TypedDict, total=False):
    params: Dict[str, object]


class Variant0ActionFlowActionInput(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    position: Required[int]

    children: Iterable[Variant0ActionFlowActionInputChild]

    continue_on_error: Annotated[bool, PropertyInfo(alias="continueOnError")]

    key: str
    """
    Stable identifier used by template resolution v2+ to address this step as
    {{key.field}}. Omitted keys are derived from the step name whenever a flow is
    created. For template resolution v3, replacing an existing flow's full action
    tree requires every step to carry an explicit key — a missing key is rejected
    there, not derived, so a name change can never silently move a step's key.
    """

    name_override: Annotated[str, PropertyInfo(alias="nameOverride")]

    overrides: Optional[Variant0ActionFlowActionInputOverrides]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]


class Variant0ActionFlowDraftActionInputDraft(TypedDict, total=False):
    method: Required[str]

    name: Required[str]

    service: Required[str]

    params: Dict[str, object]


class Variant0ActionFlowDraftActionInputOverrides(TypedDict, total=False):
    params: Dict[str, object]


class Variant0ActionFlowDraftActionInput(TypedDict, total=False):
    draft: Required[Variant0ActionFlowDraftActionInputDraft]

    position: Required[int]

    continue_on_error: Annotated[bool, PropertyInfo(alias="continueOnError")]

    key: str
    """
    Stable identifier used by template resolution v2+ to address this step as
    {{key.field}}. Omitted keys are derived from the step name whenever a flow is
    created. For template resolution v3, replacing an existing flow's full action
    tree requires every step to carry an explicit key — a missing key is rejected
    there, not derived, so a name change can never silently move a step's key.
    """

    name_override: Annotated[str, PropertyInfo(alias="nameOverride")]

    overrides: Optional[Variant0ActionFlowDraftActionInputOverrides]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]


Variant0Action: TypeAlias = Union[Variant0ActionFlowActionInput, Variant0ActionFlowDraftActionInput]


class Variant0DeliveryRecording(TypedDict, total=False):
    filename: Required[str]


class Variant0Delivery(TypedDict, total=False):
    destination: Required[Literal["mobilerun", "one_drive", "google_drive"]]

    folder: str
    """Absolute destination folder; not allowed when destination is mobilerun.

    May contain {{meta.<name>}} (for example {{meta.shortDate}} = YYMMDD,
    {{meta.fileTime}} = HH-mm, in the trigger timezone) and
    {{event.payload.<field>}} placeholders, resolved once per run so every artifact
    of that run lands in the same folder. Each substituted value must be a single
    safe folder name (no "/", "\", "..", control characters); otherwise delivery
    fails with invalid_delivery_folder. With a placeholder folder, screenshots are
    delivered directly into the resolved folder; with a static folder they go into a
    per-run "<flow>-<timestamp>-<id>-screenshots" subfolder.
    """

    recording: Variant0DeliveryRecording

    screenshots: object


class Variant0RecordingPolicy(TypedDict, total=False):
    mode: Required[Literal["off", "flow", "selected_steps"]]


class Variant1(TypedDict, total=False):
    draft: Required[Variant1Draft]

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]

    contract: Variant1Contract

    verify: Variant1Verify


class Variant1DraftAction(TypedDict, total=False):
    catalog_entry_id: Required[Annotated[str, PropertyInfo(alias="catalogEntryId")]]

    name: Required[str]

    position: Required[int]

    role: Required[str]

    description: str

    params: Dict[str, object]


class Variant1DraftFlowDeliveryRecording(TypedDict, total=False):
    filename: Required[str]


class Variant1DraftFlowDelivery(TypedDict, total=False):
    destination: Required[Literal["mobilerun", "one_drive", "google_drive"]]

    folder: str
    """Absolute destination folder; not allowed when destination is mobilerun.

    May contain {{meta.<name>}} (for example {{meta.shortDate}} = YYMMDD,
    {{meta.fileTime}} = HH-mm, in the trigger timezone) and
    {{event.payload.<field>}} placeholders, resolved once per run so every artifact
    of that run lands in the same folder. Each substituted value must be a single
    safe folder name (no "/", "\", "..", control characters); otherwise delivery
    fails with invalid_delivery_folder. With a placeholder folder, screenshots are
    delivered directly into the resolved folder; with a static folder they go into a
    per-run "<flow>-<timestamp>-<id>-screenshots" subfolder.
    """

    recording: Variant1DraftFlowDeliveryRecording

    screenshots: object


class Variant1DraftFlowRecordingPolicy(TypedDict, total=False):
    mode: Required[Literal["off", "flow", "selected_steps"]]


class Variant1DraftFlow(TypedDict, total=False):
    cooldown_scope: Annotated[Literal["flow", "device"], PropertyInfo(alias="cooldownScope")]

    cooldown_seconds: Annotated[Optional[int], PropertyInfo(alias="cooldownSeconds")]

    delivery: Variant1DraftFlowDelivery

    description: str

    device_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="deviceIds")]

    execution_mode: Annotated[Literal["device", "cloud"], PropertyInfo(alias="executionMode")]

    health_monitoring_enabled: Annotated[bool, PropertyInfo(alias="healthMonitoringEnabled")]

    name: str

    recording_policy: Annotated[Variant1DraftFlowRecordingPolicy, PropertyInfo(alias="recordingPolicy")]

    self_healing_enabled: Annotated[bool, PropertyInfo(alias="selfHealingEnabled")]

    self_healing_max_attempts: Annotated[int, PropertyInfo(alias="selfHealingMaxAttempts")]


class Variant1Draft(TypedDict, total=False):
    actions: Required[Iterable[Variant1DraftAction]]

    flow: Required[Variant1DraftFlow]

    trigger: Required[Dict[str, object]]


class Variant1ContractMetaFlow(TypedDict, total=False):
    health_monitoring_enabled: Required[Annotated[bool, PropertyInfo(alias="healthMonitoringEnabled")]]

    self_healing_enabled: Required[Annotated[bool, PropertyInfo(alias="selfHealingEnabled")]]

    self_healing_max_attempts: Required[Annotated[int, PropertyInfo(alias="selfHealingMaxAttempts")]]

    recording_mode: Annotated[Literal["off", "flow", "selected_steps"], PropertyInfo(alias="recordingMode")]

    result_delivery: Annotated[Literal["none", "message", "wake"], PropertyInfo(alias="resultDelivery")]


class Variant1ContractMetaSink(TypedDict, total=False):
    type: Required[Literal["chat", "file", "webhook"]]

    endpoint_id: Annotated[Optional[str], PropertyInfo(alias="endpointId")]


class Variant1ContractMetaTriggerScheduleRuleJitter(TypedDict, total=False):
    """Optional per-occurrence random window around the nominal schedule time"""

    after_minutes: Annotated[int, PropertyInfo(alias="afterMinutes")]

    before_minutes: Annotated[int, PropertyInfo(alias="beforeMinutes")]


class Variant1ContractMetaTriggerScheduleRule(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    type: Required[Literal["once", "cron", "recurring"]]

    date_time: Annotated[str, PropertyInfo(alias="dateTime")]
    """ISO 8601 datetime (for type=once)"""

    expression: str
    """Cron expression (for type=cron)"""

    jitter: Variant1ContractMetaTriggerScheduleRuleJitter
    """Optional per-occurrence random window around the nominal schedule time"""

    rrule: str
    """RRULE string (for type=recurring)"""


class Variant1ContractMetaTrigger(TypedDict, total=False):
    activation: Required[Literal["event", "schedule", "custom"]]
    """Accepted for compatibility; derived from trigger.type with agent_routine."""

    cadence: Required[Optional[str]]

    event_type: Required[Annotated[Optional[str], PropertyInfo(alias="eventType")]]

    schedule_rule: Required[Annotated[Variant1ContractMetaTriggerScheduleRule, PropertyInfo(alias="scheduleRule")]]

    timezone: Required[Optional[str]]

    type: Required[Literal["schedule", "app_event", "device_event", "platform_event", "custom"]]


class Variant1ContractMetaCloudAction(TypedDict, total=False):
    method: Required[str]

    role: Required[str]


class Variant1ContractMeta(TypedDict, total=False):
    flow: Required[Variant1ContractMetaFlow]

    sink: Required[Variant1ContractMetaSink]

    timezone: Required[Optional[str]]

    trigger: Required[Variant1ContractMetaTrigger]

    verification: Required[Literal["rules", "agent_review", "rules_then_review", "none"]]

    cloud_actions: Annotated[Iterable[Variant1ContractMetaCloudAction], PropertyInfo(alias="cloudActions")]

    output_filename: Annotated[Optional[str], PropertyInfo(alias="outputFilename")]


class Variant1Contract(TypedDict, total=False):
    deliverable: Literal["none", "file", "chat", "integration"]
    """Required without profile.

    Ignored with agent_routine; derived from meta.sink.type.
    """

    integration_role: Annotated[str, PropertyInfo(alias="integrationRole")]
    """Ignored with agent_routine; derived from the action graph."""

    meta: Variant1ContractMeta

    producer_roles: Annotated[SequenceNotStr[str], PropertyInfo(alias="producerRoles")]
    """Ignored with agent_routine; derived from the action graph."""

    profile: Literal["agent_routine"]

    slug: str

    upload_role: Annotated[str, PropertyInfo(alias="uploadRole")]
    """Ignored with agent_routine; derived from the action graph."""


class Variant1Verify(TypedDict, total=False):
    device_id: Annotated[str, PropertyInfo(alias="deviceId")]

    payload: Dict[str, object]


FlowValidateParams: TypeAlias = Union[Variant0, Variant1]
