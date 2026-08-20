# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.socks5_proxy_config import Socks5ProxyConfig

__all__ = ["ProxyDeleteResponse", "Data", "DataWireguardProxyConfig"]


class DataWireguardProxyConfig(BaseModel):
    config: str

    name: str

    protocol: Literal["wireguard"]

    proxy_id: str = FieldInfo(alias="proxyId")


Data: TypeAlias = Annotated[Union[Socks5ProxyConfig, DataWireguardProxyConfig], PropertyInfo(discriminator="protocol")]


class ProxyDeleteResponse(BaseModel):
    data: Data

    message: str

    success: Literal[True]
