# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ServiceListMethodsResponse", "Data", "DataParam"]


class DataParam(BaseModel):
    description: str

    name: str

    required: bool

    type: Literal["string", "number", "boolean", "object", "array"]

    default: Optional[object] = None

    example: Optional[object] = None


class Data(BaseModel):
    is_async: bool = FieldInfo(alias="isAsync")

    method: str

    params: List[DataParam]

    requires_target: bool = FieldInfo(alias="requiresTarget")


class ServiceListMethodsResponse(BaseModel):
    data: List[Data]
