# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConversationSendResponse"]


class ConversationSendResponse(BaseModel):
    assistant_text: str = FieldInfo(alias="assistantText")

    chat_session_id: str = FieldInfo(alias="chatSessionId")

    error_text: Optional[str] = FieldInfo(alias="errorText", default=None)
