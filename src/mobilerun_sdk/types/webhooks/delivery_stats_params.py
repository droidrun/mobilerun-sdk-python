# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DeliveryStatsParams"]


class DeliveryStatsParams(TypedDict, total=False):
    kind: Literal["http", "integration"]
    """Only include deliveries to endpoints of this kind."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
