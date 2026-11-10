# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NumberBindResponse", "Binding", "Line", "LineCarrier"]


class Binding(BaseModel):
    bound_at: datetime = FieldInfo(alias="boundAt")

    number_id: str = FieldInfo(alias="numberId")

    phone_number: str = FieldInfo(alias="phoneNumber")


class LineCarrier(BaseModel):
    country_iso: str = FieldInfo(alias="countryIso")

    mcc: str

    mnc: str

    name: str


class Line(BaseModel):
    carrier: LineCarrier

    default_number: bool = FieldInfo(alias="defaultNumber")

    kind: Literal["simulated", "uicc", "esim", "unknown"]

    line_id: str = FieldInfo(alias="lineId")

    number_source: Literal["backend_default", "caller", "unknown"] = FieldInfo(alias="numberSource")

    state: Literal["pending", "active", "inactive", "failed", "unknown"]

    iccid: Optional[str] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)


class NumberBindResponse(BaseModel):
    binding: Binding

    line: Line

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
