# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .device_carrier import DeviceCarrier
from .device_identifiers import DeviceIdentifiers

__all__ = ["DeviceSpec", "Location", "Proxy", "ProxySocks5"]


class Location(BaseModel):
    latitude: float

    longitude: float

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""


class ProxySocks5(BaseModel):
    host: str

    password: str

    port: int

    user: str


class Proxy(BaseModel):
    name: Optional[str] = None

    smart_ip: Optional[bool] = FieldInfo(alias="smartIp", default=None)

    socks5: Optional[ProxySocks5] = None


class DeviceSpec(BaseModel):
    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    android_version: Optional[int] = FieldInfo(alias="androidVersion", default=None)

    apps: Optional[List[str]] = None

    carrier: Optional[DeviceCarrier] = None

    country: Optional[str] = None

    files: Optional[List[str]] = None

    identifiers: Optional[DeviceIdentifiers] = None

    locale: Optional[str] = None

    location: Optional[Location] = None

    name: Optional[str] = None

    proxy: Optional[Proxy] = None

    timezone: Optional[str] = None
