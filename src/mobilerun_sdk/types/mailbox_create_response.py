# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MailboxCreateResponse", "Data", "DataInboundMessages"]


class DataInboundMessages(BaseModel):
    exhausted: bool

    included: int

    resets_at: Optional[datetime] = FieldInfo(alias="resetsAt", default=None)

    used: int


class Data(BaseModel):
    id: str

    address: Optional[str] = None

    billing_mode: Literal["rent", "included"] = FieldInfo(alias="billingMode")

    cancel_at_period_end: bool = FieldInfo(alias="cancelAtPeriodEnd")

    checkout_expires_at: Optional[datetime] = FieldInfo(alias="checkoutExpiresAt", default=None)

    checkout_url: Optional[str] = FieldInfo(alias="checkoutUrl", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    current_period_end: Optional[datetime] = FieldInfo(alias="currentPeriodEnd", default=None)

    inbound_messages: DataInboundMessages = FieldInfo(alias="inboundMessages")

    label: Optional[str] = None

    status: Literal["provisioning", "awaiting_payment", "active", "cancel_scheduled", "archived", "billing_error"]


class MailboxCreateResponse(BaseModel):
    data: Data
