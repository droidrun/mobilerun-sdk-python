# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import Optional, List

__all__ = ["ServiceListMethodsResponse", "Data", "DataParam"]

class DataParam(BaseModel):
    description: str

    name: str

    required: bool

    type: Literal["string", "number", "boolean", "object", "array"]

    default: Optional[object] = None

    example: Optional[object] = None

class Data(BaseModel):
    method: str

    params: List[DataParam]

class ServiceListMethodsResponse(BaseModel):
    data: List[Data]