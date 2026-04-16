# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .proxy_config import ProxyConfig

__all__ = ["ProxyListResponse"]


class ProxyListResponse(BaseModel):
    data: List[ProxyConfig]
