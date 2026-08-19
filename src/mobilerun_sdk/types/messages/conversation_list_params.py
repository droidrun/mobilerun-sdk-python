# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from ..._utils import PropertyInfo

from typing import Union

from datetime import datetime

__all__ = ["ConversationListParams"]

class ConversationListParams(TypedDict, total=False):
    cursor_last_message_id: Annotated[str, PropertyInfo(alias="cursorLastMessageId")]

    cursor_last_occurred_at: Annotated[Union[str, datetime], PropertyInfo(alias="cursorLastOccurredAt", format = "iso8601")]

    esim_id: Annotated[str, PropertyInfo(alias="esimId")]

    limit: int

    number_id: Annotated[str, PropertyInfo(alias="numberId")]