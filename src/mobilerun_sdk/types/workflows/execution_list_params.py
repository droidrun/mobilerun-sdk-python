# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from ..._utils import PropertyInfo

from typing import Optional

__all__ = ["ExecutionListParams"]

class ExecutionListParams(TypedDict, total=False):
    flow_id: Annotated[str, PropertyInfo(alias="flowId")]

    from_: Annotated[Optional[str], PropertyInfo(alias="from")]

    order_by: Annotated[Literal["startedAt", "finishedAt", "status"], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    search: str

    status: Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"]

    to: Optional[str]

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]