# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DeviceListParams"]


class DeviceListParams(TypedDict, total=False):
    country: str

    name: str

    order_by: Annotated[Literal["id", "createdAt", "updatedAt", "assignedAt"], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    provider_id: Annotated[str, PropertyInfo(alias="providerId")]

    state: Optional[
        List[Literal["creating", "assigned", "ready", "rebooting", "migrating", "terminated", "maintenance", "unknown"]]
    ]

    type: Literal[
        "dedicated_physical_device", "dedicated_premium_device", "dedicated_emulated_device", "dedicated_ios_device"
    ]
