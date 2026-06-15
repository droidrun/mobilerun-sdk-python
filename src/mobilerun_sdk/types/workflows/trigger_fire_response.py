# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TriggerFireResponse"]


class TriggerFireResponse(BaseModel):
    enqueued_count: int = FieldInfo(alias="enqueuedCount")
    """Number of flow executions enqueued.

    May be 0 if no flows are attached to this trigger, or if all attached flows are
    currently in cooldown.
    """

    invocation_id: str = FieldInfo(alias="invocationId")
    """Unique ID for this fire invocation.

    Job IDs in the execution queue are derived from it (one per enqueued flow).
    """
