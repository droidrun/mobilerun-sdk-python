# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowRunResponse", "Data", "DataSkipped"]


class DataSkipped(BaseModel):
    """
    Why no execution was admitted: device_required means no device and actions are not device-free eligible; flow_disabled means disabled at admission; flow_unavailable means missing or archived at admission. Blocked flows keep their existing error response. Manual runs bypass trigger conditions.
    """

    reason: Literal["device_required", "flow_disabled", "flow_unavailable"]


class Data(BaseModel):
    enqueued_count: int = FieldInfo(alias="enqueuedCount")

    execution_ids: List[str] = FieldInfo(alias="executionIds")
    """Ids of the executions this run created.

    An idempotent replay returns the ids of the original run.
    """

    enqueue_failed: Optional[Literal[True]] = FieldInfo(alias="enqueueFailed", default=None)
    """At least one admitted execution failed queue submission.

    This is an enqueue error, not a skip. Keyed runs report prepared executions;
    post-commit submission failures are recorded on the execution instead.
    """

    skipped: Optional[DataSkipped] = None
    """
    Why no execution was admitted: device_required means no device and actions are
    not device-free eligible; flow_disabled means disabled at admission;
    flow_unavailable means missing or archived at admission. Blocked flows keep
    their existing error response. Manual runs bypass trigger conditions.
    """


class FlowRunResponse(BaseModel):
    data: Data
