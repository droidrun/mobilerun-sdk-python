# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from ..._utils import PropertyInfo

__all__ = ["AppListParams"]

class AppListParams(TypedDict, total=False):
    category: str

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    query: str