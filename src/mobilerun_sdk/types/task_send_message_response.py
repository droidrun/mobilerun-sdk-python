# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TaskSendMessageResponse"]


class TaskSendMessageResponse(BaseModel):
    sent: bool
    """Whether the message was queued for delivery"""
