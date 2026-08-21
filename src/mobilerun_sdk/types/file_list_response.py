# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FileListResponse", "File", "Quota"]


class File(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: Literal["user", "agent", "workflow"] = FieldInfo(alias="createdBy")

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    enabled: bool

    file_id: str = FieldInfo(alias="fileId")

    filename: str

    mime_type: str = FieldInfo(alias="mimeType")

    size_bytes: float = FieldInfo(alias="sizeBytes")

    zone: Literal["user", "agent", "workflow", "skills"]


class Quota(BaseModel):
    current_bytes: int = FieldInfo(alias="currentBytes")

    quota_bytes: int = FieldInfo(alias="quotaBytes")


class FileListResponse(BaseModel):
    files: List[File]

    quota: Quota
