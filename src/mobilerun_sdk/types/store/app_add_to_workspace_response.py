# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

__all__ = ["AppAddToWorkspaceResponse"]

class AppAddToWorkspaceResponse(BaseModel):
    message: str

    success: Literal[True]