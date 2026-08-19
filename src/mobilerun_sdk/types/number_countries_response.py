# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from pydantic import Field as FieldInfo

from typing import List

__all__ = ["NumberCountriesResponse", "Data", "DataItem"]

class DataItem(BaseModel):
    country: str

    in_stock: bool = FieldInfo(alias = "inStock")

    name: str

    plan_id: str = FieldInfo(alias = "planId")

class Data(BaseModel):
    items: List[DataItem]

class NumberCountriesResponse(BaseModel):
    data: Data