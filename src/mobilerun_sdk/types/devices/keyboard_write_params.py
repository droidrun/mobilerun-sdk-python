# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["KeyboardWriteParams"]


class KeyboardWriteParams(TypedDict, total=False):
    text: Required[str]

    clear: bool

    error_rate: Annotated[float, PropertyInfo(alias="errorRate")]
    """Per-character mistake rate for humantouch typing. -1 uses server default."""

    stealth: bool

    wpm: int
    """Words per minute for stealth typing. 0 uses portal default."""

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
