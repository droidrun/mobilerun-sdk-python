# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DeviceListParams"]


class DeviceListParams(TypedDict, total=False):
    country: str

    created_by: Annotated[str, PropertyInfo(alias="createdBy")]
    """Filter to devices created by this user id. Mutually exclusive with mine."""

    mine: bool
    """
    When true, only return devices created by the calling user (resolved from
    X-User-ID, never a client-supplied id).
    """

    name: str

    order_by: Annotated[Literal["id", "createdAt", "updatedAt", "assignedAt"], PropertyInfo(alias="orderBy")]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    provider_id: Annotated[str, PropertyInfo(alias="providerId")]

    state: Optional[
        List[
            Literal[
                "creating",
                "assigned",
                "ready",
                "rebooting",
                "migrating",
                "resetting",
                "terminated",
                "maintenance",
                "stopped",
                "unknown",
            ]
        ]
    ]

    type: Literal[
        "android_cloud_phone",
        "dedicated_premium_device",
        "dedicated_physical_device",
        "dedicated_ios_device",
        "dedicated_emulated_device",
    ]
    """
    Deprecated device type aliases are accepted during a compatibility grace period:
    dedicated_premium_device maps to android_cloud_phone, dedicated_physical_device
    maps to android_physical_phone, dedicated_ios_device maps to ios_stealth_phone,
    and dedicated_emulated_device maps to android_emulator.
    """
