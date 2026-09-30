# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ActionAddParams", "Child", "ChildOverrides", "Overrides"]


class ActionAddParams(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    position: Required[int]

    children: Iterable[Child]

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

    overrides: Optional[Overrides]

    parent_flow_action_id: Annotated[Optional[str], PropertyInfo(alias="parentFlowActionId")]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]


class ChildOverrides(TypedDict, total=False):
    params: Dict[str, object]


class Child(TypedDict, total=False):
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

    overrides: Optional[ChildOverrides]

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]


class Overrides(TypedDict, total=False):
    params: Dict[str, object]
