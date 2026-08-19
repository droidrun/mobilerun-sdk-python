# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from pydantic import Field as FieldInfo

from typing import List

from typing_extensions import TypeAliasType, TypeAlias

__all__ = ["ApnListResponse", "ApnListResponseItem"]

class ApnListResponseItem(BaseModel):
    id: int

    apn: str

    is_preferred: bool = FieldInfo(alias = "isPreferred")

    mcc: str

    mnc: str

    name: str

    protocol: str

    roaming_protocol: str = FieldInfo(alias = "roamingProtocol")

    sub_id: int = FieldInfo(alias = "subId")

    type: str

ApnListResponse: TypeAlias = List[ApnListResponseItem]