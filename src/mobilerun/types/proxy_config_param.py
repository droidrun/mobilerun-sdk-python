# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProxyConfigParam", "Socks5"]


class Socks5(TypedDict, total=False):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class ProxyConfigParam(TypedDict, total=False):
    name: str

    smart_ip: Annotated[bool, PropertyInfo(alias="smartIp")]

    socks5: Socks5

    wireguard: str
