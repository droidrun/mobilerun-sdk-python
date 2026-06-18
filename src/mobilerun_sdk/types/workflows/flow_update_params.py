# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FlowUpdateParams"]


class FlowUpdateParams(TypedDict, total=False):
    cooldown_scope: Annotated[Literal["flow", "device"], PropertyInfo(alias="cooldownScope")]

    cooldown_seconds: Annotated[Optional[int], PropertyInfo(alias="cooldownSeconds")]

    description: str

    enabled: bool

    name: str

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]
