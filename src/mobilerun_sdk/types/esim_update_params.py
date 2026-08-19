# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional

__all__ = ["EsimUpdateParams"]

class EsimUpdateParams(TypedDict, total=False):
    msisdn: Optional[str]
    """Self-reported E.164 MSISDN for this eSIM's line.

    Omit to leave unchanged; null/empty clears it. An unverified label — never used
    for routing.
    """

    name: Optional[str]
    """
    User-defined display label — NFC-normalized, up to 15 GRAPHEMES (not UTF-16 code
    units; an emoji/flag may span several). Omit to leave unchanged;
    null/empty/whitespace-only clears it.
    """