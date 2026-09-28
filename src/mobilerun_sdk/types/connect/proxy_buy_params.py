# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProxyBuyParams"]


class ProxyBuyParams(TypedDict, total=False):
    country: Required[str]
    """ISO 3166-1 alpha-2 country code to provision the proxy in."""

    type: Required[Literal["dedicated_residential", "residential", "mobile"]]

    name: str
    """
    Display name for the proxy, up to 64 characters excluding surrounding
    whitespace, and containing no NUL. Omit it (or send only whitespace) to get a
    generated label built from the country, type, and id.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
