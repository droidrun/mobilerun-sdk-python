# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FlowValidateDocumentResponse", "Data", "DataError", "DataErrorRepair", "DataWarning"]


class DataErrorRepair(BaseModel):
    action: Literal["fix_spec_and_restart", "ask_user", "retry_later"]

    hint: str


class DataError(BaseModel):
    code: str

    field: str
    """RFC 6901 JSON Pointer; empty string is the document root"""

    message: str

    repair: DataErrorRepair


class DataWarning(BaseModel):
    code: str

    message: str


class Data(BaseModel):
    errors: List[DataError]

    valid: bool

    warnings: List[DataWarning]


class FlowValidateDocumentResponse(BaseModel):
    data: Data
