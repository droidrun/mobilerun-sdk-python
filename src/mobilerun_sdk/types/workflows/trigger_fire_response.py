# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TriggerFireResponse"]


class TriggerFireResponse(BaseModel):
    deduplicated: bool
    """
    True when at least one attached flow was skipped because it already had an
    execution for this (flow, invocationId). Only ever true when the client supplied
    invocationId.
    """

    enqueued_count: int = FieldInfo(alias="enqueuedCount")
    """Number of flow executions enqueued.

    May be 0 if no flows are attached to this trigger, if all attached flows are
    currently in cooldown, or if every attached flow was deduplicated.
    """

    invocation_id: str = FieldInfo(alias="invocationId")
    """
    Unique ID for this fire invocation (echoes the client-supplied invocationId, or
    a generated one). Job IDs in the execution queue are derived from it (one per
    enqueued flow).
    """
