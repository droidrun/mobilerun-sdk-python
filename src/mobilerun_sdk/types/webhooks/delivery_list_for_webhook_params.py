# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from ..._utils import PropertyInfo

__all__ = ["DeliveryListForWebhookParams"]

class DeliveryListForWebhookParams(TypedDict, total=False):
    event_id: Annotated[str, PropertyInfo(alias="eventId")]
    """Exact text match against the originating event id."""

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]