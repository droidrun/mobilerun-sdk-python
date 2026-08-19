# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from pydantic import Field as FieldInfo

from typing_extensions import Literal

__all__ = ["EsimSelectorResponse", "Data", "DataItem"]

class DataItem(BaseModel):
    id: str

    carrier_name: Optional[str] = FieldInfo(alias = "carrierName", default = None)

    iccid: Optional[str] = None

    msisdn: Optional[str] = None

    name: Optional[str] = None

    source: Literal["stocked", "byo"]

    status: Literal["in_stock", "owned", "installing", "installed", "install_failed", "retired"]

class Data(BaseModel):
    items: List[DataItem]

class EsimSelectorResponse(BaseModel):
    data: Data