# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowValidateResponse", "Data", "DataError", "DataErrorRepair", "DataWarning"]


class DataErrorRepair(BaseModel):
    action: Literal["fix_spec_and_restart", "ask_user", "retry_later"]

    hint: str


class DataError(BaseModel):
    code: str

    field: str

    message: str

    action_id: Optional[str] = FieldInfo(alias="actionId", default=None)

    known_steps: Optional[List[str]] = FieldInfo(alias="knownSteps", default=None)

    reference: Optional[str] = None

    repair: Optional[DataErrorRepair] = None


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
