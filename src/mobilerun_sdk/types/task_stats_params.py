# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaskStatsParams"]


class TaskStatsParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Window start, ISO 8601 UTC (inclusive)."""

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Window end, ISO 8601 UTC (exclusive). At most 90 days after `from`."""

    bucket: Literal["hour", "day"]
    """Bucket size. `hour` only for windows of at most 7 days."""

    source: Optional[Literal["api", "agent"]]
    """
    Only tasks created via the API ('api') or tasks spawned by an agent step or
    created with internal=true ('agent').
    """
