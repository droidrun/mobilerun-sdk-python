# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["ProxyConfig", "Socks5ProxyConfig", "WireguardProxyConfig"]


class Socks5ProxyConfig(BaseModel):
    host: str

    name: str

    password: str

    port: int

    protocol: Literal["socks5"]

    proxy_id: str = FieldInfo(alias="proxyId")

    user: str


class WireguardProxyConfig(BaseModel):
    config: str

    name: str

    protocol: Literal["wireguard"]

    proxy_id: str = FieldInfo(alias="proxyId")


ProxyConfig: TypeAlias = Annotated[
    Union[Socks5ProxyConfig, WireguardProxyConfig], PropertyInfo(discriminator="protocol")
]
