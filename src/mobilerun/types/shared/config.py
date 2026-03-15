# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Config"]


class Config(BaseModel):
    host: str

    password: str

    port: int

    user: str
