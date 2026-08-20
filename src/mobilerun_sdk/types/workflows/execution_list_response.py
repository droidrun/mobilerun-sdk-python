# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .flow_execution import FlowExecution
from ..shared.pagination import Pagination

__all__ = ["ExecutionListResponse", "Item"]


class Item(FlowExecution):
    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)


class ExecutionListResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
