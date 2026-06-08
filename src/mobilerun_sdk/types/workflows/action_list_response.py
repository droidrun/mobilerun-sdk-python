# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .action import Action
from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["ActionListResponse"]


class ActionListResponse(BaseModel):
    items: List[Action]

    pagination: Pagination
