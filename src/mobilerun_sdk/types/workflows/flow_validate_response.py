# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowValidateResponse", "Data", "DataError", "DataWarning"]


class DataError(BaseModel):
    code: str

    field: str

    message: str

    known_steps: Optional[List[str]] = FieldInfo(alias="knownSteps", default=None)

    reference: Optional[str] = None


class DataWarning(BaseModel):
    code: str

    message: str

    connect_key: Optional[str] = FieldInfo(alias="connectKey", default=None)

    destination: Optional[str] = None


class Data(BaseModel):
    errors: List[DataError]

    valid: bool

    warnings: List[DataWarning]


class FlowValidateResponse(BaseModel):
    data: Data
