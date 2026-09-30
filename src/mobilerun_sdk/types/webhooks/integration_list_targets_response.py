# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IntegrationListTargetsResponse", "Data"]


class Data(BaseModel):
    args: Dict[str, object]
    """Pass as `args` when creating an `integration` webhook."""

    is_private: bool = FieldInfo(alias="isPrivate")

    label: str


class IntegrationListTargetsResponse(BaseModel):
    data: List[Data]
