# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.pagination import Pagination
from .routine_file_folder import RoutineFileFolder

__all__ = ["FolderListResponse"]


class FolderListResponse(BaseModel):
    items: List[RoutineFileFolder]

    pagination: Pagination
