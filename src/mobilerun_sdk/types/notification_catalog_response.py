# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["NotificationCatalogResponse", "Data", "DataEvent"]


class DataEvent(BaseModel):
    description: str

    label: str

    type: str

    toast: Optional[bool] = None


class Data(BaseModel):
    events: List[DataEvent]

    label: str

    source: str


class NotificationCatalogResponse(BaseModel):
    data: List[Data]
