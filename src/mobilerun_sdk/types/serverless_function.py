# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .functions.function_version import FunctionVersion

__all__ = ["ServerlessFunction"]


class ServerlessFunction(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    latest_ready_version: Optional[int] = FieldInfo(alias="latestReadyVersion", default=None)

    latest_version: Optional[FunctionVersion] = FieldInfo(alias="latestVersion", default=None)

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version_count: int = FieldInfo(alias="versionCount")
