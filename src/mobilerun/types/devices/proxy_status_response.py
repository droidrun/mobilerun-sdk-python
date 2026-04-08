# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProxyStatusResponse", "Tunnel"]


class Tunnel(BaseModel):
    """WireGuard tunnel details."""

    name: str

    state: str


class ProxyStatusResponse(BaseModel):
    connected: bool

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    protocol: Optional[str] = None
    """Active proxy protocol (socks5 or wireguard)."""

    tunnel: Optional[Tunnel] = None
    """WireGuard tunnel details."""
