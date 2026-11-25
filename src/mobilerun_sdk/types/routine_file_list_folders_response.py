# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["RoutineFileListFoldersResponse", "Item", "ItemFlow"]


class ItemFlow(BaseModel):
    flow_deleted: bool = FieldInfo(alias="flowDeleted")

    flow_id: str = FieldInfo(alias="flowId")

    flow_name: Optional[str] = FieldInfo(alias="flowName", default=None)


class Item(BaseModel):
    file_count: int = FieldInfo(alias="fileCount")

    flows: List[ItemFlow]

    folder: str

    last_created_at: Optional[datetime] = FieldInfo(alias="lastCreatedAt", default=None)

    size_bytes: int = FieldInfo(alias="sizeBytes")


class RoutineFileListFoldersResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
