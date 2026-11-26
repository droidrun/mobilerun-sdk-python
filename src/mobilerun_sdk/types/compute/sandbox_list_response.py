# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = [
    "SandboxListResponse",
    "Data",
    "DataItem",
    "DataItemAPIKey",
    "DataItemAPIKeyUnionMember0",
    "DataItemAPIKeyUnionMember1",
]


class DataItemAPIKeyUnionMember0(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")

    permissions: Dict[str, List[str]]


class DataItemAPIKeyUnionMember1(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")

    full: Literal[True]


DataItemAPIKey: TypeAlias = Union[DataItemAPIKeyUnionMember0, DataItemAPIKeyUnionMember1]


class DataItem(BaseModel):
    id: str

    allowed_hosts: List[str] = FieldInfo(alias="allowedHosts")

    created_at: datetime = FieldInfo(alias="createdAt")

    expires_at: datetime = FieldInfo(alias="expiresAt")

    idle_timeout_s: int = FieldInfo(alias="idleTimeoutS")

    name: Optional[str] = None

    status: Literal["starting", "running", "stopped"]

    stopped_at: Optional[datetime] = FieldInfo(alias="stoppedAt", default=None)

    stop_reason: Optional[Literal["deleted", "idle", "timeout", "lost"]] = FieldInfo(alias="stopReason", default=None)

    used_seconds: float = FieldInfo(alias="usedSeconds")

    api_key: Optional[DataItemAPIKey] = FieldInfo(alias="apiKey", default=None)


class Data(BaseModel):
    items: List[DataItem]

    pagination: Pagination


class SandboxListResponse(BaseModel):
    data: Data
