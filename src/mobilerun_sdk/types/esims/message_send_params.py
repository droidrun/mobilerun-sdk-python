# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageSendParams"]


class MessageSendParams(TypedDict, total=False):
    body: Required[str]
    """
    SMS body text (max 320 chars — smaller than the admin tier's cap; see the
    schema's own doc comment for why)
    """

    to: Required[str]
    """
    Recipient phone number — normalized to E.164 (spaces/dashes/dots stripped);
    rejected with 400 if it doesn't validate as E.164 afterward.
    """

    client_request_id: Annotated[str, PropertyInfo(alias="clientRequestId")]
    """Client-supplied idempotency key, scoped to (owner, esimId, key).

    Replaying the same key + identical payload returns the original send; the same
    key with a DIFFERENT payload is a 409 conflict.
    """

    delivery_report: Annotated[bool, PropertyInfo(alias="deliveryReport")]
    """
    Wait for physedge to confirm carrier delivery before completing the send (adds
    executor-side latency, never on this request — sends are always async/202).
    Defaults to false for the public tier (opt-in, unlike the admin tier's
    default-true).
    """
