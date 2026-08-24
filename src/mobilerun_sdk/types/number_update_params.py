# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["NumberUpdateParams"]


class NumberUpdateParams(TypedDict, total=False):
    label: Optional[str]
    """
    User-defined display label — NFC-normalized, up to 100 GRAPHEMES (not UTF-16
    code units; an emoji/flag may span several). Display-only, never used for
    routing. Also seeds the billing entity name at purchase.
    """
