# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.permission_set import PermissionSet

__all__ = ["FileInfo", "Permissions", "PermissionsSpecial"]


class PermissionsSpecial(BaseModel):
    set_gid: bool = FieldInfo(alias="setGid")

    set_uid: bool = FieldInfo(alias="setUid")

    sticky: bool


class Permissions(BaseModel):
    group: PermissionSet

    others: PermissionSet

    owner: PermissionSet

    special: PermissionsSpecial


class FileInfo(BaseModel):
    extended_attributes: bool = FieldInfo(alias="extendedAttributes")

    group: str

    hard_links: int = FieldInfo(alias="hardLinks")

    modified_at: datetime = FieldInfo(alias="modifiedAt")

    name: str

    owner: str

    permissions: Permissions

    size: int

    type: str

    symlink_target: Optional[str] = FieldInfo(alias="symlinkTarget", default=None)
