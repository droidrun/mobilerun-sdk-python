# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FunctionRunSummary", "APIKey", "APIKeyUnionMember0", "APIKeyUnionMember1"]


class APIKeyUnionMember0(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")

    permissions: Dict[str, List[str]]


class APIKeyUnionMember1(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")

    full: Literal[True]


APIKey: TypeAlias = Union[APIKeyUnionMember0, APIKeyUnionMember1]


class FunctionRunSummary(BaseModel):
    id: str

    duration_ms: Optional[int] = FieldInfo(alias="durationMs", default=None)

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)

    error_code: Optional[
        Literal[
            "function_error",
            "input_invalid",
            "timeout",
            "cancelled",
            "sandbox_lost",
            "sandbox_start_failed",
            "function_not_found",
            "internal_error",
            "output_invalid",
            "result_too_large",
            "state_too_large",
            "dataset_too_large",
            "executor_unavailable",
        ]
    ] = FieldInfo(alias="errorCode", default=None)

    function_id: str = FieldInfo(alias="functionId")

    logs: Literal["none", "pending", "available", "gone"]

    outcome: Optional[Literal["succeeded", "partial", "failed"]] = None

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    status: Literal["running", "done", "failed"]

    used_seconds: Optional[int] = FieldInfo(alias="usedSeconds", default=None)

    version: int

    api_key: Optional[APIKey] = FieldInfo(alias="apiKey", default=None)
