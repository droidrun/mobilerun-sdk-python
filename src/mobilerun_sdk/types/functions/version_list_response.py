# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .function_version import FunctionVersion
from ..shared.pagination import Pagination

__all__ = ["VersionListResponse", "Data"]


class Data(BaseModel):
    items: List[Optional[FunctionVersion]]

    pagination: Pagination


class VersionListResponse(BaseModel):
    data: Data
