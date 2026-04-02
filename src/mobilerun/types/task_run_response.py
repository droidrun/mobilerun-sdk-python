# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .task_status import TaskStatus

__all__ = ["TaskRunResponse"]


class TaskRunResponse(BaseModel):
    id: str
    """The ID of the task"""

    status: TaskStatus
    """The status of the task (queued or created)"""

    stream_url: Optional[str] = FieldInfo(alias="streamUrl", default=None)
    """The URL of the stream (null when queued)"""
