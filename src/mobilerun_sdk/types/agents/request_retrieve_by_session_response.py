# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "RequestRetrieveBySessionResponse",
    "Error",
    "Event",
    "Request",
    "Result",
    "ResultText",
    "ResultQuestion",
    "Room",
    "RoomMember",
]


class Error(BaseModel):
    code: str
    """Why the request did not produce an answer.

    An open set: new codes can appear. Codes written today: `agent_archived`,
    `agent_disabled`, `dispatch_failed`, `timed_out`, `cancelled`,
    `result_too_large`, `no_answer`, `target_turn_failed`, `target_error`,
    `target_aborted`, `target_crash_recovered`, `target_unknown_outcome`.
    """

    message: str

    preview: Optional[str] = None


class Event(BaseModel):
    created_at: str = FieldInfo(alias="createdAt")

    kind: str

    payload: Optional[Dict[str, object]] = None

    seq: int


class Request(BaseModel):
    message: str

    source_display_name: Optional[str] = FieldInfo(alias="sourceDisplayName", default=None)

    timeout_seconds: int = FieldInfo(alias="timeoutSeconds")

    file_ids: Optional[List[str]] = FieldInfo(alias="fileIds", default=None)


class ResultText(BaseModel):
    text: str


class ResultQuestion(BaseModel):
    question: str


Result: TypeAlias = Union[ResultText, ResultQuestion, None]


class RoomMember(BaseModel):
    id: str

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    joined_at: str = FieldInfo(alias="joinedAt")

    left_at: Optional[str] = FieldInfo(alias="leftAt", default=None)

    participant_type: Literal["agent", "user"] = FieldInfo(alias="participantType")

    role: Literal["owner", "member"]

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)


class Room(BaseModel):
    id: str

    kind: Literal["direct", "group"]

    members: List[RoomMember]


class RequestRetrieveBySessionResponse(BaseModel):
    id: str

    created_at: str = FieldInfo(alias="createdAt")

    deadline_at: str = FieldInfo(alias="deadlineAt")

    depth: int

    dispatch_attempts: int = FieldInfo(alias="dispatchAttempts")

    dispatched_at: Optional[str] = FieldInfo(alias="dispatchedAt", default=None)

    error: Optional[Error] = None

    events: List[Event]

    finished_at: Optional[str] = FieldInfo(alias="finishedAt", default=None)

    request: Request

    result: Optional[Result] = None

    room: Room

    source_agent_id: str = FieldInfo(alias="sourceAgentId")

    source_session_id: str = FieldInfo(alias="sourceSessionId")

    status: Literal[
        "queued", "running", "answered", "failed", "timed_out", "cancelled", "late_answer", "needs_user_input"
    ]

    target_agent_id: str = FieldInfo(alias="targetAgentId")

    target_session_id: str = FieldInfo(alias="targetSessionId")

    updated_at: str = FieldInfo(alias="updatedAt")

    visited: List[str]
