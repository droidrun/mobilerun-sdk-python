# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExecutionGetMetricsResponse", "Data", "DataByStatus"]


class DataByStatus(BaseModel):
    cancelled: int

    failed: int

    invalid: int

    pending: int

    running: int

    skipped: int

    success: int


class Data(BaseModel):
    avg_duration_ms: Optional[float] = FieldInfo(alias="avgDurationMs", default=None)

    by_status: DataByStatus = FieldInfo(alias="byStatus")

    last_execution_at: Optional[str] = FieldInfo(alias="lastExecutionAt", default=None)

    total: int


class ExecutionGetMetricsResponse(BaseModel):
    data: Data
