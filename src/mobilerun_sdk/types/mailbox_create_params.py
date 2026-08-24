# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailboxCreateParams"]


class MailboxCreateParams(TypedDict, total=False):
    client_request_id: Required[Annotated[str, PropertyInfo(alias="clientRequestId")]]

    billing_preference: Annotated[Literal["included", "rent"], PropertyInfo(alias="billingPreference")]
    """Funding preference.

    Omit or use included for included-first activation; rent always preserves
    package capacity and starts paid checkout.
    """

    label: str

    local_part: Annotated[str, PropertyInfo(alias="localPart")]
    """Optional full mailbox local part (the address before "@").

    Trimmed and lowercased before validation. Omit for a random, non-guessable
    mx\\__-prefixed address.
    """
