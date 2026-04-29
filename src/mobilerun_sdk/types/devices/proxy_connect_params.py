# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProxyConnectParams", "Socks5"]


class ProxyConnectParams(TypedDict, total=False):
    host: str

    name: str
    """Proxy name"""

    password: str

    port: int

    smart_ip: Annotated[bool, PropertyInfo(alias="smartIp")]

    socks5: Socks5
    """SOCKS5 proxy configuration (required for socks5)."""

    user: str

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]


class Socks5(TypedDict, total=False):
    """SOCKS5 proxy configuration (required for socks5)."""

    host: Required[str]

    port: Required[int]

    password: str

    user: str
