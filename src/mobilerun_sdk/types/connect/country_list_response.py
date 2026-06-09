# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CountryListResponse", "Item", "Pagination"]


class Item(BaseModel):
    code: str
    """ISO 3166-1 alpha-2 country code (lowercase)."""

    name: str

    proxy_types: List[Literal["residential"]] = FieldInfo(alias="proxyTypes")
    """Proxy types available to provision in this country."""


class Pagination(BaseModel):
    """Pagination metadata for a list response."""

    has_next: bool = FieldInfo(alias="hasNext")
    """Whether a next page exists."""

    has_prev: bool = FieldInfo(alias="hasPrev")
    """Whether a previous page exists."""

    page: int
    """Current page number (1-based)."""

    pages: int
    """Total number of pages."""

    page_size: int = FieldInfo(alias="pageSize")
    """Number of items per page."""

    total: int
    """Total number of items across all pages."""


class CountryListResponse(BaseModel):
    """A page of countries."""

    items: List[Item]

    pagination: Pagination
    """Pagination metadata for a list response."""
