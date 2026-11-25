# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TaskStatsResponse", "Bucket", "DurationSeconds", "TopFailure", "Totals"]


class Bucket(BaseModel):
    cancelled: int

    failed: int

    running: int
    """Tasks not finished yet (prepared, queued, created, running, cancelling)"""

    start: datetime
    """Bucket start (UTC, floored to the bucket size)"""

    succeeded: int


class DurationSeconds(BaseModel):
    """finishedAt - claimedAt of finished tasks created in the window"""

    p50: Optional[float] = None
    """Median seconds from claim to finish"""

    p95: Optional[float] = None
    """95th percentile seconds from claim to finish"""


class TopFailure(BaseModel):
    count: int

    message: str
    """Failure message: first line, trimmed, max 80 chars"""


class Totals(BaseModel):
    cancelled: int

    failed: int

    running: int
    """Tasks not finished yet (prepared, queued, created, running, cancelling)"""

    succeeded: int

    success_rate: Optional[float] = FieldInfo(alias="successRate", default=None)
    """succeeded / (succeeded + failed); null when nothing finished"""


class TaskStatsResponse(BaseModel):
    bucket: Literal["hour", "day"]

    buckets: List[Bucket]
    """Every bucket in the window, zero-filled"""

    duration_seconds: DurationSeconds = FieldInfo(alias="durationSeconds")
    """finishedAt - claimedAt of finished tasks created in the window"""

    from_: datetime = FieldInfo(alias="from")
    """Window start (UTC, inclusive)"""

    to: datetime
    """Window end (UTC, exclusive)"""

    top_failures: List[TopFailure] = FieldInfo(alias="topFailures")
    """Up to 5 most common failure messages"""

    totals: Totals
