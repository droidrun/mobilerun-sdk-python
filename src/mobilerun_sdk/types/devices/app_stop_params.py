# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from ..._utils import PropertyInfo

__all__ = ["AppStopParams"]

class AppStopParams(TypedDict, total=False):
    device_id: Required[Annotated[str, PropertyInfo(alias="deviceId")]]

    clear_data: Annotated[bool, PropertyInfo(alias="clearData")]
    """If true, clears all app data (pm clear) in addition to stopping the app."""

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]