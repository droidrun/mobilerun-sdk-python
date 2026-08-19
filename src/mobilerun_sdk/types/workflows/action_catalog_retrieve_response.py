# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from pydantic import Field as FieldInfo

from typing_extensions import Literal

__all__ = ["ActionCatalogRetrieveResponse", "Data"]

class Data(BaseModel):
    id: str

    created_at: Optional[str] = FieldInfo(alias = "createdAt", default = None)

    description: Optional[str] = None

    method: str

    name: str

    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"]

    updated_at: Optional[str] = FieldInfo(alias = "updatedAt", default = None)

    params_schema: Optional[object] = FieldInfo(alias = "paramsSchema", default = None)

class ActionCatalogRetrieveResponse(BaseModel):
    data: Data