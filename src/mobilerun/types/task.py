# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .task_status import TaskStatus
from .package_credentials import PackageCredentials

__all__ = ["Task"]


class Task(BaseModel):
    device_id: str = FieldInfo(alias="deviceId")

    llm_model: str = FieldInfo(alias="llmModel")
    """The LLM model identifier to use for the task (e.g. 'gemini/gemini-2.5-flash')"""

    task: str

    user_id: str = FieldInfo(alias="userId")

    id: Optional[str] = None

    agent_id: Optional[int] = FieldInfo(alias="agentId", default=None)

    apps: Optional[List[str]] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    credentials: Optional[List[PackageCredentials]] = None

    display_id: Optional[int] = FieldInfo(alias="displayId", default=None)

    execution_timeout: Optional[int] = FieldInfo(alias="executionTimeout", default=None)

    files: Optional[List[str]] = None

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)

    message: Optional[str] = None

    output: Optional[Dict[str, object]] = None

    output_schema: Optional[Dict[str, object]] = FieldInfo(alias="outputSchema", default=None)

    reasoning: Optional[bool] = None

    status: Optional[TaskStatus] = None

    stealth: Optional[bool] = None

    steps: Optional[int] = None

    succeeded: Optional[bool] = None

    temperature: Optional[float] = None

    tmp_device: Optional[bool] = FieldInfo(alias="tmpDevice", default=None)

    trajectory: Optional[List[Dict[str, object]]] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    vision: Optional[bool] = None

    vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] = FieldInfo(
        alias="vpnCountry", default=None
    )
