# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
