# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExecutionListParams"]


class ExecutionListParams(TypedDict, total=False):
    flow_id: Annotated[str, PropertyInfo(alias="flowId")]

    from_: Annotated[Union[str, datetime, None], PropertyInfo(alias="from", format="iso8601")]

    invocation_id: Annotated[str, PropertyInfo(alias="invocationId")]

    order_by: Annotated[Literal["startedAt", "finishedAt", "status"], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    search: str

    status: Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"]

    to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]
