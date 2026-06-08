# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FlowListParams"]


class FlowListParams(TypedDict, total=False):
    enabled: Optional[bool]

    order_by: Annotated[Literal["name", "createdAt", "updatedAt"], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    search: str

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]
