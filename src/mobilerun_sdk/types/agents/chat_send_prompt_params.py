# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ChatSendPromptParams", "Message", "MessagePart"]


class ChatSendPromptParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    id: str

    agent: str

    context: str

    file_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="fileIds")]

    metadata: Dict[str, Optional[object]]

    trigger: Literal["submit-message", "regenerate-message"]


class MessagePart(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    type: Required[str]


class Message(TypedDict, total=False):
    id: Required[str]

    parts: Required[Iterable[MessagePart]]

    role: Required[Literal["user", "assistant", "system"]]

    metadata: Dict[str, Optional[object]]
