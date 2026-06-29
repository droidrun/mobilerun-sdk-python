# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.meta import Meta

__all__ = ["CarrierListResponse", "Item"]


class Item(BaseModel):
    id: int

    company: str

    country: str

    country_code: str

    country_iso: str

    created_at: datetime

    detail_url: str

    gsm_bands: str

    lte_bands: str

    mcc: str

    mnc: str

    mobile_prefix: str

    nsn_size: str

    number_format: str

    operator: str

    protocols: str

    umts_bands: str

    website: str

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""


class CarrierListResponse(BaseModel):
    items: Optional[List[Item]] = None

    pagination: Meta

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
