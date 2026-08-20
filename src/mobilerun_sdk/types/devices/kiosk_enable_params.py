# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["KioskEnableParams"]


class KioskEnableParams(TypedDict, total=False):
    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]
    """Package to lock the device to (Android lock-task mode)."""

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
