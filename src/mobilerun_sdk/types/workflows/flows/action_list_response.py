# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ActionListResponse", "Data", "DataOverrides"]


class DataOverrides(BaseModel):
    params: Optional[Dict[str, object]] = None


class Data(BaseModel):
    id: str

    action_id: str = FieldInfo(alias="actionId")

    continue_on_error: bool = FieldInfo(alias="continueOnError")

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    flow_id: str = FieldInfo(alias="flowId")

    name_override: Optional[str] = FieldInfo(alias="nameOverride", default=None)

    overrides: Optional[DataOverrides] = None

    parent_flow_action_id: Optional[str] = FieldInfo(alias="parentFlowActionId", default=None)

    position: int


class ActionListResponse(BaseModel):
    data: List[Data]
