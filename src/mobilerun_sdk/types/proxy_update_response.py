# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .proxy_config import ProxyConfig

__all__ = ["ProxyUpdateResponse"]


class ProxyUpdateResponse(BaseModel):
    data: ProxyConfig

    message: str

    success: Literal[True]
