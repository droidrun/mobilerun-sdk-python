# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ApprovalRespondResponse"]


class ApprovalRespondResponse(BaseModel):
    decision: Literal["approve", "deny"]
    """The recorded decision"""
