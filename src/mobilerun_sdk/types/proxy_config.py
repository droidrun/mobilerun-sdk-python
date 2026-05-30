# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.socks5 import Socks5

__all__ = ["ProxyConfig"]


class ProxyConfig(BaseModel):
    name: Optional[str] = None

    smart_ip: Optional[bool] = FieldInfo(alias="smartIp", default=None)

    socks5: Optional[Socks5] = None
