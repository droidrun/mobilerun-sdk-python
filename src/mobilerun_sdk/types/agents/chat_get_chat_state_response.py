# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ChatGetChatStateResponse"]


class ChatGetChatStateResponse(BaseModel):
    abort_requested: bool = FieldInfo(alias="abortRequested")

    chat_active: bool = FieldInfo(alias="chatActive")

    workflow_active: bool = FieldInfo(alias="workflowActive")
