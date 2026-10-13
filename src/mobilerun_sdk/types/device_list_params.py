# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["DeviceListParams"]


class DeviceListParams(TypedDict, total=False):
    country: str

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Include devices created at or after this RFC3339 timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]
    """Include devices created before this RFC3339 timestamp (exclusive).

    Must be later than createdAfter when both are set.
    """

    created_by: Annotated[str, PropertyInfo(alias="createdBy")]
    """Filter to devices created by this user id. Mutually exclusive with mine."""

    mine: bool
    """When true, only return devices created by the authenticated caller."""

    name: str

    order_by: Annotated[
        Literal["id", "createdAt", "updatedAt", "assignedAt", "gridPosition"], PropertyInfo(alias="orderBy")
    ]

    order_by_direction: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderByDirection")]

    owner_id: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="ownerId")]
    """Filter by owner IDs.

    Comma-separated or repeated parameters. Restricted to platform administrators.
    """

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    platform: Literal["android", "ios"]
    """
    Filter by the device's platform as served in the platform field (runtime,
    announced, else type-derived).
    """

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
    """Filter by current device state.

    Comma-separated (state=ready,stopped). Defaults to every state except terminated
    and unknown, so stopped and maintenance devices are listed; pass
    state=terminated or state=unknown to see those.
    """

    type: Literal[
        "android_cloud_phone",
        "android_physical_phone",
        "ios_stealth_phone",
        "android_emulator",
        "ios_simulator",
        "device_slot",
    ]
    """Canonical device type.

    Retired dedicated\\__\\** aliases are no longer accepted. Availability depends on
    the deployment.
    """
