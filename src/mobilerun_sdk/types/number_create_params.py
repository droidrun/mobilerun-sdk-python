# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NumberCreateParams"]


class NumberCreateParams(TypedDict, total=False):
    billing_preference: Annotated[Literal["included", "rent"], PropertyInfo(alias="billingPreference")]
    """
    Prefer a free package seat ('included', default) or force the paid checkout
    ('rent')
    """

    country: str
    """Optional ISO 3166-1 alpha-2 country code from GET /numbers/countries.

    Cannot be combined with `purpose`.
    """

    label: Optional[str]
    """
    User-defined display label — NFC-normalized, up to 100 GRAPHEMES (not UTF-16
    code units; an emoji/flag may span several). Display-only, never used for
    routing. Also seeds the billing entity name at purchase.
    """

    purpose: str
    """Optional Mobilerun Phone purpose slug from GET /numbers/purposes."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
    """Optional request idempotency key."""
