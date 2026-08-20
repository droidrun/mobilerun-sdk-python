# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CatalogRetrieveResponse", "Data", "DataPayloadSchema"]


class DataPayloadSchema(BaseModel):
    description: str

    name: str

    type: Literal["string", "number", "boolean", "object", "array"]

    example: Optional[object] = None


class Data(BaseModel):
    app_event_type: str = FieldInfo(alias="appEventType")

    app_name: str = FieldInfo(alias="appName")

    category: Literal["app", "system", "device", "webhook"]

    label: str

    package_name: Optional[str] = FieldInfo(alias="packageName", default=None)

    payload_schema: List[DataPayloadSchema] = FieldInfo(alias="payloadSchema")

    source_event_type: str = FieldInfo(alias="sourceEventType")


class CatalogRetrieveResponse(BaseModel):
    data: Data
