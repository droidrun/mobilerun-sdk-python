# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    status: Literal["active", "failing", "blocked", "disabled"]
