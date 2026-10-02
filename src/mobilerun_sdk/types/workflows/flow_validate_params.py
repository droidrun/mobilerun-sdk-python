# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "FlowValidateParams",
    "Action",
    "ActionFlowActionInput",
    "ActionFlowActionInputChild",
    "ActionFlowActionInputChildOverrides",
    "ActionFlowActionInputOverrides",
    "ActionFlowDraftActionInput",
    "ActionFlowDraftActionInputDraft",
    "ActionFlowDraftActionInputOverrides",
    "Delivery",
    "DeliveryRecording",
    "RecordingPolicy",
]


class FlowValidateParams(TypedDict, total=False):
    actions: Required[Iterable[Action]]

    name: Required[str]

    cooldown_scope: Annotated[Literal["flow", "device"], PropertyInfo(alias="cooldownScope")]

    cooldown_seconds: Annotated[Optional[int], PropertyInfo(alias="cooldownSeconds")]

    delivery: Delivery

    description: str

    device_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="deviceIds")]

    enabled: bool

    health_monitoring_enabled: Annotated[bool, PropertyInfo(alias="healthMonitoringEnabled")]

    notify_on_failure: Annotated[bool, PropertyInfo(alias="notifyOnFailure")]

    notify_on_success: Annotated[bool, PropertyInfo(alias="notifyOnSuccess")]

    notify_webhook_id: Annotated[Optional[str], PropertyInfo(alias="notifyWebhookId")]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]

    recording_policy: Annotated[RecordingPolicy, PropertyInfo(alias="recordingPolicy")]

    self_healing_enabled: Annotated[bool, PropertyInfo(alias="selfHealingEnabled")]

    self_healing_max_attempts: Annotated[int, PropertyInfo(alias="selfHealingMaxAttempts")]

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]


class ActionFlowActionInputChildOverrides(TypedDict, total=False):
    params: Dict[str, object]


class ActionFlowActionInputChild(TypedDict, total=False):
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

    overrides: Optional[ActionFlowActionInputChildOverrides]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]


class ActionFlowActionInputOverrides(TypedDict, total=False):
    params: Dict[str, object]


class ActionFlowActionInput(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    position: Required[int]

    children: Iterable[ActionFlowActionInputChild]

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

    overrides: Optional[ActionFlowActionInputOverrides]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]


class ActionFlowDraftActionInputDraft(TypedDict, total=False):
    method: Required[str]

    name: Required[str]

    service: Required[str]

    params: Dict[str, object]


class ActionFlowDraftActionInputOverrides(TypedDict, total=False):
    params: Dict[str, object]


class ActionFlowDraftActionInput(TypedDict, total=False):
    draft: Required[ActionFlowDraftActionInputDraft]

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

    overrides: Optional[ActionFlowDraftActionInputOverrides]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]


Action: TypeAlias = Union[ActionFlowActionInput, ActionFlowDraftActionInput]


class DeliveryRecording(TypedDict, total=False):
    filename: Required[str]


class Delivery(TypedDict, total=False):
    destination: Required[Literal["mobilerun", "one_drive", "google_drive"]]

    folder: str
    """not allowed when destination is mobilerun"""

    recording: DeliveryRecording

    screenshots: object


class RecordingPolicy(TypedDict, total=False):
    mode: Required[Literal["off", "flow", "selected_steps"]]
