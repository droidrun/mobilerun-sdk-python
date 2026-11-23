# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RoutineFile"]


class RoutineFile(BaseModel):
    id: str

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    execution_id: str = FieldInfo(alias="executionId")

    filename: str

    flow_deleted: bool = FieldInfo(alias="flowDeleted")
    """
    True when the routine no longer exists (replaced by a deploy, or deleted before
    its files were deleted with it). Its files stay until you delete them.
    """

    flow_id: str = FieldInfo(alias="flowId")

    flow_name: Optional[str] = FieldInfo(alias="flowName", default=None)
    """Null when the routine no longer exists."""

    folder: str
    """Canonical folder the file was saved under, for example "/Exports/241109"."""

    kind: Literal["recording", "screenshot", "file"]

    mime_type: str = FieldInfo(alias="mimeType")

    size_bytes: int = FieldInfo(alias="sizeBytes")
