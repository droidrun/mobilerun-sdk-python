# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    direction: Literal["all", "inbound", "outbound"]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
