# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .task_status import TaskStatus
from .package_credentials import PackageCredentials

__all__ = ["TaskRetrieveResponse", "Task"]


class Task(BaseModel):
    """The task"""

    id: str

    device_id: str = FieldInfo(alias="deviceId")

    display_id: int = FieldInfo(alias="displayId")

    llm_model: str = FieldInfo(alias="llmModel")
    """The LLM model identifier to use for the task (e.g. 'gemini/gemini-2.5-flash')"""

    owner_id: str = FieldInfo(alias="ownerId")

    status: TaskStatus

    task: str

    tmp_device: bool = FieldInfo(alias="tmpDevice")

    user_id: str = FieldInfo(alias="userId")
    """Deprecated: use ownerId (tenancy) / createdBy (actor)."""

    accessibility: Optional[bool] = None

    agent_id: Optional[int] = FieldInfo(alias="agentId", default=None)

    apps: Optional[List[str]] = None

    cancel_requested_at: Optional[datetime] = FieldInfo(alias="cancelRequestedAt", default=None)

    claimed_at: Optional[datetime] = FieldInfo(alias="claimedAt", default=None)

    continue_on_failure: Optional[bool] = FieldInfo(alias="continueOnFailure", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    credentials: Optional[List[PackageCredentials]] = None

    credits_used: Optional[float] = FieldInfo(alias="creditsUsed", default=None)

    dispatched_at: Optional[datetime] = FieldInfo(alias="dispatchedAt", default=None)

    execution_timeout: Optional[int] = FieldInfo(alias="executionTimeout", default=None)

    files: Optional[List[str]] = None

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)

    memory_namespace: Optional[str] = FieldInfo(alias="memoryNamespace", default=None)
    """Memory namespace for cross-task personalization"""

    message: Optional[str] = None

    output: Optional[Dict[str, object]] = None

    output_schema: Optional[Dict[str, object]] = FieldInfo(alias="outputSchema", default=None)

    reasoning: Optional[bool] = None

    stealth: Optional[bool] = None

    steps: Optional[int] = None

    stream_url: Optional[str] = FieldInfo(alias="streamUrl", default=None)

    subagent_model: Optional[str] = FieldInfo(alias="subagentModel", default=None)
    """LLM model used by sub-agent roles: executor, app_opener, structured_output"""

    succeeded: Optional[bool] = None

    temperature: Optional[float] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    vision: Optional[bool] = None

    vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] = FieldInfo(
        alias="vpnCountry", default=None
    )


class TaskRetrieveResponse(BaseModel):
    task: Task
    """The task"""
