# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["ActionListResponse", "Item"]


class Item(BaseModel):
    id: str

    catalog_entry_id: str = FieldInfo(alias="catalogEntryId")

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    description: Optional[str] = None

    method: str
    """Deprecated: use uses."""

    name: str

    owner_id: str = FieldInfo(alias="ownerId")

    service: Literal[
        "tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api", "triggers_api", "sandbox_api"
    ]
    """Deprecated: use uses."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")
    """Deprecated: use ownerId (tenancy) / createdBy (actor)."""

    uses: Optional[str] = None
    """Authored step name; null when this step has no name.

    Includes hidden executable steps.
    """

    params: Optional[object] = None

    params_schema: Optional[object] = FieldInfo(alias="paramsSchema", default=None)


class ActionListResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
