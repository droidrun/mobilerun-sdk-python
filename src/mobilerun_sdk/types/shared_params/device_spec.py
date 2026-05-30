# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .location import Location
from .device_carrier import DeviceCarrier
from .device_identifiers import DeviceIdentifiers
from ..proxy_config_param import ProxyConfigParam

__all__ = ["DeviceSpec"]


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

    proxy: ProxyConfigParam

    timezone: str
