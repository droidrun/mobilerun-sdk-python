# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.device_carrier import DeviceCarrier
from .shared_params.device_identifiers import DeviceIdentifiers

__all__ = ["DeviceCreateParams", "Location", "Proxy", "ProxySocks5"]


class DeviceCreateParams(TypedDict, total=False):
    query_country: Annotated[str, PropertyInfo(alias="country")]
    """ISO 3166-1 alpha-2 country code.

    If omitted the system picks the country with the most availability.
    """

    device_type: Annotated[
        Literal[
            "dedicated_physical_device", "dedicated_premium_device", "dedicated_emulated_device", "dedicated_ios_device"
        ],
        PropertyInfo(alias="deviceType"),
    ]

    android_version: Annotated[int, PropertyInfo(alias="androidVersion")]

    apps: Optional[SequenceNotStr[str]]

    carrier: DeviceCarrier

    body_country: Annotated[str, PropertyInfo(alias="country")]

    files: Optional[SequenceNotStr[str]]

    identifiers: DeviceIdentifiers

    locale: str

    location: Location

    name: str

    proxy: Proxy

    timezone: str


class Location(TypedDict, total=False):
    latitude: Required[float]

    longitude: Required[float]


class ProxySocks5(TypedDict, total=False):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class Proxy(TypedDict, total=False):
    name: str

    smart_ip: Annotated[bool, PropertyInfo(alias="smartIp")]

    socks5: ProxySocks5
