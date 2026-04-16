# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.meta import Meta

__all__ = ["TaskListResponse", "Item"]


class Item(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    task_id: str = FieldInfo(alias="taskId")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class TaskListResponse(BaseModel):
    items: Optional[List[Item]] = None

    pagination: Meta

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
