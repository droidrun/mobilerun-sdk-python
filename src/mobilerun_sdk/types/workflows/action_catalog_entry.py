# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ActionCatalogEntry"]


class ActionCatalogEntry(BaseModel):
    id: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    is_async: bool = FieldInfo(alias="isAsync")

    method: str

    name: str

    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"]

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    params_schema: Optional[object] = FieldInfo(alias="paramsSchema", default=None)
