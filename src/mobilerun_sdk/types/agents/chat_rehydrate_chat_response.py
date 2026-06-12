# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ChatRehydrateChatResponse", "Message", "MessagePart", "MessageMetadata"]


class MessagePart(BaseModel):
    type: str

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[object]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[object]]


class MessageMetadata(BaseModel):
    agent: Optional[str] = None

    agent_message_id: Optional[str] = FieldInfo(alias="agentMessageId", default=None)

    agent_session_id: Optional[str] = FieldInfo(alias="agentSessionId", default=None)


class Message(BaseModel):
    id: str

    parts: List[MessagePart]

    role: Literal["user", "assistant", "system"]

    metadata: Optional[MessageMetadata] = None

    source: Optional[Literal["cloud", "telegram", "api", "workflow"]] = None

    synthetic: Optional[bool] = None


class ChatRehydrateChatResponse(BaseModel):
    messages: List[Message]

    turn_active: bool = FieldInfo(alias="turnActive")
