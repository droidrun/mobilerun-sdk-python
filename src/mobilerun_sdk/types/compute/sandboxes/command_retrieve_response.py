# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CommandRetrieveResponse", "Data"]


class Data(BaseModel):
    command_id: str = FieldInfo(alias="commandId")

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    exit_code: Optional[int] = FieldInfo(alias="exitCode", default=None)

    started_at: datetime = FieldInfo(alias="startedAt")

    status: Literal["running", "exited"]

    stderr: str

    stdout: str

    timed_out: bool = FieldInfo(alias="timedOut")

    truncated: bool


class CommandRetrieveResponse(BaseModel):
    data: Data
