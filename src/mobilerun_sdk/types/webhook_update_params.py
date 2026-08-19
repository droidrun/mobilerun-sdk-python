# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from typing import Optional

from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]

class WebhookUpdateParams(TypedDict, total=False):
    description: Optional[str]

    event_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="eventTypes")]

    state: Literal["ACTIVE", "DISABLED"]