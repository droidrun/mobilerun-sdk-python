# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MessageListResponse", "Item"]


class Item(BaseModel):
    id: str

    from_address: Optional[str] = FieldInfo(alias="fromAddress", default=None)

    has_otp: bool = FieldInfo(alias="hasOtp")

    mailbox_id: str = FieldInfo(alias="mailboxId")

    preview: Optional[str] = None

    received_at: datetime = FieldInfo(alias="receivedAt")

    subject: Optional[str] = None


class MessageListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
