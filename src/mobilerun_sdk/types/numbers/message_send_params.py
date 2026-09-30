# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageSendParams"]


class MessageSendParams(TypedDict, total=False):
    body: Required[str]
    """
    SMS body text, up to 1600 characters (rejected with 400 beyond that, before
    hashing). A number's own limit may be lower and is answered 422 body_too_long.
    """

    to: Required[str]
    """Recipient phone number, as E.164 or a US 10/11-digit number.

    Destinations the number cannot send to are rejected with 422
    unsupported_destination, non-numbers with 422 invalid_recipient.
    """

    client_request_id: Annotated[str, PropertyInfo(alias="clientRequestId")]
    """Deprecated: use the Idempotency-Key header instead.

    Optional idempotency key. Replaying the same key and payload returns the
    original send.
    """

    delivery_report: Annotated[bool, PropertyInfo(alias="deliveryReport")]
    """Request a delivery report. Defaults to false."""
