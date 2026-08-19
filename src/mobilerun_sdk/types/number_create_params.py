# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Annotated

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

    purpose: str
    """Optional Mobilerun Phone purpose slug from GET /numbers/purposes."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
    """Optional request idempotency key."""