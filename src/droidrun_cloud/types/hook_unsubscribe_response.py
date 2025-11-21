# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["HookUnsubscribeResponse"]


class HookUnsubscribeResponse(BaseModel):
    id: str
    """The subscription ID"""

    unsubscribed: bool
    """Whether unsubscription was successful"""
