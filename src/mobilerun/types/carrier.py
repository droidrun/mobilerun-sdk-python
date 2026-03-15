# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Carrier"]


class Carrier(BaseModel):
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
