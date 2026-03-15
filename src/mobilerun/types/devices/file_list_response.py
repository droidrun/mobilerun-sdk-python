# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.permission_set import PermissionSet

__all__ = ["FileListResponse", "File", "FilePermissions", "FilePermissionsSpecial"]


class FilePermissionsSpecial(BaseModel):
    set_gid: bool = FieldInfo(alias="setGid")

    set_uid: bool = FieldInfo(alias="setUid")

    sticky: bool


class FilePermissions(BaseModel):
    group: PermissionSet

    others: PermissionSet

    owner: PermissionSet

    special: FilePermissionsSpecial


class File(BaseModel):
    extended_attributes: bool = FieldInfo(alias="extendedAttributes")

    group: str

    hard_links: int = FieldInfo(alias="hardLinks")

    modified_at: datetime = FieldInfo(alias="modifiedAt")

    name: str

    owner: str

    permissions: FilePermissions

    size: int

    type: str

    symlink_target: Optional[str] = FieldInfo(alias="symlinkTarget", default=None)


class FileListResponse(BaseModel):
    files: Optional[List[File]] = None

    path: str

    total: int

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
