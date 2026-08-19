# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from ..._utils import PropertyInfo

from typing import Dict

__all__ = ["EventDryRunParams"]

class EventDryRunParams(TypedDict, total=False):
    event_type: Required[Annotated[str, PropertyInfo(alias="eventType")]]

    device_id: Annotated[str, PropertyInfo(alias="deviceId")]

    payload: Dict[str, object]