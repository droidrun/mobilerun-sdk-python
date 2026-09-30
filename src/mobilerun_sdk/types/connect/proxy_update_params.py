# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProxyUpdateParams"]


class ProxyUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """
    New display name, up to 64 characters excluding surrounding whitespace, and
    containing no NUL. Send null (or an empty/whitespace-only string) to drop a
    custom name and go back to the generated label. Omit to leave the name
    unchanged.
    """
