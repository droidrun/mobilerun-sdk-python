# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .socks5 import Socks5
from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .location import Location
from .device_carrier import DeviceCarrier
from .device_identifiers import DeviceIdentifiers

__all__ = ["DeviceSpec", "Proxy"]


class Proxy(TypedDict, total=False):
    name: str

    smart_ip: Annotated[bool, PropertyInfo(alias="smartIp")]

    socks5: Socks5


class DeviceSpec(TypedDict, total=False):
    android_version: Annotated[int, PropertyInfo(alias="androidVersion")]

    apps: Optional[SequenceNotStr[str]]

    carrier: DeviceCarrier

    country: str

    files: Optional[SequenceNotStr[str]]

    identifiers: DeviceIdentifiers

    locale: str

    location: Location

    name: str

    proxy: Proxy

    timezone: str
