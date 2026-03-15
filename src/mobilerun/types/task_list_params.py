# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .task_status import TaskStatus

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    order_by: Annotated[Optional[Literal["id", "createdAt", "finishedAt", "status"]], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    query: Optional[str]
    """Search in task description."""

    status: Optional[TaskStatus]
