# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from typing import Iterable, Optional, Dict

from ..._utils import PropertyInfo

from ..._types import SequenceNotStr

__all__ = ["FlowCreateParams", "Action", "ActionChild", "ActionChildOverrides", "ActionOverrides"]

class FlowCreateParams(TypedDict, total=False):
    actions: Required[Iterable[Action]]

    name: Required[str]

    trigger_id: Required[Annotated[str, PropertyInfo(alias="triggerId")]]

    cooldown_scope: Annotated[Literal["flow", "device"], PropertyInfo(alias="cooldownScope")]

    cooldown_seconds: Annotated[Optional[int], PropertyInfo(alias="cooldownSeconds")]

    description: str

    device_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="deviceIds")]

    enabled: bool

    health_monitoring_enabled: Annotated[bool, PropertyInfo(alias="healthMonitoringEnabled")]

    notify_on_failure: Annotated[bool, PropertyInfo(alias="notifyOnFailure")]

    notify_on_success: Annotated[bool, PropertyInfo(alias="notifyOnSuccess")]

    notify_webhook_id: Annotated[Optional[str], PropertyInfo(alias="notifyWebhookId")]

    self_healing_enabled: Annotated[bool, PropertyInfo(alias="selfHealingEnabled")]

    self_healing_max_attempts: Annotated[int, PropertyInfo(alias="selfHealingMaxAttempts")]

class ActionChildOverrides(TypedDict, total=False):
    params: Dict[str, object]

class ActionChild(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    position: Required[int]

    continue_on_error: Annotated[bool, PropertyInfo(alias="continueOnError")]

    name_override: Annotated[str, PropertyInfo(alias="nameOverride")]

    overrides: Optional[ActionChildOverrides]

class ActionOverrides(TypedDict, total=False):
    params: Dict[str, object]

class Action(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    position: Required[int]

    children: Iterable[ActionChild]

    continue_on_error: Annotated[bool, PropertyInfo(alias="continueOnError")]

    name_override: Annotated[str, PropertyInfo(alias="nameOverride")]

    overrides: Optional[ActionOverrides]