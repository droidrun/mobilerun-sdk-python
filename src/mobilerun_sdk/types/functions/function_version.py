# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FunctionVersion",
    "APIKey",
    "APIKeyPermissions",
    "APIKeyFull",
    "InspectError",
    "InspectErrorError",
    "InspectErrorErrorRepair",
    "Manifest",
    "ManifestCredential",
]


class APIKeyPermissions(BaseModel):
    permissions: Dict[str, List[str]]


class APIKeyFull(BaseModel):
    full: Literal[True]


APIKey: TypeAlias = Union[APIKeyPermissions, APIKeyFull]


class InspectErrorErrorRepair(BaseModel):
    action: str

    hint: str


class InspectErrorError(BaseModel):
    code: str

    message: str

    line: Optional[int] = None

    repair: Optional[InspectErrorErrorRepair] = None


class InspectError(BaseModel):
    code: str

    message: str

    errors: Optional[List[InspectErrorError]] = None


class ManifestCredential(BaseModel):
    name: str

    package_name: str = FieldInfo(alias="packageName")


class Manifest(BaseModel):
    credentials: Optional[List[ManifestCredential]] = None

    hosts: Optional[List[str]] = None

    scopes: Optional[List[str]] = None


class FunctionVersion(BaseModel):
    api_key: APIKey = FieldInfo(alias="apiKey")

    created_at: datetime = FieldInfo(alias="createdAt")

    function_id: str = FieldInfo(alias="functionId")

    input_schema: Optional[Dict[str, object]] = FieldInfo(alias="inputSchema", default=None)

    inspect_error: Optional[InspectError] = FieldInfo(alias="inspectError", default=None)

    manifest: Manifest

    output_kind: Optional[str] = FieldInfo(alias="outputKind", default=None)

    output_schema: Optional[Dict[str, object]] = FieldInfo(alias="outputSchema", default=None)

    runtime_version: Optional[str] = FieldInfo(alias="runtimeVersion", default=None)

    sha256: str

    size_bytes: int = FieldInfo(alias="sizeBytes")

    status: Literal["pending_inspection", "ready", "rejected"]

    version: int
