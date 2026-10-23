# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FlowCapacityParams"]


class FlowCapacityParams(TypedDict, total=False):
    agent_id: Annotated[Union[str, Literal["unassigned"]], PropertyInfo(alias="agentId")]
    """Agent bucket UUID or unassigned.

    Omit on list to include every bucket; omit on capacity for unassigned.
    """
