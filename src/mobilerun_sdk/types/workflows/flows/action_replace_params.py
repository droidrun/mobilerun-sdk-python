# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Iterable, Optional, Dict

from ...._utils import PropertyInfo

__all__ = ["ActionReplaceParams", "Action", "ActionChild", "ActionChildOverrides", "ActionOverrides"]

class ActionReplaceParams(TypedDict, total=False):
    actions: Required[Iterable[Action]]

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