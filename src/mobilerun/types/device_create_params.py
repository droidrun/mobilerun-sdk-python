# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.device_carrier import DeviceCarrier
from .shared_params.device_identifiers import DeviceIdentifiers

__all__ = ["DeviceCreateParams", "Proxy", "ProxySocks5"]


class DeviceCreateParams(TypedDict, total=False):
    device_type: Annotated[
        Literal[
            "dedicated_physical_device", "dedicated_premium_device", "dedicated_emulated_device", "dedicated_ios_device"
        ],
        PropertyInfo(alias="deviceType"),
    ]

    apps: Optional[SequenceNotStr[str]]

    carrier: DeviceCarrier

    files: Optional[SequenceNotStr[str]]

    identifiers: DeviceIdentifiers

    name: str

    proxy: Proxy


class ProxySocks5(TypedDict, total=False):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class Proxy(TypedDict, total=False):
    name: str

    smart_ip: Annotated[bool, PropertyInfo(alias="smartIp")]

    socks5: ProxySocks5

    wireguard: str
