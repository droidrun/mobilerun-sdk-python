# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NumberCapacityParams"]


class NumberCapacityParams(TypedDict, total=False):
    country: Required[str]
    """ISO 3166-1 alpha-2 country code from GET /numbers/phones/countries."""
