# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .scheduled_run import ScheduledRun

__all__ = ["ScheduledRunCancelResponse"]


class ScheduledRunCancelResponse(BaseModel):
    data: ScheduledRun
