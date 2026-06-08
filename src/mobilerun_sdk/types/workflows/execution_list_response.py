# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .flow_execution import FlowExecution
from ..shared.pagination import Pagination

__all__ = ["ExecutionListResponse"]


class ExecutionListResponse(BaseModel):
    items: List[FlowExecution]

    pagination: Pagination
