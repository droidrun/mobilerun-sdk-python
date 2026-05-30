# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .proxy_config import ProxyConfig

__all__ = ["ProxyRetrieveResponse"]


class ProxyRetrieveResponse(BaseModel):
    data: ProxyConfig
