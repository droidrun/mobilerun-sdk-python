# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .sandbox import Sandbox
from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["SandboxListResponse", "Data"]


class Data(BaseModel):
    items: List[Sandbox]

    pagination: Pagination


class SandboxListResponse(BaseModel):
    data: Data
