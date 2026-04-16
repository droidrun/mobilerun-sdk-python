# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EsimActivateParams"]


class EsimActivateParams(TypedDict, total=False):
    enable: Required[bool]

    matching_id: Required[Annotated[str, PropertyInfo(alias="matchingId")]]

    sm_dp_addr: Required[Annotated[str, PropertyInfo(alias="smDpAddr")]]

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
