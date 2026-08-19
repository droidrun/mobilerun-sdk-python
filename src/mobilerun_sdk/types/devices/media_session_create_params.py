# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["MediaSessionCreateParams"]

class MediaSessionCreateParams(TypedDict, total=False):
    camera: Required[bool]
    """
    Publish combined browser audio and H264 video into the device's virtual
    microphone and camera. Requires microphone=true.
    """

    microphone: Required[bool]
    """Publish browser audio into the device's virtual microphone."""