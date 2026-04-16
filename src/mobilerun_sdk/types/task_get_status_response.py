# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .task_status import TaskStatus

__all__ = ["TaskGetStatusResponse"]


class TaskGetStatusResponse(BaseModel):
    status: TaskStatus
    """The status of the task"""

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
