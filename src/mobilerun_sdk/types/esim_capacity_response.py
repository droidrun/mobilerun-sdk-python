# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from pydantic import Field as FieldInfo

__all__ = ["EsimCapacityResponse", "Data"]

class Data(BaseModel):
    available: bool

    free_devices: int = FieldInfo(alias = "freeDevices")

class EsimCapacityResponse(BaseModel):
    data: Data