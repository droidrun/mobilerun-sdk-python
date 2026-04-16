# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .task import Task
from .._models import BaseModel
from .shared.pagination_meta import PaginationMeta

__all__ = ["TaskListResponse"]


class TaskListResponse(BaseModel):
    items: List[Task]
    """The paginated items"""

    pagination: PaginationMeta
    """Pagination metadata"""
