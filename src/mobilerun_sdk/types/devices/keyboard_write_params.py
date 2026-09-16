# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["KeyboardWriteParams"]


class KeyboardWriteParams(TypedDict, total=False):
    text: Required[str]

    clear: bool

    completion_mode: Annotated[Literal["accepted", "committed"], PropertyInfo(alias="completionMode")]
    """Completion guarantee.

    accepted returns after the input provider accepts the operation; committed
    additionally waits for the focused UI state to contain the complete text or
    become quiescent.
    """

    error_rate: Annotated[float, PropertyInfo(alias="errorRate")]
    """Per-character mistake rate for humantouch typing. -1 uses server default."""

    stealth: bool

    wpm: int
    """Words per minute for stealth typing. 0 uses portal default."""

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
