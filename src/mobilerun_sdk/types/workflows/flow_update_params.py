# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["FlowUpdateParams"]


class FlowUpdateParams(TypedDict, total=False):
    cooldown_scope: Annotated[Literal["flow", "device"], PropertyInfo(alias="cooldownScope")]

    cooldown_seconds: Annotated[Optional[int], PropertyInfo(alias="cooldownSeconds")]

    description: str

    device_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="deviceIds")]

    enabled: bool

    health_monitoring_enabled: Annotated[bool, PropertyInfo(alias="healthMonitoringEnabled")]

    name: str

    notify_on_failure: Annotated[bool, PropertyInfo(alias="notifyOnFailure")]

    notify_on_success: Annotated[bool, PropertyInfo(alias="notifyOnSuccess")]

    notify_webhook_id: Annotated[Optional[str], PropertyInfo(alias="notifyWebhookId")]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]

    self_healing_enabled: Annotated[bool, PropertyInfo(alias="selfHealingEnabled")]

    self_healing_max_attempts: Annotated[int, PropertyInfo(alias="selfHealingMaxAttempts")]

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]
