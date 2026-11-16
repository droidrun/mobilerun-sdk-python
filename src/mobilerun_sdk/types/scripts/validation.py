# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Validation", "Error", "ErrorRepair", "Warning", "WarningRepair"]


class ErrorRepair(BaseModel):
    action: str

    hint: str


class Error(BaseModel):
    code: str

    message: str

    line: Optional[int] = None

    repair: Optional[ErrorRepair] = None


class WarningRepair(BaseModel):
    action: str

    hint: str


class Warning(BaseModel):
    code: str

    message: str

    line: Optional[int] = None

    repair: Optional[WarningRepair] = None


class Validation(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    errors: List[Error]

    status: Literal["pending", "done", "failed"]

    warnings: List[Warning]

    dataset_key: Optional[str] = FieldInfo(alias="datasetKey", default=None)

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)

    input_schema: Optional[Dict[str, object]] = FieldInfo(alias="inputSchema", default=None)

    output_kind: Optional[Literal["value", "dataset", "none"]] = FieldInfo(alias="outputKind", default=None)

    output_schema: Optional[Dict[str, object]] = FieldInfo(alias="outputSchema", default=None)

    runtime_version: Optional[str] = FieldInfo(alias="runtimeVersion", default=None)

    valid: Optional[bool] = None
