# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TelegramReceiveUpdateParams", "Message", "MessageChat", "MessageFrom"]


class TelegramReceiveUpdateParams(TypedDict, total=False):
    update_id: Required[float]

    message: Message


class MessageChat(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    id: Required[float]

    type: Required[str]


class MessageFrom(TypedDict, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    id: Required[float]

    first_name: str

    is_bot: bool

    username: str


_MessageReservedKeywords = TypedDict(
    "_MessageReservedKeywords",
    {
        "from": MessageFrom,
    },
    total=False,
)


class Message(_MessageReservedKeywords, total=False, extra_items=Optional[object]):  # type: ignore[call-arg]
    chat: Required[MessageChat]

    message_id: Required[float]

    caption: str

    text: str
