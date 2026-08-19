# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Dict

from pydantic import Field as FieldInfo

__all__ = ["ActionAddResponse", "Data", "DataOverrides"]

class DataOverrides(BaseModel):
    params: Optional[Dict[str, object]] = None

class Data(BaseModel):
    id: str

    action_id: str = FieldInfo(alias = "actionId")

    continue_on_error: bool = FieldInfo(alias = "continueOnError")

    created_at: Optional[str] = FieldInfo(alias = "createdAt", default = None)

    flow_id: str = FieldInfo(alias = "flowId")

    name_override: Optional[str] = FieldInfo(alias = "nameOverride", default = None)

    overrides: Optional[DataOverrides] = None

    parent_flow_action_id: Optional[str] = FieldInfo(alias = "parentFlowActionId", default = None)

    position: int

class ActionAddResponse(BaseModel):
    data: Data