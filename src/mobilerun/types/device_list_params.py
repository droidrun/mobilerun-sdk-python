# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DeviceListParams"]


class DeviceListParams(TypedDict, total=False):
    x_user_id: Required[Annotated[str, PropertyInfo(alias="X-User-ID")]]

    country: str

    order_by: Annotated[Literal["id", "createdAt", "updatedAt", "assignedAt"], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    state: Literal["creating", "assigned", "ready", "terminated", "unknown"]
