# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TriggerListParams"]


class TriggerListParams(TypedDict, total=False):
    activation: Literal["event", "schedule", "custom"]

    event_type: Annotated[str, PropertyInfo(alias="eventType")]

    order_by: Annotated[Literal["name", "createdAt", "updatedAt"], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    search: str
