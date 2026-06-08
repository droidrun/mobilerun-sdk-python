# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CatalogListParams"]


class CatalogListParams(TypedDict, total=False):
    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    source: Literal["device", "system", "webhook"]
