# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProxyBuyParams"]


class ProxyBuyParams(TypedDict, total=False):
    country: Required[str]
    """ISO 3166-1 alpha-2 country code to provision the proxy in."""

    type: Literal["dedicated_residential", "residential", "mobile"]
