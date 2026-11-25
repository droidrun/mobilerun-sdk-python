# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecordingListAllParams"]


class RecordingListAllParams(TypedDict, total=False):
    cursor: str

    device_id: Annotated[str, PropertyInfo(alias="deviceId")]

    limit: int

    status: str

    type: str
