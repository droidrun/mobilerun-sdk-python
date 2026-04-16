# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["UsageResult"]


class UsageResult(BaseModel):
    request_tokens: int

    requests: int

    response_tokens: int

    total_tokens: int
