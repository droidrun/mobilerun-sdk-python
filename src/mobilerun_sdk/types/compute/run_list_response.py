# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.pagination import Pagination
from .function_run_summary import FunctionRunSummary

__all__ = ["RunListResponse", "Data"]


class Data(BaseModel):
    items: List[FunctionRunSummary]

    pagination: Pagination


class RunListResponse(BaseModel):
    data: Data
