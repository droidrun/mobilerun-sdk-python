# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .user_secret import UserSecret

__all__ = ["SecretCreateResponse"]


class SecretCreateResponse(BaseModel):
    data: UserSecret
