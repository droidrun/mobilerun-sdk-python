# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RequestListParams"]


class RequestListParams(TypedDict, total=False):
    before: str
    """Opaque nextCursor from the previous page."""

    limit: int
    """Maximum number of requests to return (1–100; default 50)."""
