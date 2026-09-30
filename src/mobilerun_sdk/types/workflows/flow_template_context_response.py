# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowTemplateContextResponse", "Data", "DataLoop", "DataRoot", "DataStepReference"]


class DataLoop(BaseModel):
    context: List[str]

    item_variable_default: str = FieldInfo(alias="itemVariableDefault")

    name: str


class DataRoot(BaseModel):
    description: str

    name: str

    shape: Optional[object] = None


class DataStepReference(BaseModel):
    note: str

    pattern: str

    key_rule: Optional[str] = FieldInfo(alias="keyRule", default=None)

    slug_rule: Optional[str] = FieldInfo(alias="slugRule", default=None)


class Data(BaseModel):
    grammar: str

    loop: DataLoop

    payload_aliases: List[str] = FieldInfo(alias="payloadAliases")

    roots: List[DataRoot]

    step_reference: DataStepReference = FieldInfo(alias="stepReference")

    template_resolution_version: int = FieldInfo(alias="templateResolutionVersion")


class FlowTemplateContextResponse(BaseModel):
    data: Data
