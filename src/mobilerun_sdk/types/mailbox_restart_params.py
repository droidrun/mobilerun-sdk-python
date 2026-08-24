# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailboxRestartParams"]


class MailboxRestartParams(TypedDict, total=False):
    billing_preference: Annotated[Literal["included", "rent"], PropertyInfo(alias="billingPreference")]
    """Funding preference.

    Omit or use included for included-first activation; rent always preserves
    package capacity and starts paid checkout.
    """
