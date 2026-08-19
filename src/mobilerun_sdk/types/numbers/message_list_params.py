# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Annotated

from ..._utils import PropertyInfo

from typing import Union

from datetime import datetime

__all__ = ["MessageListParams"]

class MessageListParams(TypedDict, total=False):
    direction: Literal["all", "inbound", "outbound"]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    since: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]