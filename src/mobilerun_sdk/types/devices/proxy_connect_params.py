# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from ..._utils import PropertyInfo

__all__ = ["ProxyConnectParams", "Connect", "Socks5"]

class ProxyConnectParams(TypedDict, total=False):
    connect: Connect
    """
    Mobilerun Connect proxy — pass exactly one of id (use an existing proxy's
    credentials) or country (provision or reuse a rotating residential proxy for the
    device).
    """

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

class Connect(TypedDict, total=False):
    """
    Mobilerun Connect proxy — pass exactly one of id (use an existing proxy's credentials) or country (provision or reuse a rotating residential proxy for the device).
    """
    id: str
    """Existing Mobilerun Connect proxy id; its credentials are fetched server-side."""

    country: str
    """
    ISO 3166-1 alpha-2 country code; provisions (or reuses) a rotating residential
    Mobilerun Connect proxy for the device.
    """

class Socks5(TypedDict, total=False):
    """SOCKS5 proxy configuration (required for socks5)."""
    host: Required[str]

    port: Required[int]

    password: str

    user: str