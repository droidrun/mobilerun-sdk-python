# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ProxyUpdateParams", "UpdateSocks5Proxy", "UpdateWireguardProxy"]


class UpdateSocks5Proxy(TypedDict, total=False):
    host: Required[str]

    name: Required[str]

    password: Required[str]

    port: Required[int]

    protocol: Required[Literal["socks5"]]

    user: Required[str]


class UpdateWireguardProxy(TypedDict, total=False):
    config: Required[str]

    name: Required[str]

    protocol: Required[Literal["wireguard"]]


ProxyUpdateParams: TypeAlias = Union[UpdateSocks5Proxy, UpdateWireguardProxy]
