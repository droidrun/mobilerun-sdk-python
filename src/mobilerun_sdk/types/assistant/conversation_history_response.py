# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConversationHistoryResponse", "Message", "MessagePart", "MessageMetadata"]


class MessagePart(BaseModel):
    type: str

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class MessageMetadata(BaseModel):
    agent: Optional[str] = None

    agent_message_id: Optional[str] = FieldInfo(alias="agentMessageId", default=None)

    agent_session_id: Optional[str] = FieldInfo(alias="agentSessionId", default=None)

    turn_anchor_message_id: Optional[str] = FieldInfo(alias="turnAnchorMessageId", default=None)


class Message(BaseModel):
    id: str

    parts: List[MessagePart]

    role: Literal["user", "assistant", "system"]

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    feedback: Optional[bool] = None

    metadata: Optional[MessageMetadata] = None

    source: Optional[Literal["cloud", "telegram", "api", "workflow", "notification"]] = None

    synthetic: Optional[bool] = None

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Deprecated: use createdBy."""


class ConversationHistoryResponse(BaseModel):
    messages: List[Message]

    turn_active: bool = FieldInfo(alias="turnActive")

    truncated: Optional[bool] = None
