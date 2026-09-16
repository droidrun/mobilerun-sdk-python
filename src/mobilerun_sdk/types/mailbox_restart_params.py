# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailboxRestartParams"]


class MailboxRestartParams(TypedDict, total=False):
    billing_preference: Annotated[Literal["included", "included_only", "rent"], PropertyInfo(alias="billingPreference")]
    """
    included uses package capacity when available and otherwise starts paid
    checkout; included_only fails without creating a paid reservation when no
    included slot remains; rent always starts paid checkout.
    """
