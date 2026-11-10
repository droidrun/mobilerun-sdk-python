# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RequestListForAgentResponse", "Request", "RequestRoom", "RequestRoomMember"]


class RequestRoomMember(BaseModel):
    id: str

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    joined_at: str = FieldInfo(alias="joinedAt")

    left_at: Optional[str] = FieldInfo(alias="leftAt", default=None)

    participant_type: Literal["agent", "user"] = FieldInfo(alias="participantType")

    role: Literal["owner", "member"]

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)


class RequestRoom(BaseModel):
    id: str

    kind: Literal["direct", "group"]

    members: List[RequestRoomMember]


class Request(BaseModel):
    id: str

    created_at: str = FieldInfo(alias="createdAt")

    deadline_at: str = FieldInfo(alias="deadlineAt")

    depth: int

    dispatched_at: Optional[str] = FieldInfo(alias="dispatchedAt", default=None)

    error_code: Optional[str] = FieldInfo(alias="errorCode", default=None)
    """`error.code` of the full request, null when it has none.

    An open set: new codes can appear. Codes written today: `agent_archived`,
    `agent_disabled`, `dispatch_failed`, `timed_out`, `cancelled`,
    `result_too_large`, `no_answer`, `target_turn_failed`, `target_error`,
    `target_aborted`, `target_crash_recovered`, `target_unknown_outcome`.
    """

    finished_at: Optional[str] = FieldInfo(alias="finishedAt", default=None)

    room: RequestRoom

    source_agent_id: str = FieldInfo(alias="sourceAgentId")

    source_session_id: str = FieldInfo(alias="sourceSessionId")

    status: Literal[
        "queued", "running", "answered", "failed", "timed_out", "cancelled", "late_answer", "needs_user_input"
    ]

    target_agent_id: str = FieldInfo(alias="targetAgentId")

    target_session_id: str = FieldInfo(alias="targetSessionId")

    updated_at: str = FieldInfo(alias="updatedAt")


class RequestListForAgentResponse(BaseModel):
    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page; null when there are no older requests."""

    requests: List[Request]
