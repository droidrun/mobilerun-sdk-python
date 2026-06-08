# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .flow_action_overrides_param import FlowActionOverridesParam

__all__ = ["FlowChildActionInputParam"]


class FlowChildActionInputParam(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    position: Required[int]

    continue_on_error: Annotated[bool, PropertyInfo(alias="continueOnError")]

    device_id: Annotated[str, PropertyInfo(alias="deviceId")]

    name_override: Annotated[str, PropertyInfo(alias="nameOverride")]

    overrides: Optional[FlowActionOverridesParam]
