# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FileListResponse",
    "File",
    "FileCollectionStatus",
    "FileCollectionStatusUnionMember0",
    "FileCollectionStatusUnionMember0Records",
    "FileCollectionStatusUnionMember1",
    "Quota",
]


class FileCollectionStatusUnionMember0Records(BaseModel):
    reported: int

    unit: str


class FileCollectionStatusUnionMember0(BaseModel):
    completeness: Literal["complete", "partial", "none", "unknown"]

    coverage: Literal["exhaustive", "bounded", "unknown"]

    end_reached: bool = FieldInfo(alias="endReached")

    records: FileCollectionStatusUnionMember0Records

    resumable: bool

    version: Literal[1]


class FileCollectionStatusUnionMember1(BaseModel):
    completeness: Literal["unknown"]

    coverage: Literal["unknown"]

    end_reached: Literal[False] = FieldInfo(alias="endReached")

    resumable: Literal[False]

    version: Literal[1]


FileCollectionStatus: TypeAlias = Union[FileCollectionStatusUnionMember0, FileCollectionStatusUnionMember1]


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

    collection_status: Optional[FileCollectionStatus] = FieldInfo(alias="collectionStatus", default=None)


class Quota(BaseModel):
    current_bytes: int = FieldInfo(alias="currentBytes")

    quota_bytes: int = FieldInfo(alias="quotaBytes")


class FileListResponse(BaseModel):
    files: List[File]

    quota: Quota
