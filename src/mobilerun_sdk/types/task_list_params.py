# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from typing import Optional

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

    status: Optional[Literal["queued", "created", "running", "cancelling", "completed", "failed", "cancelled"]]