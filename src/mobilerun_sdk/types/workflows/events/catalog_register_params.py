# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CatalogRegisterParams", "Event"]


class CatalogRegisterParams(TypedDict, total=False):
    events: Required[Iterable[Event]]


class Event(TypedDict, total=False):
    event_type: Required[Annotated[str, PropertyInfo(alias="eventType")]]

    label: Required[str]

    description: str

    payload_schema: Annotated[Dict[str, Optional[object]], PropertyInfo(alias="payloadSchema")]

    source: Literal["device", "system", "webhook"]
