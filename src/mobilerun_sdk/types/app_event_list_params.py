# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from .._utils import PropertyInfo

from typing import Optional

__all__ = ["AppEventListParams"]

class AppEventListParams(TypedDict, total=False):
    device_id: Annotated[str, PropertyInfo(alias="deviceId")]

    event_type: Annotated[str, PropertyInfo(alias="eventType")]

    from_: Annotated[Optional[str], PropertyInfo(alias="from")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    source: Literal["app", "system", "device", "webhook"]

    to: Optional[str]