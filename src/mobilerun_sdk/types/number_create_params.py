# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NumberCreateParams"]


class NumberCreateParams(TypedDict, total=False):
    billing_preference: Annotated[Literal["included", "included_only", "rent"], PropertyInfo(alias="billingPreference")]
    """
    Use included capacity when available, require included capacity without paid
    fallback (included_only), or start a paid checkout (rent).
    """

    country: str
    """Optional ISO 3166-1 alpha-2 country code from GET /numbers/phones/countries.

    Cannot be combined with `purpose`.
    """

    label: Optional[str]
    """
    User-defined display label — NFC-normalized, up to 100 GRAPHEMES (not UTF-16
    code units; an emoji/flag may span several). Display-only, never used for
    routing. Also seeds the billing entity name at purchase.
    """

    purpose: str
    """Optional purpose from GET /numbers/phones/purposes."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
    """Optional request idempotency key."""
