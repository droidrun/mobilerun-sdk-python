# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowRunResponse", "Data"]


class Data(BaseModel):
    enqueued_count: int = FieldInfo(alias="enqueuedCount")

    execution_ids: List[str] = FieldInfo(alias="executionIds")
    """Ids of the executions this run created.

    An idempotent replay returns the ids of the original run.
    """


class FlowRunResponse(BaseModel):
    data: Data
