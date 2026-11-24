# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ScheduledRunCancelResponse", "Data"]


class Data(BaseModel):
    id: str

    cancelled_at: Optional[datetime] = FieldInfo(alias="cancelledAt", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: str = FieldInfo(alias="createdBy")

    error: Optional[str] = None

    execution_ids: List[str] = FieldInfo(alias="executionIds")

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)

    flow_id: str = FieldInfo(alias="flowId")

    payload: Dict[str, object]

    run_at: datetime = FieldInfo(alias="runAt")

    skip_reason: Optional[str] = FieldInfo(alias="skipReason", default=None)

    status: Literal["scheduled", "started", "skipped", "failed", "missed", "cancelled"]


class ScheduledRunCancelResponse(BaseModel):
    data: Data
