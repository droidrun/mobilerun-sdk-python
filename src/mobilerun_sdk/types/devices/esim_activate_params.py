# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EsimActivateParams"]


class EsimActivateParams(TypedDict, total=False):
    enable: Required[bool]

    sm_dp_addr: Required[Annotated[str, PropertyInfo(alias="smDpAddr")]]

    confirmation_code: Annotated[str, PropertyInfo(alias="confirmationCode")]
    """Optional carrier-issued confirmation code (the 4th LPA segment).

    Required only for plans whose SM-DP+ challenges the device for one. Requires
    matchingId — the LPA spec only interprets segment 4 when segment 3 is present.
    """

    matching_id: Annotated[str, PropertyInfo(alias="matchingId")]

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
