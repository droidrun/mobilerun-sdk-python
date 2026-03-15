# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProxyConnectParams", "Proxy"]


class ProxyConnectParams(TypedDict, total=False):
    host: str

    password: str

    port: int

    proxy: Proxy
    """Preferred new format."""

    smart_ip: Annotated[bool, PropertyInfo(alias="smartIp")]

    user: str

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]


class Proxy(TypedDict, total=False):
    """Preferred new format."""

    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]
