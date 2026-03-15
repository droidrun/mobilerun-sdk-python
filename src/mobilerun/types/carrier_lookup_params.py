# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CarrierLookupParams"]


class CarrierLookupParams(TypedDict, total=False):
    mcc: Required[str]
    """Mobile Country Code"""

    mnc: Required[str]
    """Mobile Network Code"""
