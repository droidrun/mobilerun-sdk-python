# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from pydantic import Field as FieldInfo

from typing_extensions import Literal

from typing import List

__all__ = ["ProxyListResponse", "Item", "Pagination"]

class Item(BaseModel):
    """A provisioned proxy without its credentials."""
    id: str

    country: str
    """ISO 3166-1 alpha-2 country code (lowercase)."""

    created_at: datetime = FieldInfo(alias = "createdAt")

    host: str

    port: int

    status: Literal["pending_payment", "provisioning", "active", "cancelling", "ended", "error"]
    """Lifecycle of a proxy.

    A freshly created proxy is `provisioning` — or `pending_payment` until the
    customer completes checkout — and becomes `active` once its upstream is
    assigned. `cancelling` retains full access through the paid period; when the
    subscription expires the proxy is `ended`. `error` marks a failed provisioning
    attempt.
    """

    type: Literal["dedicated_residential", "residential", "mobile"]

    username: str

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

class ProxyListResponse(BaseModel):
    """A page of proxies."""
    items: List[Item]

    pagination: Pagination
    """Pagination metadata for a list response."""