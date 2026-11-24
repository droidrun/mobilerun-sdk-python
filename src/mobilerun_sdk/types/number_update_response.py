# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "NumberUpdateResponse",
    "Data",
    "DataActions",
    "DataDeviceBinding",
    "DataLineCapabilities",
    "DataLineCapabilitiesSMS",
    "DataSim",
]


class DataActions(BaseModel):
    """Actions currently available for this phone number."""

    bind_device: bool = FieldInfo(alias="bindDevice")
    """
    True when this number can be bound to a cloud device (active, has a phone
    number, receives SMS, not a BYO device line). When false,
    `bindDeviceBlockedReason` says why.
    """

    bind_device_blocked_reason: Optional[
        Literal["number_not_active", "no_phone_number", "sms_inbound_unsupported", "byo_device_line"]
    ] = FieldInfo(alias="bindDeviceBlockedReason", default=None)
    """Why `bindDevice` is false; null exactly when it is true."""

    cancel: bool
    """True when DELETE /numbers/phones/{id} would cancel or abort this number now.

    False once a cancellation is already scheduled; the DELETE stays idempotent.
    """

    send: bool
    """
    True when this number passes the send gate of POST
    /numbers/phones/{id}/messages: self-service sending is switched on and the
    number is active and able to send SMS. Daily and burst limits and recipient/body
    checks still apply; the send endpoint stays the final judge.
    """


class DataDeviceBinding(BaseModel):
    """The device this number is bound to, or null."""

    bound_at: datetime = FieldInfo(alias="boundAt")

    device_id: str = FieldInfo(alias="deviceId")

    device_type: Optional[str] = FieldInfo(alias="deviceType", default=None)


class DataLineCapabilitiesSMS(BaseModel):
    inbound: bool
    """This line can receive on this channel."""

    outbound: bool
    """This line can send on this channel."""


class DataLineCapabilities(BaseModel):
    """What this line supports in principle, per channel.

    Use `actions` for what you can do right now.
    """

    sms: DataLineCapabilitiesSMS


class DataSim(BaseModel):
    """
    SIM of a phone connected through the Mobilerun Portal app; null for other phones or before the first sync.
    """

    carrier_name: Optional[str] = FieldInfo(alias="carrierName", default=None)

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    sim_slot: Optional[int] = FieldInfo(alias="simSlot", default=None)


class Data(BaseModel):
    id: str

    actions: DataActions
    """Actions currently available for this phone number."""

    cancel_at_period_end: bool = FieldInfo(alias="cancelAtPeriodEnd")

    cancellable: bool
    """Deprecated: use `actions.cancel`"""

    can_send: bool = FieldInfo(alias="canSend")
    """Deprecated: use `actions.send`"""

    capabilities: Optional[List[Literal["sms", "voice"]]] = None
    """Deprecated: use `lineCapabilities`"""

    checkout_url: Optional[str] = FieldInfo(alias="checkoutUrl", default=None)

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    current_period_end: Optional[datetime] = FieldInfo(alias="currentPeriodEnd", default=None)

    device_binding: Optional[DataDeviceBinding] = FieldInfo(alias="deviceBinding", default=None)
    """The device this number is bound to, or null."""

    failure_reason: Optional[Literal["out_of_stock", "unknown"]] = FieldInfo(alias="failureReason", default=None)
    """Why setup failed.

    Null unless state is failed, and null when the failure has no classified reason.
    out_of_stock: no number is currently available for the requested country.
    """

    iccid: Optional[str] = None
    """ICCID of the SIM behind this line when a trustworthy value is known, else null."""

    label: Optional[str] = None

    line_capabilities: DataLineCapabilities = FieldInfo(alias="lineCapabilities")
    """What this line supports in principle, per channel.

    Use `actions` for what you can do right now.
    """

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    purpose: Optional[str] = None

    sim: Optional[DataSim] = None
    """
    SIM of a phone connected through the Mobilerun Portal app; null for other phones
    or before the first sync.
    """

    state: Literal["awaiting_payment", "provisioning", "active", "cancel_scheduled", "expired", "failed"]

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class NumberUpdateResponse(BaseModel):
    data: Data
