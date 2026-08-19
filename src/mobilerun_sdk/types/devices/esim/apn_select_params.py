# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from ...._utils import PropertyInfo

__all__ = ["ApnSelectParams"]

class ApnSelectParams(TypedDict, total=False):
    apn_id: Required[Annotated[int, PropertyInfo(alias="apnId")]]

    sub_id: Required[Annotated[int, PropertyInfo(alias="subId")]]

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]