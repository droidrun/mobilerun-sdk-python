# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ServerlessFunction",
    "LatestVersion",
    "LatestVersionAPIKey",
    "LatestVersionAPIKeyPermissions",
    "LatestVersionAPIKeyFull",
    "LatestVersionInspectError",
    "LatestVersionInspectErrorError",
    "LatestVersionInspectErrorErrorRepair",
    "LatestVersionManifest",
    "LatestVersionManifestCredential",
]


class LatestVersionAPIKeyPermissions(BaseModel):
    permissions: Dict[str, List[str]]


class LatestVersionAPIKeyFull(BaseModel):
    full: Literal[True]


LatestVersionAPIKey: TypeAlias = Union[LatestVersionAPIKeyPermissions, LatestVersionAPIKeyFull]


class LatestVersionInspectErrorErrorRepair(BaseModel):
    action: str

    hint: str


class LatestVersionInspectErrorError(BaseModel):
    code: str

    message: str

    line: Optional[int] = None

    repair: Optional[LatestVersionInspectErrorErrorRepair] = None


class LatestVersionInspectError(BaseModel):
    code: str

    message: str

    errors: Optional[List[LatestVersionInspectErrorError]] = None


class LatestVersionManifestCredential(BaseModel):
    name: str

    package_name: str = FieldInfo(alias="packageName")


class LatestVersionManifest(BaseModel):
    credentials: Optional[List[LatestVersionManifestCredential]] = None

    hosts: Optional[List[str]] = None

    scopes: Optional[List[str]] = None


class LatestVersion(BaseModel):
    api_key: LatestVersionAPIKey = FieldInfo(alias="apiKey")

    created_at: datetime = FieldInfo(alias="createdAt")

    function_id: str = FieldInfo(alias="functionId")

    input_schema: Optional[Dict[str, object]] = FieldInfo(alias="inputSchema", default=None)

    inspect_error: Optional[LatestVersionInspectError] = FieldInfo(alias="inspectError", default=None)

    manifest: LatestVersionManifest

    output_kind: Optional[str] = FieldInfo(alias="outputKind", default=None)

    output_schema: Optional[Dict[str, object]] = FieldInfo(alias="outputSchema", default=None)

    runtime_version: Optional[str] = FieldInfo(alias="runtimeVersion", default=None)

    sha256: str

    size_bytes: int = FieldInfo(alias="sizeBytes")

    status: Literal["pending_inspection", "ready", "rejected"]

    version: int


class ServerlessFunction(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    latest_ready_version: Optional[int] = FieldInfo(alias="latestReadyVersion", default=None)

    latest_version: Optional[LatestVersion] = FieldInfo(alias="latestVersion", default=None)

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version_count: int = FieldInfo(alias="versionCount")
