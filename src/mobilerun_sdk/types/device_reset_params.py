# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["DeviceResetParams"]


class DeviceResetParams(TypedDict, total=False):
    mode: Literal["full", "identity"]
    """What to erase.

    full: factory reset — erases the user data (apps, accounts, storage) and gives
    the device a new identity. identity: new device fingerprint, apps and data are
    kept. When omitted: full, or identity on devices whose capabilities report
    factoryReset=false.
    """

    preserve: Optional[List[Literal["proxy", "location", "locale", "timezone"]]]
    """
    Device configuration to restore after the reset: the latest value set through
    the API. Omitted, null or empty preserves nothing.
    """
