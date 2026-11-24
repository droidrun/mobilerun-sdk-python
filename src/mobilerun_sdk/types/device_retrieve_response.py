# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DeviceRetrieveResponse"]


class DeviceRetrieveResponse(BaseModel):
    id: str

    active_task_id: str = FieldInfo(alias="activeTaskId")

    assigned_at: Optional[datetime] = FieldInfo(alias="assignedAt", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    platform: Literal["android", "ios"]
    """Operating system the device runs."""

    state: str

    state_message: str = FieldInfo(alias="stateMessage")

    stream_url: str = FieldInfo(alias="streamUrl")

    task_count: int = FieldInfo(alias="taskCount")

    terminates_at: Optional[datetime] = FieldInfo(alias="terminatesAt", default=None)

    type: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    billing_strategy: Optional[str] = FieldInfo(alias="billingStrategy", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    idle_timeout_default_minutes: Optional[int] = FieldInfo(alias="idleTimeoutDefaultMinutes", default=None)
    """
    The platform default idle timeout this device uses when its own setting is
    cleared (PUT idle-timeout with minutes null). Omitted when no default applies to
    this device.
    """

    idle_timeout_minutes: Optional[int] = FieldInfo(alias="idleTimeoutMinutes", default=None)
    """
    The effective idle timeout: minutes without client activity after which the
    device is stopped automatically (state stopped, stopReason IDLE_TIMEOUT). It is
    the device's own setting when one exists, otherwise the platform default for
    pay-as-you-go (minute-billed) devices that can be stopped. Omitted while no idle
    timer applies (explicitly turned off, or no default for this device). Change it
    with PUT /devices/{deviceId}/idle-timeout.
    """

    idle_timeout_source: Optional[Literal["device", "default"]] = FieldInfo(alias="idleTimeoutSource", default=None)
    """
    Where idleTimeoutMinutes comes from: device = the device's own setting (also
    when it is off), default = the platform default. Omitted when no idle timer can
    apply.
    """

    last_activity_at: Optional[datetime] = FieldInfo(alias="lastActivityAt", default=None)
    """When the device last had client activity (RFC 3339).

    Tracked only while the idle timer is on, to about one minute of precision;
    omitted otherwise.
    """

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    provider_id: Optional[str] = FieldInfo(alias="providerId", default=None)

    stop_reason: Optional[
        Literal[
            "STOP_REQUESTED",
            "MINUTE_BALANCE_EXHAUSTED",
            "RESOURCE_EXHAUSTED",
            "SUBSCRIPTION_REQUIRED",
            "PAYMENT_REQUIRED",
            "DEVICE_OPERATION_FAILED",
            "DEVICE_LEFT",
            "IDLE_TIMEOUT",
        ]
    ] = FieldInfo(alias="stopReason", default=None)
    """Why the device was last stopped.

    Present only while state is stopped; clients should use this value instead of
    parsing stateMessage.
    """

    stop_reason_at: Optional[datetime] = FieldInfo(alias="stopReasonAt", default=None)
    """When devices-api recorded the stop reason (RFC 3339).

    Present only while state is stopped and a reason is recorded.
    """

    stream_token: Optional[str] = FieldInfo(alias="streamToken", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Deprecated: use ownerId/createdBy."""
