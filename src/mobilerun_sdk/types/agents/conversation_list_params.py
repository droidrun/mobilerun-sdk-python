# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
    kind: Literal["chat", "agent_workflow"]

    mine: Literal["true", "false"]

    workflow_id: Annotated[str, PropertyInfo(alias="workflowId")]
