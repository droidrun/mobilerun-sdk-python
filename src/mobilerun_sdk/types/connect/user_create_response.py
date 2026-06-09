# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserCreateResponse"]


class UserCreateResponse(BaseModel):
    """A SOCKS5 user including its password.

    Returned only on create and single-user reads.
    """

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    password: str

    username: str

    proxy_id: Optional[str] = FieldInfo(alias="proxyId", default=None)
    """The proxy this user routes to (dedicated routing), or null if unbound."""
