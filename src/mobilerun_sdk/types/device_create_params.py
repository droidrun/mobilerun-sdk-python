# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.location import Location
from .shared_params.device_carrier import DeviceCarrier
from .shared_params.device_identifiers import DeviceIdentifiers

__all__ = ["DeviceCreateParams", "Proxy", "ProxyConnect", "ProxySocks5"]


class DeviceCreateParams(TypedDict, total=False):
    billing: Literal["auto", "subscription", "minute"]
    """Billing mode.

    'auto' tries subscription first, then minute billing if no subscription
    entitlement exists or all subscription slots are in use, provided minute billing
    is enabled. When subscription billing is disabled, auto uses minutes directly.
    Billing-service failures never trigger fallback. 'subscription' requires an
    available subscription slot and never falls back. 'minute' uses minute billing
    only, subject to balance and concurrency checks. Modes depend on the device
    type's billing configuration.
    """

    query_country: Annotated[str, PropertyInfo(alias="country")]
    """ISO 3166-1 alpha-2 country code.

    If omitted the system picks the country with the most availability.
    """

    device_type: Annotated[str, PropertyInfo(alias="deviceType")]
    """Use android_cloud_phone for a cloud Android phone.

    Only canonical identifiers are accepted. Other backends are deployment-specific;
    recognized but unavailable types return DEVICE*TYPE_UNAVAILABLE (422). Retired
    dedicated*\\** aliases are rejected with a canonical replacement.
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
