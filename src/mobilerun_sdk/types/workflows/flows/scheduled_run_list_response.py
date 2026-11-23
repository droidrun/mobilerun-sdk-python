# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .scheduled_run import ScheduledRun
from ...shared.pagination import Pagination

__all__ = ["ScheduledRunListResponse"]


class ScheduledRunListResponse(BaseModel):
    items: List[ScheduledRun]

    pagination: Pagination
