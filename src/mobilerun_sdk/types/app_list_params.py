# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Annotated

from .._utils import PropertyInfo

__all__ = ["AppListParams"]

class AppListParams(TypedDict, total=False):
    order: Literal["asc", "desc"]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    platform: Literal["all", "android", "ios"]

    query: str

    sort_by: Annotated[Literal["createdAt", "name"], PropertyInfo(alias="sortBy")]

    status: Literal["all", "queued", "available", "failed"]