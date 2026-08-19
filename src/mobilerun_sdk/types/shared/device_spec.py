# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from pydantic import Field as FieldInfo

from .device_carrier import DeviceCarrier

from .device_identifiers import DeviceIdentifiers

from .location import Location

__all__ = ["DeviceSpec", "Proxy", "ProxyConnect", "ProxySocks5"]

class ProxyConnect(BaseModel):
    id: Optional[str] = None
    """Existing Mobilerun Connect proxy id; its credentials are fetched server-side."""

    country: Optional[str] = None
    """
    ISO 3166-1 alpha-2 country code; provisions (or reuses) a rotating residential
    Mobilerun Connect proxy for the device.
    """

class ProxySocks5(BaseModel):
    host: str

    password: str

    port: int

    user: str

class Proxy(BaseModel):
    connect: Optional[ProxyConnect] = None

    name: Optional[str] = None

    smart_ip: Optional[bool] = FieldInfo(alias = "smartIp", default = None)

    socks5: Optional[ProxySocks5] = None

class DeviceSpec(BaseModel):
    schema_: Optional[str] = FieldInfo(alias = "$schema", default = None)
    """A URL to the JSON Schema for this object."""

    android_version: Optional[int] = FieldInfo(alias = "androidVersion", default = None)

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