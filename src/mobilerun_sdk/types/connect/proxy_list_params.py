# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProxyListParams"]


class ProxyListParams(TypedDict, total=False):
    country: str
    """Filter to proxies in this country (ISO 3166-1 alpha-2, lowercase)."""

    page: int
    """Page number (1-based)."""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Number of items per page."""
