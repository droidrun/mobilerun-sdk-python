# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CountryListParams"]


class CountryListParams(TypedDict, total=False):
    page: int
    """Page number (1-based)."""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Number of items per page."""

    type: Literal["residential"]
    """Filter to countries offering this proxy type."""
