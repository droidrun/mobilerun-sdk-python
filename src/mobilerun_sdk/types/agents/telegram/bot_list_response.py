# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BotListResponse", "Bot"]


class Bot(BaseModel):
    id: str

    bot_username: str = FieldInfo(alias="botUsername")

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    last_message_at: Optional[datetime] = FieldInfo(alias="lastMessageAt", default=None)

    link_code_expires_at: Optional[datetime] = FieldInfo(alias="linkCodeExpiresAt", default=None)

    owner_telegram_user_id: Optional[int] = FieldInfo(alias="ownerTelegramUserId", default=None)

    status: Literal["pending", "active", "disabled"]


class BotListResponse(BaseModel):
    bots: List[Bot]
