# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from pydantic import Field as FieldInfo

from typing import Optional

__all__ = ["UserRetrieveResponse"]

class UserRetrieveResponse(BaseModel):
    """A SOCKS5 user including its password.

    Returned only on create and single-user reads.
    """
    id: str

    created_at: datetime = FieldInfo(alias = "createdAt")

    password: str

    username: str

    proxy_id: Optional[str] = FieldInfo(alias = "proxyId", default = None)
    """The proxy this user routes to (dedicated routing), or null if unbound."""