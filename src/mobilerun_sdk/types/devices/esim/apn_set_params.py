# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from ...._utils import PropertyInfo

__all__ = ["ApnSetParams"]

class ApnSetParams(TypedDict, total=False):
    apn: Required[str]

    mcc: Required[str]

    mnc: Required[str]

    name: Required[str]

    protocol: Required[str]

    roaming_protocol: Required[Annotated[str, PropertyInfo(alias="roamingProtocol")]]

    sub_id: Required[Annotated[int, PropertyInfo(alias="subId")]]

    type: Required[str]

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]