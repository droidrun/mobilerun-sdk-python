# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentListResponse", "AgentListResponseItem"]


class AgentListResponseItem(BaseModel):
    id: int

    description: Optional[str] = None

    icon: str

    llm_model: str = FieldInfo(alias="llmModel")

    max_steps: int = FieldInfo(alias="maxSteps")

    name: str

    reasoning: bool

    vision: bool


AgentListResponse: TypeAlias = List[AgentListResponseItem]
