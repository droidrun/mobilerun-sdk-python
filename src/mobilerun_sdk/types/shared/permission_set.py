# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PermissionSet"]


class PermissionSet(BaseModel):
    execute: bool

    read: bool

    write: bool
