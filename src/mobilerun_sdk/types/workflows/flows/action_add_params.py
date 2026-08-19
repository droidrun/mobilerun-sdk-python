# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from ...._utils import PropertyInfo

from typing import Iterable, Optional, Dict

__all__ = ["ActionAddParams", "Child", "ChildOverrides", "Overrides"]

class ActionAddParams(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    position: Required[int]

    children: Iterable[Child]

    continue_on_error: Annotated[bool, PropertyInfo(alias="continueOnError")]

    name_override: Annotated[str, PropertyInfo(alias="nameOverride")]

    overrides: Optional[Overrides]

    parent_flow_action_id: Annotated[Optional[str], PropertyInfo(alias="parentFlowActionId")]

class ChildOverrides(TypedDict, total=False):
    params: Dict[str, object]

class Child(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    position: Required[int]

    continue_on_error: Annotated[bool, PropertyInfo(alias="continueOnError")]

    name_override: Annotated[str, PropertyInfo(alias="nameOverride")]

    overrides: Optional[ChildOverrides]

class Overrides(TypedDict, total=False):
    params: Dict[str, object]