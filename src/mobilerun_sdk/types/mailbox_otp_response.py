# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MailboxOtpResponse", "Data"]


class Data(BaseModel):
    code: str
    """String to preserve leading zeros"""

    confidence: Literal["high", "medium", "low"]

    message_id: str = FieldInfo(alias="messageId")

    received_at: datetime = FieldInfo(alias="receivedAt")

    sender: Optional[str] = None

    subject: Optional[str] = None


class MailboxOtpResponse(BaseModel):
    data: Data
