# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from ..._utils import PropertyInfo

__all__ = ["FileDeleteParams"]

class FileDeleteParams(TypedDict, total=False):
    path: Required[str]

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]