# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Socks5"]


class Socks5(BaseModel):
    host: str

    password: str

    port: int

    user: str
