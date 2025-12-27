# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TaskListResponse", "Item", "Pagination"]


class Item(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    task_id: str = FieldInfo(alias="taskId")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class Pagination(BaseModel):
    has_next: bool = FieldInfo(alias="hasNext")

    has_prev: bool = FieldInfo(alias="hasPrev")

    page: int

    pages: int

    page_size: int = FieldInfo(alias="pageSize")

    total: int


class TaskListResponse(BaseModel):
    items: Optional[List[Item]] = None

    pagination: Pagination

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
