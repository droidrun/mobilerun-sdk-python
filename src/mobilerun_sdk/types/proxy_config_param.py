# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.socks5 import Socks5

__all__ = ["ProxyConfigParam"]


class ProxyConfigParam(TypedDict, total=False):
    name: str

    smart_ip: Annotated[bool, PropertyInfo(alias="smartIp")]

    socks5: Socks5
