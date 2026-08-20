# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MessageSendResponse", "Data"]


class Data(BaseModel):
    id: str

    body: Optional[str] = None

    created_at: datetime = FieldInfo(alias="createdAt")

    delivery_status: Optional[str] = FieldInfo(alias="deliveryStatus", default=None)

    detected_sender: Optional[str] = FieldInfo(alias="detectedSender", default=None)

    direction: Literal["inbound", "outbound"]

    esim_id: Optional[str] = FieldInfo(alias="esimId", default=None)

    occurred_at: datetime = FieldInfo(alias="occurredAt")

    peer_key: Optional[str] = FieldInfo(alias="peerKey", default=None)

    peer_number: Optional[str] = FieldInfo(alias="peerNumber", default=None)

    provider_code: Optional[str] = FieldInfo(alias="providerCode", default=None)

    status: Literal["received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"]


class MessageSendResponse(BaseModel):
    data: Data
