# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .routine_file import RoutineFile
from .shared.pagination import Pagination

__all__ = ["RoutineFileListResponse"]


class RoutineFileListResponse(BaseModel):
    items: List[RoutineFile]

    pagination: Pagination
