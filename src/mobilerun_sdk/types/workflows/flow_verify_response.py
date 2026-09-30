# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowVerifyResponse", "Data"]


class Data(BaseModel):
    deduplicated: bool
    """
    True when this run already existed for the (flow, invocationId) key (HTTP 200);
    false for a newly enqueued run (HTTP 202).
    """

    device_id: Optional[str] = FieldInfo(alias="deviceId", default=None)
    """
    Device the verification runs on; null for a device-free verification (a 0-device
    flow whose actions are all device-free allowlisted).
    """

    execution_id: str = FieldInfo(alias="executionId")

    flow_id: str = FieldInfo(alias="flowId")

    invocation_id: str = FieldInfo(alias="invocationId")

    kind: Literal["verification"]

    status: Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"]

    trigger_id: str = FieldInfo(alias="triggerId")


class FlowVerifyResponse(BaseModel):
    data: Data
