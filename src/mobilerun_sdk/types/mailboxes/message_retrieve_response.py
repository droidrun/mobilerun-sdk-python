# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MessageRetrieveResponse", "Data", "DataAttachment"]


class DataAttachment(BaseModel):
    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)

    name: Optional[str] = None

    size: int


class Data(BaseModel):
    id: str

    attachment_count: int = FieldInfo(alias="attachmentCount")

    attachments: List[DataAttachment]

    from_address: Optional[str] = FieldInfo(alias="fromAddress", default=None)

    from_name: Optional[str] = FieldInfo(alias="fromName", default=None)

    has_otp: bool = FieldInfo(alias="hasOtp")

    mailbox_id: str = FieldInfo(alias="mailboxId")

    received_at: datetime = FieldInfo(alias="receivedAt")

    subject: Optional[str] = None

    text_body: Optional[str] = FieldInfo(alias="textBody", default=None)


class MessageRetrieveResponse(BaseModel):
    data: Data
