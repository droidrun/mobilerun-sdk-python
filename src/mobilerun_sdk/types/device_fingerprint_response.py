# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from pydantic import Field as FieldInfo

from .shared.device_carrier import DeviceCarrier

from .shared.device_identifiers import DeviceIdentifiers

__all__ = ["DeviceFingerprintResponse", "Display", "Model"]

class Display(BaseModel):
    density_dpi: Optional[int] = FieldInfo(alias = "densityDpi", default = None)

    height: Optional[int] = None

    width: Optional[int] = None

class Model(BaseModel):
    aosp_version: Optional[str] = FieldInfo(alias = "aospVersion", default = None)

    brand: Optional[str] = None

    device: Optional[str] = None

    hardware: Optional[str] = None

    image_repository: Optional[str] = FieldInfo(alias = "imageRepository", default = None)

    manufacturer: Optional[str] = None

    model: Optional[str] = None

class DeviceFingerprintResponse(BaseModel):
    carrier: DeviceCarrier

    display: Display

    identifiers: DeviceIdentifiers

    model: Model

    schema_: Optional[str] = FieldInfo(alias = "$schema", default = None)
    """A URL to the JSON Schema for this object."""