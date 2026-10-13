# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActionTapParams"]


class ActionTapParams(TypedDict, total=False):
    x: Required[int]

    y: Required[int]

    humanize: bool
    """Request human-like input where supported by the device. Defaults to false."""

    stealth: bool
    """Deprecated: use humanize. Both names must agree when supplied together."""

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
