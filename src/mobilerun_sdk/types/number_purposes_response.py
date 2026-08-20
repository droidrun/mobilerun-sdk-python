# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["NumberPurposesResponse", "Data", "DataItem"]


class DataItem(BaseModel):
    label: str

    slug: str


class Data(BaseModel):
    items: List[DataItem]


class NumberPurposesResponse(BaseModel):
    data: Data
