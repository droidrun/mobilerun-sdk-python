# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EsimCapacityResponse", "Data"]


class Data(BaseModel):
    available: bool

    free_devices: int = FieldInfo(alias="freeDevices")


class EsimCapacityResponse(BaseModel):
    data: Data
