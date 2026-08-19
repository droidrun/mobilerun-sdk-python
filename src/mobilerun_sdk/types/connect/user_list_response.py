# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from pydantic import Field as FieldInfo

from typing import Optional, List

__all__ = ["UserListResponse", "Item", "Pagination"]

class Item(BaseModel):
    """A SOCKS5 credential without its password."""
    id: str

    created_at: datetime = FieldInfo(alias = "createdAt")

    username: str

    proxy_id: Optional[str] = FieldInfo(alias = "proxyId", default = None)
    """The proxy this user routes to (dedicated routing), or null if unbound."""

class Pagination(BaseModel):
    """Pagination metadata for a list response."""
    has_next: bool = FieldInfo(alias = "hasNext")
    """Whether a next page exists."""

    has_prev: bool = FieldInfo(alias = "hasPrev")
    """Whether a previous page exists."""

    page: int
    """Current page number (1-based)."""

    pages: int
    """Total number of pages."""

    page_size: int = FieldInfo(alias = "pageSize")
    """Number of items per page."""

    total: int
    """Total number of items across all pages."""

class UserListResponse(BaseModel):
    """A page of SOCKS5 users."""
    items: List[Item]

    pagination: Pagination
    """Pagination metadata for a list response."""