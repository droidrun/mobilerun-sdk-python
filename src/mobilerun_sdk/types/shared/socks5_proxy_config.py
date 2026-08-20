# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Socks5ProxyConfig"]


class Socks5ProxyConfig(BaseModel):
    host: str

    name: str

    password: str

    port: int

    protocol: Literal["socks5"]

    proxy_id: str = FieldInfo(alias="proxyId")

    user: str
