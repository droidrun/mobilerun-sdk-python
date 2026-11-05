# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageRetrieveParams"]


class MessageRetrieveParams(TypedDict, total=False):
    mailbox_id: Required[Annotated[str, PropertyInfo(alias="mailboxId")]]

    include_html: Annotated[Literal["true", "false"], PropertyInfo(alias="includeHtml")]
    """Return the raw HTML part as htmlBody (untrusted; render isolated)."""
