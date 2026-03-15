# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProxyConfig"]


class ProxyConfig(BaseModel):
    host: str

    name: str

    password: str

    port: int

    proxy_id: str = FieldInfo(alias="proxyId")

    user: str
