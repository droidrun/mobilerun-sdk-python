# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationHistoryParams"]


class ConversationHistoryParams(TypedDict, total=False):
    before: str
    """Any real row in this session; its containing turn is excluded."""

    limit: int
