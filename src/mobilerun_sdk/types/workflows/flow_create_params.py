# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .flow_action_overrides_param import FlowActionOverridesParam
from .flow_child_action_input_param import FlowChildActionInputParam

__all__ = ["FlowCreateParams", "Action"]


class FlowCreateParams(TypedDict, total=False):
    actions: Required[Iterable[Action]]

    name: Required[str]

    trigger_id: Required[Annotated[str, PropertyInfo(alias="triggerId")]]

    cooldown_scope: Annotated[Literal["flow", "device"], PropertyInfo(alias="cooldownScope")]

    cooldown_seconds: Annotated[Optional[int], PropertyInfo(alias="cooldownSeconds")]

    description: str

    enabled: bool


class Action(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    position: Required[int]

    children: Iterable[FlowChildActionInputParam]

    continue_on_error: Annotated[bool, PropertyInfo(alias="continueOnError")]

    device_id: Annotated[str, PropertyInfo(alias="deviceId")]

    name_override: Annotated[str, PropertyInfo(alias="nameOverride")]

    overrides: Optional[FlowActionOverridesParam]
