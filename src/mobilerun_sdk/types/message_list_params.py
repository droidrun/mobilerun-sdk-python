# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    direction: Literal["all", "inbound", "outbound"]

    esim_id: Annotated[str, PropertyInfo(alias="esimId")]

    number_id: Annotated[str, PropertyInfo(alias="numberId")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    peer_key: Annotated[str, PropertyInfo(alias="peerKey")]

    peer_number: Annotated[str, PropertyInfo(alias="peerNumber")]

    status: Literal[
        "all", "received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"
    ]
