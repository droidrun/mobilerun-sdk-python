# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

__all__ = ["NumberPurposesResponse", "Data", "DataItem"]

class DataItem(BaseModel):
    label: str

    slug: str

class Data(BaseModel):
    items: List[DataItem]

class NumberPurposesResponse(BaseModel):
    data: Data