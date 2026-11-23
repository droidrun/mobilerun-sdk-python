# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .sandbox import Sandbox
from ..._models import BaseModel

__all__ = ["SandboxCreateResponse"]


class SandboxCreateResponse(BaseModel):
    data: Sandbox
