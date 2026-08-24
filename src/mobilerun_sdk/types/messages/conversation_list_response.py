# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConversationListResponse", "Item", "ItemLastMessage", "NextCursor"]


class ItemLastMessage(BaseModel):
    id: str

    body: Optional[str] = None

    direction: Literal["inbound", "outbound"]

    occurred_at: datetime = FieldInfo(alias="occurredAt")

    status: Literal["received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"]


class Item(BaseModel):
    esim_ids: List[str] = FieldInfo(alias="esimIds")

    last_message: ItemLastMessage = FieldInfo(alias="lastMessage")

    peer_key: str = FieldInfo(alias="peerKey")

    unread_count: int = FieldInfo(alias="unreadCount")


class NextCursor(BaseModel):
    last_message_id: str = FieldInfo(alias="lastMessageId")

    last_occurred_at: datetime = FieldInfo(alias="lastOccurredAt")


class ConversationListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[NextCursor] = FieldInfo(alias="nextCursor", default=None)
