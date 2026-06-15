# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowExecution"]


class FlowExecution(BaseModel):
    id: str

    error: Optional[str] = None

    event_id: Optional[str] = FieldInfo(alias="eventId", default=None)

    finished_at: Optional[str] = FieldInfo(alias="finishedAt", default=None)

    flow_id: str = FieldInfo(alias="flowId")

    flow_name: Optional[str] = FieldInfo(alias="flowName", default=None)

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)

    status: Optional[Literal["pending", "running", "success", "failed"]] = None

    trigger_id: str = FieldInfo(alias="triggerId")

    trigger_name: Optional[str] = FieldInfo(alias="triggerName", default=None)

    result: Optional[object] = None
