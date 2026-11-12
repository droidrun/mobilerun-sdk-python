# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Script", "InspectError", "Manifest", "ManifestCredential"]


class InspectError(BaseModel):
    code: str

    message: str


class ManifestCredential(BaseModel):
    name: str

    package_name: str = FieldInfo(alias="packageName")


class Manifest(BaseModel):
    credentials: Optional[List[ManifestCredential]] = None

    hosts: Optional[List[str]] = None

    scopes: Optional[List[str]] = None


class Script(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: str = FieldInfo(alias="createdBy")

    dataset_key: Optional[str] = FieldInfo(alias="datasetKey", default=None)

    description: Optional[str] = None

    input_schema: Optional[Dict[str, object]] = FieldInfo(alias="inputSchema", default=None)

    inspect_error: Optional[InspectError] = FieldInfo(alias="inspectError", default=None)

    manifest: Manifest

    name: str

    output_kind: Optional[str] = FieldInfo(alias="outputKind", default=None)

    output_schema: Optional[Dict[str, object]] = FieldInfo(alias="outputSchema", default=None)

    runtime_version: Optional[str] = FieldInfo(alias="runtimeVersion", default=None)

    sha256: str

    size_bytes: int = FieldInfo(alias="sizeBytes")

    status: Literal["pending_inspection", "ready", "rejected"]

    version: int
    """Per-name version number, starting at 1 and never reused."""

    version_count: Optional[int] = FieldInfo(alias="versionCount", default=None)
    """Number of active versions of this name. Only set when listing with latest=true."""
