# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["DeviceCreateParams"]


class DeviceCreateParams(TypedDict, total=False):
    apps: Required[Optional[SequenceNotStr[str]]]

    files: Required[Optional[SequenceNotStr[str]]]

    x_user_id: Required[Annotated[str, PropertyInfo(alias="X-User-ID")]]

    country: str

    name: str
