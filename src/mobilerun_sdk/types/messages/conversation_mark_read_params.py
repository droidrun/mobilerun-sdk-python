# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationMarkReadParams"]


class ConversationMarkReadParams(TypedDict, total=False):
    peer_key: Required[Annotated[str, PropertyInfo(alias="peerKey")]]
    """The thread's canonical peer key (see GET .../conversations)"""

    up_to_message_id: Required[Annotated[str, PropertyInfo(alias="upToMessageId")]]

    up_to_occurred_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="upToOccurredAt", format="iso8601")]]
    """
    Mark inbound messages read up to (and including) this occurredAt/upToMessageId
    cursor
    """
