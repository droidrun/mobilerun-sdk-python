# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FlowVerifyParams"]


class FlowVerifyParams(TypedDict, total=False):
    invocation_id: Required[Annotated[str, PropertyInfo(alias="invocationId")]]
    """Client-supplied idempotency key.

    A repeat request for the same (flow, invocationId) returns the existing
    verification run (`deduplicated: true`, HTTP 200) instead of enqueuing another.
    """

    device_id: Annotated[str, PropertyInfo(alias="deviceId")]
    """Device to run the verification on.

    Must be one the flow is bound to. Optional only when the flow is bound to
    exactly one device (that device is used); otherwise required.
    """

    payload: Dict[str, object]
