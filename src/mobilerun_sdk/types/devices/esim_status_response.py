# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EsimStatusResponse", "EsimStatusResponseItem"]


class EsimStatusResponseItem(BaseModel):
    carrier: str

    data_roaming_enabled: bool = FieldInfo(alias="dataRoamingEnabled")

    data_state: str = FieldInfo(alias="dataState")

    is_roaming: bool = FieldInfo(alias="isRoaming")

    mobile_data_enabled: bool = FieldInfo(alias="mobileDataEnabled")

    network_type: str = FieldInfo(alias="networkType")

    operator: str

    phone_type: str = FieldInfo(alias="phoneType")

    sim_state: str = FieldInfo(alias="simState")

    sub_id: int = FieldInfo(alias="subId")


EsimStatusResponse: TypeAlias = List[EsimStatusResponseItem]
