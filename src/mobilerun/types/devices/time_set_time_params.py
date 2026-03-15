# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TimeSetTimeParams"]


class TimeSetTimeParams(TypedDict, total=False):
    time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
