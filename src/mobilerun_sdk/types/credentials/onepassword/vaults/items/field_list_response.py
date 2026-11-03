# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = ["FieldListResponse", "Data"]


class Data(BaseModel):
    id: str

    field_type: str = FieldInfo(alias="fieldType")

    title: str

    section_id: Optional[str] = FieldInfo(alias="sectionId", default=None)


class FieldListResponse(BaseModel):
    data: List[Data]
