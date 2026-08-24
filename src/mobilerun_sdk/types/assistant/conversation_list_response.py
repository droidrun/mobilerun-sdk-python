# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConversationListResponse", "Session", "SessionUnionMember0", "SessionUnionMember1"]


class SessionUnionMember0(BaseModel):
    id: str

    agent: Optional[str] = None

    base_prompt_tokens: Optional[float] = FieldInfo(alias="basePromptTokens", default=None)

    context_exhausted_at: Optional[str] = FieldInfo(alias="contextExhaustedAt", default=None)

    cost_cents: float = FieldInfo(alias="costCents")

    cost_usd: float = FieldInfo(alias="costUsd")

    created_at: str = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    episode: int

    kind: Literal["chat"]

    last_active_at: str = FieldInfo(alias="lastActiveAt")

    peak_prompt_tokens: Optional[float] = FieldInfo(alias="peakPromptTokens", default=None)

    pinned: bool

    prompt_status: Literal["ready", "machine_replaced"] = FieldInfo(alias="promptStatus")

    source_execution_id: None = FieldInfo(alias="sourceExecutionId", default=None)

    status: str

    title: str

    turn_active: bool = FieldInfo(alias="turnActive")

    turn_started_at: Optional[str] = FieldInfo(alias="turnStartedAt", default=None)

    workflow_id: None = FieldInfo(alias="workflowId", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)


class SessionUnionMember1(BaseModel):
    id: str

    agent: Optional[str] = None

    base_prompt_tokens: Optional[float] = FieldInfo(alias="basePromptTokens", default=None)

    context_exhausted_at: Optional[str] = FieldInfo(alias="contextExhaustedAt", default=None)

    cost_cents: float = FieldInfo(alias="costCents")

    cost_usd: float = FieldInfo(alias="costUsd")

    created_at: str = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    episode: int

    kind: Literal["agent_workflow"]

    last_active_at: str = FieldInfo(alias="lastActiveAt")

    peak_prompt_tokens: Optional[float] = FieldInfo(alias="peakPromptTokens", default=None)

    pinned: bool

    prompt_status: Literal["ready", "machine_replaced"] = FieldInfo(alias="promptStatus")

    source_execution_id: str = FieldInfo(alias="sourceExecutionId")

    status: str

    title: str

    turn_active: bool = FieldInfo(alias="turnActive")

    turn_started_at: Optional[str] = FieldInfo(alias="turnStartedAt", default=None)

    workflow_id: str = FieldInfo(alias="workflowId")

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)


Session: TypeAlias = Union[SessionUnionMember0, SessionUnionMember1]


class ConversationListResponse(BaseModel):
    sessions: List[Session]
