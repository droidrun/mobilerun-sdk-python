# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from pydantic import Field as FieldInfo

from typing import Optional, List

from typing_extensions import Literal

from datetime import datetime

from .shared.pagination import Pagination

__all__ = ["NumberListResponse", "Data", "DataItem"]

class DataItem(BaseModel):
    id: str

    cancel_at_period_end: bool = FieldInfo(alias = "cancelAtPeriodEnd")

    cancellable: bool

    can_send: bool = FieldInfo(alias = "canSend")

    capabilities: Optional[List[Literal["sms", "voice"]]] = None

    checkout_url: Optional[str] = FieldInfo(alias = "checkoutUrl", default = None)

    country_code: Optional[str] = FieldInfo(alias = "countryCode", default = None)

    created_at: Optional[datetime] = FieldInfo(alias = "createdAt", default = None)

    current_period_end: Optional[datetime] = FieldInfo(alias = "currentPeriodEnd", default = None)

    phone_number: Optional[str] = FieldInfo(alias = "phoneNumber", default = None)

    purpose: Optional[str] = None

    state: Literal["awaiting_payment", "provisioning", "active", "cancel_scheduled", "expired", "failed"]

    updated_at: Optional[datetime] = FieldInfo(alias = "updatedAt", default = None)

class Data(BaseModel):
    items: List[DataItem]

    pagination: Pagination

class NumberListResponse(BaseModel):
    data: Data