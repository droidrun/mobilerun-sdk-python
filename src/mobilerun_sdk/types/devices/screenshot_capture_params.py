# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScreenshotCaptureParams"]


class ScreenshotCaptureParams(TypedDict, total=False):
    hide_overlay: Annotated[bool, PropertyInfo(alias="hideOverlay")]

    save: bool
    """
    Store the screenshot as device media: in the owner's active recording, or
    standalone for 7 days. Without save=true nothing is stored. The PNG response is
    unchanged; X-Screenshot-Saved reports whether it was stored.
    """

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
