# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FileConfirmResponse",
    "CollectionStatus",
    "CollectionStatusUnionMember0",
    "CollectionStatusUnionMember0Records",
    "CollectionStatusUnionMember1",
]


class CollectionStatusUnionMember0Records(BaseModel):
    reported: int

    unit: str


class CollectionStatusUnionMember0(BaseModel):
    completeness: Literal["complete", "partial", "none", "unknown"]

    coverage: Literal["exhaustive", "bounded", "unknown"]

    end_reached: bool = FieldInfo(alias="endReached")

    records: CollectionStatusUnionMember0Records

    resumable: bool

    version: Literal[1]


class CollectionStatusUnionMember1(BaseModel):
    completeness: Literal["unknown"]

    coverage: Literal["unknown"]

    end_reached: Literal[False] = FieldInfo(alias="endReached")

    resumable: Literal[False]

    version: Literal[1]


CollectionStatus: TypeAlias = Union[CollectionStatusUnionMember0, CollectionStatusUnionMember1]


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

    collection_status: Optional[CollectionStatus] = FieldInfo(alias="collectionStatus", default=None)
