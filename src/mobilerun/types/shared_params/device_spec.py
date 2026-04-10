# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr
from .device_carrier import DeviceCarrier
from .device_identifiers import DeviceIdentifiers
from ..proxy_config_param import ProxyConfigParam

__all__ = ["DeviceSpec"]


class DeviceSpec(TypedDict, total=False):
    apps: Optional[SequenceNotStr[str]]

    carrier: DeviceCarrier

    files: Optional[SequenceNotStr[str]]

    identifiers: DeviceIdentifiers

    name: str

    proxy: ProxyConfigParam
