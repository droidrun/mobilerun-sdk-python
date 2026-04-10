# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProxyConfig", "Socks5"]


class Socks5(BaseModel):
    host: str

    password: str

    port: int

    user: str


class ProxyConfig(BaseModel):
    name: Optional[str] = None

    smart_ip: Optional[bool] = FieldInfo(alias="smartIp", default=None)

    socks5: Optional[Socks5] = None

    wireguard: Optional[str] = None
