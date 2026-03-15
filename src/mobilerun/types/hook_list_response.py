# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .task_status import TaskStatus
from .shared.pagination_meta import PaginationMeta

__all__ = ["HookListResponse", "Item"]


class Item(BaseModel):
    service: Literal["zapier", "n8n", "make", "internal", "other"]

    url: str

    user_id: str = FieldInfo(alias="userId")

    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    events: Optional[List[TaskStatus]] = None

    state: Optional[Literal["active", "disabled", "deleted"]] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class HookListResponse(BaseModel):
    items: List[Item]
    """The paginated items"""

    pagination: PaginationMeta
    """Pagination metadata"""
