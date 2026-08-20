# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookEventTypesResponse", "Data", "DataSource", "DataSourceEvent", "DataSourceEventSurfaces"]


class DataSourceEventSurfaces(BaseModel):
    feed: bool

    toast: bool

    webhook: bool


class DataSourceEvent(BaseModel):
    description: str

    surfaces: DataSourceEventSurfaces

    type: str


class DataSource(BaseModel):
    events: List[DataSourceEvent]

    source: str


class Data(BaseModel):
    schema_version: Literal[1] = FieldInfo(alias="schemaVersion")

    sources: List[DataSource]


class WebhookEventTypesResponse(BaseModel):
    data: Data
