# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FlowAction", "Overrides"]


class Overrides(BaseModel):
    params: Optional[Dict[str, Optional[object]]] = None


class FlowAction(BaseModel):
    id: str

    action_id: str = FieldInfo(alias="actionId")

    continue_on_error: bool = FieldInfo(alias="continueOnError")

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    device_id: Optional[str] = FieldInfo(alias="deviceId", default=None)

    flow_id: str = FieldInfo(alias="flowId")

    name_override: Optional[str] = FieldInfo(alias="nameOverride", default=None)

    overrides: Optional[Overrides] = None

    parent_flow_action_id: Optional[str] = FieldInfo(alias="parentFlowActionId", default=None)

    position: int
