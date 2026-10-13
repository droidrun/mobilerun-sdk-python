# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecordingScreenshotsResponse", "RecordingScreenshotsResponseItem"]


class RecordingScreenshotsResponseItem(BaseModel):
    id: str

    captured_at: datetime = FieldInfo(alias="capturedAt")

    size_bytes: int = FieldInfo(alias="sizeBytes")

    url: str
    """Presigned download URL, valid for 15 minutes."""


RecordingScreenshotsResponse: TypeAlias = List[RecordingScreenshotsResponseItem]
