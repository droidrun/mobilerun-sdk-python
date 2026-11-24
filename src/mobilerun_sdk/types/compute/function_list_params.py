# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FunctionListParams"]


class FunctionListParams(TypedDict, total=False):
    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    search: str
    """Case-insensitive substring match against the function name."""
