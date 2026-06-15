# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .user_secret import UserSecret

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    data: List[UserSecret]
