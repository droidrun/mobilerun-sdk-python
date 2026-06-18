# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DeliveryStatsResponse", "Data", "DataByStatus"]


class DataByStatus(BaseModel):
    dead: float

    pending: float

    skipped: float

    success: float


class Data(BaseModel):
    by_status: DataByStatus = FieldInfo(alias="byStatus")

    success_rate: Optional[float] = FieldInfo(alias="successRate", default=None)

    total: float


class DeliveryStatsResponse(BaseModel):
    data: Data
