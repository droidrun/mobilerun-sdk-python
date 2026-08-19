# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from .._utils import PropertyInfo

__all__ = ["EsimCreateParams"]

class EsimCreateParams(TypedDict, total=False):
    idempotency_key: Annotated[str, PropertyInfo(alias="idempotencyKey")]
    """
    Client-supplied key; replaying the same key returns the original purchase
    instead of buying again
    """