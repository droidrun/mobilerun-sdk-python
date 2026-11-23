# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TaskGetStatusResponse", "Execution", "ExecutionCheckpoint", "PendingApproval"]


class ExecutionCheckpoint(BaseModel):
    current_subgoal: Optional[str] = FieldInfo(alias="currentSubgoal", default=None)

    plan: Optional[str] = None

    progress_summary: Optional[str] = FieldInfo(alias="progressSummary", default=None)

    steps: Optional[int] = None


class Execution(BaseModel):
    """Execution metadata for abnormal terminal outcomes"""

    checkpoint: ExecutionCheckpoint

    termination_reason: Literal["execution_timeout", "worker_lost", "cancelled", "agent_failed"] = FieldInfo(
        alias="terminationReason"
    )

    retry_safety: Optional[Literal["unknown"]] = FieldInfo(alias="retrySafety", default=None)


class PendingApproval(BaseModel):
    """A human approval the running task is waiting for."""

    approval_id: str = FieldInfo(alias="approvalId")
    """Identifies the approval"""

    details: Dict[str, object]
    """
    Kind-specific, non-secret context (payment_card: label, secretGroup,
    targetPackage, targetHost?)
    """

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """Without an answer by this time the task fails"""

    kind: str
    """What is being approved, e.g. payment_card; new kinds may be added"""

    device_id: Optional[str] = FieldInfo(alias="deviceId", default=None)
    """Device the task runs on, so a client can show it next to the approval"""


class TaskGetStatusResponse(BaseModel):
    status: Literal["prepared", "queued", "created", "running", "cancelling", "completed", "failed", "cancelled"]
    """The status of the task"""

    terminal: bool
    """True when the task has reached a final status and will not change again"""

    execution: Optional[Execution] = None
    """Execution metadata for abnormal terminal outcomes"""

    last_response: Optional[Dict[str, object]] = FieldInfo(alias="lastResponse", default=None)
    """The last agent response (FastAgentResponseEvent or ManagerPlanEvent)"""

    message: Optional[str] = None
    """The agent's final answer or failure reason"""

    output: Optional[Dict[str, object]] = None
    """Structured output if outputSchema was set"""

    pending_approval: Optional[PendingApproval] = FieldInfo(alias="pendingApproval", default=None)
    """A human approval the running task is waiting for."""

    recording_device_id: Optional[str] = FieldInfo(alias="recordingDeviceId", default=None)
    """Device ID associated with recordingId"""

    recording_id: Optional[str] = FieldInfo(alias="recordingId", default=None)
    """ID of the task's whole-task video recording, if recordingEnabled was set"""

    steps: Optional[int] = None
    """Number of steps taken"""

    succeeded: Optional[bool] = None
    """Whether the task succeeded"""
