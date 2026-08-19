# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from ..._utils import PropertyInfo

__all__ = ["UserCreateParams"]

class UserCreateParams(TypedDict, total=False):
    password: str
    """Desired SOCKS5 password, 1-255 bytes (RFC 1929). Generated when omitted."""

    proxy_id: Annotated[str, PropertyInfo(alias="proxyId")]
    """Proxy to bind the user to for dedicated routing."""

    username: str
    """Desired SOCKS5 username, 1-255 bytes (RFC 1929). Generated when omitted."""