# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from ..._utils import PropertyInfo

__all__ = ["UserListParams"]

class UserListParams(TypedDict, total=False):
    page: int
    """Page number (1-based)."""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Number of items per page."""

    proxy_id: Annotated[str, PropertyInfo(alias="proxyId")]
    """Filter to users bound to this proxy.

    Users not bound to it (including unbound users) are excluded.
    """