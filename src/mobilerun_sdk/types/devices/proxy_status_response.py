# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProxyStatusResponse"]


class ProxyStatusResponse(BaseModel):
    connected: bool

    name: Optional[str] = None
    """Active proxy name"""

    protocol: Optional[str] = None
    """Active proxy protocol (socks5)."""

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
