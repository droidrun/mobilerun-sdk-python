# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    created_by: Annotated[str, PropertyInfo(alias="createdBy")]
    """Only include webhooks created by this actor id. Mutually exclusive with `mine`."""

    mine: Literal["true", "false"]
    """When true, only include webhooks created by you (not just owned by your org)."""

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    search: str
    """Case-insensitive substring match against the URL or description."""

    status: Literal["active", "failing", "blocked", "disabled"]
