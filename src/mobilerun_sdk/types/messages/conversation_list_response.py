# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal

from datetime import datetime

from pydantic import Field as FieldInfo

__all__ = ["ConversationListResponse", "Data", "DataItem", "DataItemLastMessage", "DataNextCursor"]

class DataItemLastMessage(BaseModel):
    id: str

    body: Optional[str] = None

    direction: Literal["inbound", "outbound"]

    occurred_at: datetime = FieldInfo(alias = "occurredAt")

    status: Literal["received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"]

class DataItem(BaseModel):
    esim_ids: List[str] = FieldInfo(alias = "esimIds")

    last_message: DataItemLastMessage = FieldInfo(alias = "lastMessage")

    peer_key: str = FieldInfo(alias = "peerKey")

    unread_count: int = FieldInfo(alias = "unreadCount")

class DataNextCursor(BaseModel):
    last_message_id: str = FieldInfo(alias = "lastMessageId")

    last_occurred_at: datetime = FieldInfo(alias = "lastOccurredAt")

class Data(BaseModel):
    items: List[DataItem]

    next_cursor: Optional[DataNextCursor] = FieldInfo(alias = "nextCursor", default = None)

class ConversationListResponse(BaseModel):
    data: Data