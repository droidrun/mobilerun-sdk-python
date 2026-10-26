# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ConversationHistoryResponse",
    "Agent",
    "AgentProfile",
    "AgentProfileAvatarConfig",
    "Data",
    "DataPart",
    "DataMetadata",
    "DataMetadataSteer",
    "Turn",
    "TurnTurnState",
]


class AgentProfileAvatarConfig(BaseModel):
    """
    Configuration of a `blob` avatar: its seed and optional user-chosen palette color. A color-only config retains the default seed fallback.
    """

    color: Optional[
        Literal["slate", "red", "orange", "amber", "lime", "green", "teal", "cyan", "blue", "indigo", "violet", "pink"]
    ] = None

    seed: Union[str, int, None] = None


class AgentProfile(BaseModel):
    avatar_config: Optional[AgentProfileAvatarConfig] = FieldInfo(alias="avatarConfig", default=None)
    """
    Configuration of a `blob` avatar: its seed and optional user-chosen palette
    color. A color-only config retains the default seed fallback.
    """

    avatar_kind: Optional[Literal["blob"]] = FieldInfo(alias="avatarKind", default=None)

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)


class Agent(BaseModel):
    """
    Session Agent identity, present on every page; null only when the session has no Agent.
    """

    id: str

    profile: AgentProfile


class DataPart(BaseModel):
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


class DataMetadataSteer(BaseModel):
    """
    Steer user rows appear directly above the collapsed assistant group of their turn, matching live cloud ordering.
    """

    agent_message_id: str = FieldInfo(alias="agentMessageId")

    state: Literal["accepted", "consumed", "dropped"]

    target_role: Literal["root", "worker"] = FieldInfo(alias="targetRole")

    consumed_at: Optional[datetime] = FieldInfo(alias="consumedAt", default=None)

    drop_reason: Optional[Literal["turn_closed", "aborted"]] = FieldInfo(alias="dropReason", default=None)


class DataMetadata(BaseModel):
    agent: Optional[str] = None

    agent_message_id: Optional[str] = FieldInfo(alias="agentMessageId", default=None)

    agent_session_id: Optional[str] = FieldInfo(alias="agentSessionId", default=None)

    steer: Optional[DataMetadataSteer] = None
    """
    Steer user rows appear directly above the collapsed assistant group of their
    turn, matching live cloud ordering.
    """

    turn_anchor_message_id: Optional[str] = FieldInfo(alias="turnAnchorMessageId", default=None)


class Data(BaseModel):
    id: str

    parts: List[DataPart]

    role: Literal["user", "assistant", "system"]

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    feedback: Optional[bool] = None

    metadata: Optional[DataMetadata] = None

    source: Optional[Literal["cloud", "telegram", "api", "workflow", "notification"]] = None

    synthetic: Optional[bool] = None

    turn_id: Optional[str] = FieldInfo(alias="turnId", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Deprecated: use createdBy."""


class TurnTurnState(BaseModel):
    id: str

    abort_requested: bool = FieldInfo(alias="abortRequested")

    attachable: bool

    claim_held: bool = FieldInfo(alias="claimHeld")

    outcome: Optional[str] = None
    """Outcome of the latest turn, or null while it is still open."""

    phase: Literal["created", "running", "closed", "delivered", "failed"]

    reaping: bool

    revision: int

    started_at: str = FieldInfo(alias="startedAt")


class Turn(BaseModel):
    """Newest-page turn snapshot; null when before is supplied."""

    turn_active: bool = FieldInfo(alias="turnActive")
    """Whether this session owns an in-flight turn."""

    turn_state: Optional[TurnTurnState] = FieldInfo(alias="turnState", default=None)


class ConversationHistoryResponse(BaseModel):
    agent: Optional[Agent] = None
    """
    Session Agent identity, present on every page; null only when the session has no
    Agent.
    """

    data: List[Data]

    first_id: Optional[str] = FieldInfo(alias="firstId", default=None)
    """Oldest real row in the page; pass as before to load older turns."""

    has_more: bool = FieldInfo(alias="hasMore")
    """Older whole turns exist."""

    last_id: Optional[str] = FieldInfo(alias="lastId", default=None)
    """Newest real row in the page, before continuation collapse or synthetic rows."""

    turn: Optional[Turn] = None
    """Newest-page turn snapshot; null when before is supplied."""
