# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TaskGetStatusResponse", "Execution", "ExecutionCheckpoint"]


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


class TaskGetStatusResponse(BaseModel):
    status: Literal["queued", "created", "running", "cancelling", "completed", "failed", "cancelled"]
    """The status of the task"""

    execution: Optional[Execution] = None
    """Execution metadata for abnormal terminal outcomes"""

    last_response: Optional[Dict[str, object]] = FieldInfo(alias="lastResponse", default=None)
    """The last agent response (FastAgentResponseEvent or ManagerPlanEvent)"""

    message: Optional[str] = None
    """The agent's final answer or failure reason"""

    output: Optional[Dict[str, object]] = None
    """Structured output if outputSchema was set"""

    steps: Optional[int] = None
    """Number of steps taken"""

    succeeded: Optional[bool] = None
    """Whether the task succeeded"""
