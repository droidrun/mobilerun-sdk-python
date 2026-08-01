# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProxyLookupParams", "Socks5"]


class ProxyLookupParams(TypedDict, total=False):
    socks5: Required[Socks5]
    """SOCKS5 proxy configuration."""


class Socks5(TypedDict, total=False):
    """SOCKS5 proxy configuration."""

    host: Required[str]

    port: Required[int]

    password: str

    user: str
