# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NumberCountriesResponse", "Data", "DataItem"]


class DataItem(BaseModel):
    country: str

    in_stock: bool = FieldInfo(alias="inStock")

    name: str

    plan_id: str = FieldInfo(alias="planId")


class Data(BaseModel):
    items: List[DataItem]


class NumberCountriesResponse(BaseModel):
    data: Data
