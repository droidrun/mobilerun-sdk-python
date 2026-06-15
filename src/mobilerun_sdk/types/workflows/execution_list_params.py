# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExecutionListParams"]


class ExecutionListParams(TypedDict, total=False):
    flow_id: Annotated[str, PropertyInfo(alias="flowId")]

    from_: Annotated[Optional[str], PropertyInfo(alias="from")]

    order_by: Annotated[Literal["startedAt", "finishedAt", "status"], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    search: str

    status: Literal["pending", "running", "success", "failed"]

    to: Optional[str]

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]
