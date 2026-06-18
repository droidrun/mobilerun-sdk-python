# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookEventTypesResponse", "Data", "DataSource", "DataSourceEvent"]


class DataSourceEvent(BaseModel):
    description: str

    type: str


class DataSource(BaseModel):
    events: List[DataSourceEvent]

    source: str


class Data(BaseModel):
    schema_version: float = FieldInfo(alias="schemaVersion")

    sources: List[DataSource]


class WebhookEventTypesResponse(BaseModel):
    data: Data
