# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from typing import Union

from datetime import datetime

from ..._utils import PropertyInfo

__all__ = ["DeliveryStatsParams"]

class DeliveryStatsParams(TypedDict, total=False):
    since: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]