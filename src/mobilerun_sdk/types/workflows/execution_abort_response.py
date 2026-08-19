# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from pydantic import Field as FieldInfo

from typing_extensions import Literal

__all__ = ["ExecutionAbortResponse", "Data"]

class Data(BaseModel):
    id: str

    error: Optional[str] = None

    event_id: Optional[str] = FieldInfo(alias = "eventId", default = None)

    finished_at: Optional[str] = FieldInfo(alias = "finishedAt", default = None)

    flow_id: str = FieldInfo(alias = "flowId")

    flow_name: Optional[str] = FieldInfo(alias = "flowName", default = None)

    kind: Literal["live", "dry_run"]

    started_at: Optional[str] = FieldInfo(alias = "startedAt", default = None)

    status: Optional[Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"]] = None

    trigger_id: str = FieldInfo(alias = "triggerId")

    trigger_name: Optional[str] = FieldInfo(alias = "triggerName", default = None)

    result: Optional[object] = None
    """Opaque per-step result blob ({ steps: [...] }).

    Each step additionally carries a `verdict` field ({ outcome, summary, reason? }
    | null) when it is an agent.run step that opted into a verdict — null otherwise.
    Table-backed steps (current executions) also carry a `status` string (e.g.
    success/failed/stopped, see deriveStepStatus); it is optional and absent on
    legacy blob-only executions, so clients must not assume its presence.
    """

class ExecutionAbortResponse(BaseModel):
    data: Data