# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .location import Location
from .device_carrier import DeviceCarrier
from .device_identifiers import DeviceIdentifiers

__all__ = ["DeviceSpec", "Proxy", "ProxyConnect", "ProxySocks5"]


class ProxyConnect(TypedDict, total=False):
    id: str
    """Existing Mobilerun Connect proxy id; its credentials are fetched server-side."""

    country: str
    """
    ISO 3166-1 alpha-2 country code; provisions (or reuses) a rotating residential
    Mobilerun Connect proxy for the device.
    """


class ProxySocks5(TypedDict, total=False):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class Proxy(TypedDict, total=False):
    connect: ProxyConnect

    name: str

    smart_ip: Annotated[bool, PropertyInfo(alias="smartIp")]

    socks5: ProxySocks5


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
