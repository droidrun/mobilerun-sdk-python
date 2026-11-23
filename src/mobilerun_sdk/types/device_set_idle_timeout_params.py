# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DeviceSetIdleTimeoutParams"]


class DeviceSetIdleTimeoutParams(TypedDict, total=False):
    minutes: Required[Optional[int]]
    """
    Minutes without client activity after which the device is stopped automatically:
    5 to 240 sets a custom timeout, 0 turns the idle timer off for this device, null
    removes the device's own setting so the platform default applies again (if any).
    1 to 4 are rejected.
    """
