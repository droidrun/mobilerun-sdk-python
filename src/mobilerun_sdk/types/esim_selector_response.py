# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["EsimSelectorResponse", "Item"]


class Item(BaseModel):
    id: str

    carrier_name: Optional[str] = FieldInfo(alias="carrierName", default=None)

    iccid: Optional[str] = None

    msisdn: Optional[str] = None

    name: Optional[str] = None

    source: Literal["stocked", "byo"]

    status: Literal["in_stock", "owned", "installing", "installed", "install_failed", "retired"]


class EsimSelectorResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
