# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailboxCreateParams"]


class MailboxCreateParams(TypedDict, total=False):
    client_request_id: Required[Annotated[str, PropertyInfo(alias="clientRequestId")]]

    billing_preference: Annotated[Literal["included", "included_only", "rent"], PropertyInfo(alias="billingPreference")]
    """
    included uses package capacity when available and otherwise starts paid
    checkout; included_only fails without creating a paid reservation when no
    included slot remains; rent always starts paid checkout.
    """

    domain_id: Annotated[str, PropertyInfo(alias="domainId")]
    """Optional active custom mailbox domain owned by the caller.

    Omit to use the system domain.
    """

    label: str

    local_part: Annotated[str, PropertyInfo(alias="localPart")]
    """Optional mailbox name before the "@". Omit to generate a random address."""
