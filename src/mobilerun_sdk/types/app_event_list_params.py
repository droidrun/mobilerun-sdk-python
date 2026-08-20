# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AppEventListParams"]


class AppEventListParams(TypedDict, total=False):
    device_id: Annotated[str, PropertyInfo(alias="deviceId")]

    event_type: Annotated[str, PropertyInfo(alias="eventType")]

    from_: Annotated[Optional[str], PropertyInfo(alias="from")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    source: Literal["app", "system", "device", "webhook"]

    to: Optional[str]
