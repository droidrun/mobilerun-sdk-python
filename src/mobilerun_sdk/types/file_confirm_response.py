# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FileConfirmResponse"]


class FileConfirmResponse(BaseModel):
    actual_size_bytes: float = FieldInfo(alias="actualSizeBytes")

    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: Literal["user", "agent", "workflow"] = FieldInfo(alias="createdBy")

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    enabled: bool

    file_id: str = FieldInfo(alias="fileId")

    filename: str

    mime_type: str = FieldInfo(alias="mimeType")

    size_bytes: float = FieldInfo(alias="sizeBytes")

    state: Literal["ready"]

    zone: Literal["user", "agent", "workflow", "skills"]
