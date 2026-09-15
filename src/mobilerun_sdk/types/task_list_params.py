# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    created_by: Annotated[Optional[str], PropertyInfo(alias="createdBy")]
    """Only tasks created by this user id."""

    mine: bool
    """Only tasks created by the calling user."""

    order_by: Annotated[Optional[Literal["id", "createdAt", "finishedAt", "status"]], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    query: Optional[str]
    """Search in task description."""

    source: Optional[Literal["api", "agent"]]
    """Only tasks created via the API ('api') or spawned by an agent step ('agent')."""

    status: Optional[
        Literal["prepared", "queued", "created", "running", "cancelling", "completed", "failed", "cancelled"]
    ]
