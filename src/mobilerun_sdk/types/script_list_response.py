# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .script import Script
from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["ScriptListResponse", "Data"]


class Data(BaseModel):
    items: List[Script]

    pagination: Pagination


class ScriptListResponse(BaseModel):
    data: Data
