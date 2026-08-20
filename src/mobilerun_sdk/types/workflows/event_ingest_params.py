# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EventIngestParams"]


class EventIngestParams(TypedDict, total=False):
    event_type: Required[Annotated[str, PropertyInfo(alias="eventType")]]

    device_id: Annotated[str, PropertyInfo(alias="deviceId")]

    payload: Dict[str, object]
