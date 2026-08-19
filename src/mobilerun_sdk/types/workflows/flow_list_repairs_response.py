# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, List

from pydantic import Field as FieldInfo

__all__ = ["FlowListRepairsResponse", "Data", "DataVerdict"]

class DataVerdict(BaseModel):
    outcome: Literal["ok", "flaky", "broken"]

    summary: str

    reason: Optional[str] = None

class Data(BaseModel):
    id: str

    agent_run_id: Optional[str] = FieldInfo(alias = "agentRunId", default = None)

    attempt: int

    candidate_slug: str = FieldInfo(alias = "candidateSlug")

    chat_session_id: Optional[str] = FieldInfo(alias = "chatSessionId", default = None)

    created_at: Optional[str] = FieldInfo(alias = "createdAt", default = None)

    device_id: Optional[str] = FieldInfo(alias = "deviceId", default = None)

    episode: int

    error: Optional[str] = None

    failed_step_index: int = FieldInfo(alias = "failedStepIndex")

    finished_at: Optional[str] = FieldInfo(alias = "finishedAt", default = None)

    flow_id: str = FieldInfo(alias = "flowId")

    max_attempts: int = FieldInfo(alias = "maxAttempts")

    original_slug: str = FieldInfo(alias = "originalSlug")

    source_execution_id: str = FieldInfo(alias = "sourceExecutionId")

    started_at: Optional[str] = FieldInfo(alias = "startedAt", default = None)

    status: Literal["pending", "running", "canary", "promoting", "repaired", "failed", "escalated"]

    updated_at: Optional[str] = FieldInfo(alias = "updatedAt", default = None)

    verdict: Optional[DataVerdict] = None

class FlowListRepairsResponse(BaseModel):
    data: List[Data]