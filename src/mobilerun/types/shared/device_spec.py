# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .config import Config
from ..._models import BaseModel
from .device_carrier import DeviceCarrier
from .device_identifiers import DeviceIdentifiers

__all__ = ["DeviceSpec"]


class DeviceSpec(BaseModel):
    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    apps: Optional[List[str]] = None

    carrier: Optional[DeviceCarrier] = None

    files: Optional[List[str]] = None

    identifiers: Optional[DeviceIdentifiers] = None

    name: Optional[str] = None

    proxy: Optional[Config] = None

    smart_ip: Optional[bool] = FieldInfo(alias="smartIp", default=None)
