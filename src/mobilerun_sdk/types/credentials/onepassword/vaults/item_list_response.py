# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["ItemListResponse", "Data", "DataWebsite"]


class DataWebsite(BaseModel):
    label: str

    url: str


class Data(BaseModel):
    id: str

    category: str

    title: str

    websites: List[DataWebsite]


class ItemListResponse(BaseModel):
    data: List[Data]
