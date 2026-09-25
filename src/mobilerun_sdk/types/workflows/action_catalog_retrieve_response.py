# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ActionCatalogRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    method: str

    name: str

    provider: Literal["mobilerun", "oneDrive", "googleDrive"]

    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api"]

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    output_schema: Optional[object] = FieldInfo(alias="outputSchema", default=None)

    params_schema: Optional[object] = FieldInfo(alias="paramsSchema", default=None)


class ActionCatalogRetrieveResponse(BaseModel):
    data: Data
