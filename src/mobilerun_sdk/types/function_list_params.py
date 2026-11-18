# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionListParams"]


class FunctionListParams(TypedDict, total=False):
    latest: Literal["true", "false"]
    """
    Return one row per function name: its newest upload (any status), with
    versionCount. Combined with name, returns that single row.
    """

    name: str
    """Exact function name. Returns every active version of that name, newest first."""

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    search: str
    """Case-insensitive substring match against the function name."""
