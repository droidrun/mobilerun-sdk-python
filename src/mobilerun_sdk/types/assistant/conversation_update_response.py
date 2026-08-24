# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConversationUpdateResponse", "Session"]


class Session(BaseModel):
    id: str

    agent: Optional[str] = None

    base_prompt_tokens: Optional[float] = FieldInfo(alias="basePromptTokens", default=None)

    context_exhausted_at: Optional[str] = FieldInfo(alias="contextExhaustedAt", default=None)

    cost_cents: float = FieldInfo(alias="costCents")

    cost_usd: float = FieldInfo(alias="costUsd")

    created_at: str = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    last_active_at: str = FieldInfo(alias="lastActiveAt")

    peak_prompt_tokens: Optional[float] = FieldInfo(alias="peakPromptTokens", default=None)

    pinned: bool

    prompt_status: Literal["ready", "machine_replaced"] = FieldInfo(alias="promptStatus")

    status: str

    title: str

    turn_active: bool = FieldInfo(alias="turnActive")

    turn_started_at: Optional[str] = FieldInfo(alias="turnStartedAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)


class ConversationUpdateResponse(BaseModel):
    session: Session
