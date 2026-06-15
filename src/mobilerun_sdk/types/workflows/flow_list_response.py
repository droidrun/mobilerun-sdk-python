# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..flow import Flow
from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["FlowListResponse"]


class FlowListResponse(BaseModel):
    items: List[Flow]

    pagination: Pagination
