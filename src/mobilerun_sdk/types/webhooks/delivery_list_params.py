# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DeliveryListParams"]


class DeliveryListParams(TypedDict, total=False):
    event_id: Annotated[str, PropertyInfo(alias="eventId")]
    """Exact text match against the originating event id."""

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    status: Literal["pending", "success", "skipped", "dead"]
