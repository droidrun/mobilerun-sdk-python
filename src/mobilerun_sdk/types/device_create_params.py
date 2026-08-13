# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.socks5 import Socks5
from .shared_params.location import Location
from .shared_params.device_carrier import DeviceCarrier
from .shared_params.device_identifiers import DeviceIdentifiers

__all__ = ["DeviceCreateParams", "Proxy", "ProxyConnect"]


class DeviceCreateParams(TypedDict, total=False):
    billing: Literal["auto", "subscription", "minute"]
    """Billing mode.

    'auto' uses a subscription slot when available and otherwise bills per minute;
    'subscription' requires an available subscription slot; 'minute' bills per
    minute. Only cloud phone and cloud emulator devices support per-minute billing.
    """

    query_country: Annotated[str, PropertyInfo(alias="country")]
    """ISO 3166-1 alpha-2 country code.

    If omitted the system picks the country with the most availability.
    """

    device_type: Annotated[
        Literal[
            "android_cloud_phone",
            "dedicated_premium_device",
            "dedicated_physical_device",
            "dedicated_ios_device",
            "dedicated_emulated_device",
        ],
        PropertyInfo(alias="deviceType"),
    ]
    """
    Deprecated device type aliases are accepted during a compatibility grace period:
    dedicated_premium_device maps to android_cloud_phone, dedicated_physical_device
    maps to android_physical_phone, dedicated_ios_device maps to ios_stealth_phone,
    and dedicated_emulated_device maps to android_emulator.
    """

    profile_id: Annotated[str, PropertyInfo(alias="profileId")]
    """Profile ID to use as device spec"""

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


class ProxyConnect(TypedDict, total=False):
    id: str
    """Existing Mobilerun Connect proxy id; its credentials are fetched server-side."""

    country: str
    """
    ISO 3166-1 alpha-2 country code; provisions (or reuses) a rotating residential
    Mobilerun Connect proxy for the device.
    """


class Proxy(TypedDict, total=False):
    connect: ProxyConnect

    name: str

    smart_ip: Annotated[bool, PropertyInfo(alias="smartIp")]

    socks5: Socks5
