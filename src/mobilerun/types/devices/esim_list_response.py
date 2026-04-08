# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EsimListResponse", "EsimListResponseItem"]


class EsimListResponseItem(BaseModel):
    carrier: str

    display_name: str = FieldInfo(alias="displayName")

    iccid: str

    is_embedded: bool = FieldInfo(alias="isEmbedded")

    slot: int

    sub_id: int = FieldInfo(alias="subId")

    type: str

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""


EsimListResponse: TypeAlias = List[EsimListResponseItem]
