# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserUpdateResponse"]


class UserUpdateResponse(BaseModel):
    """A SOCKS5 credential without its password."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    username: str

    proxy_id: Optional[str] = FieldInfo(alias="proxyId", default=None)
    """The proxy this user routes to (dedicated routing), or null if unbound."""
