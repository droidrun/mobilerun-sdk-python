# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing_extensions import Literal

from typing import Optional

from pydantic import Field as FieldInfo

__all__ = ["TaskRunResponse"]

class TaskRunResponse(BaseModel):
    id: str
    """The ID of the task"""

    status: Literal["queued", "created", "running", "cancelling", "completed", "failed", "cancelled"]
    """The status of the task (queued or created)"""

    stream_url: Optional[str] = FieldInfo(alias = "streamUrl", default = None)
    """The URL of the stream (null when queued)"""