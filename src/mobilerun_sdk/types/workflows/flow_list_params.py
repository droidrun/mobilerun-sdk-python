# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FlowListParams"]


class FlowListParams(TypedDict, total=False):
    agent_id: Annotated[Union[str, Literal["unassigned"]], PropertyInfo(alias="agentId")]
    """Agent bucket UUID or unassigned.

    Omit on list to include every bucket; omit on capacity for unassigned.
    """

    created_by: Annotated[str, PropertyInfo(alias="createdBy")]

    enabled: Literal["true", "false"]
    """Only include flows with this enabled state."""

    mine: Literal["true", "false"]
    """Only include flows created by you."""

    order_by: Annotated[Literal["name", "createdAt", "updatedAt"], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    search: str

    status: List[Literal["healthy", "failing", "blocked"]]

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]
