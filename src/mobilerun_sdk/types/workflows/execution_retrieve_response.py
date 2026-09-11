# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExecutionRetrieveResponse", "Data", "DataFile", "DataRecording"]


class DataFile(BaseModel):
    file_id: str = FieldInfo(alias="fileId")

    filename: str

    mime_type: str = FieldInfo(alias="mimeType")

    size_bytes: int = FieldInfo(alias="sizeBytes")


class DataRecording(BaseModel):
    id: str

    attempt: int

    child_index: int = FieldInfo(alias="childIndex")

    flow_action_id: Optional[str] = FieldInfo(alias="flowActionId", default=None)

    iteration_index: int = FieldInfo(alias="iterationIndex")

    last_error: Optional[str] = FieldInfo(alias="lastError", default=None)

    parent_index: int = FieldInfo(alias="parentIndex")

    recording_device_id: Optional[str] = FieldInfo(alias="recordingDeviceId", default=None)

    recording_id: Optional[str] = FieldInfo(alias="recordingId", default=None)

    scope: Literal["flow", "step"]

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)

    status: Literal["starting", "recording", "stopping", "stopped", "failed"]

    step_index: int = FieldInfo(alias="stepIndex")

    stopped_at: Optional[str] = FieldInfo(alias="stoppedAt", default=None)


class Data(BaseModel):
    id: str

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    error: Optional[str] = None

    event_id: Optional[str] = FieldInfo(alias="eventId", default=None)

    files: List[DataFile]
    """
    Files produced by files.upload steps, plus files an agent.run step reported on
    its terminal response (agent-created output or a workflow upload minted during
    the turn); derived server-side at read time.
    """

    finished_at: Optional[str] = FieldInfo(alias="finishedAt", default=None)

    flow_id: str = FieldInfo(alias="flowId")

    flow_name: Optional[str] = FieldInfo(alias="flowName", default=None)

    kind: Literal["live", "dry_run"]

    recording_device_id: Optional[str] = FieldInfo(alias="recordingDeviceId", default=None)

    recording_id: Optional[str] = FieldInfo(alias="recordingId", default=None)
    """
    Device-recording id (devices-api) for this execution, set once the worker starts
    a recording. Null when the flow has recording disabled, no device is bound, or
    the recording failed to start.
    """

    recordings: List[DataRecording]
    """Durable recording segments ordered by step/loop coordinate and retry attempt.

    Whole-flow recordings use -1 for every coordinate.
    """

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)

    status: Optional[Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"]] = None

    trigger_id: str = FieldInfo(alias="triggerId")

    trigger_name: Optional[str] = FieldInfo(alias="triggerName", default=None)

    result: Optional[object] = None
    """Opaque per-step result blob ({ steps: [...] }).

    Each step additionally carries a `verdict` field ({ outcome, summary, reason? }
    | null) when it is an agent.run step that opted into a verdict — null otherwise.
    Table-backed steps (current executions) also carry a `status` string (e.g.
    success/failed/stopped, see deriveStepStatus); it is optional and absent on
    legacy blob-only executions, so clients must not assume its presence.
    """


class ExecutionRetrieveResponse(BaseModel):
    data: Data
