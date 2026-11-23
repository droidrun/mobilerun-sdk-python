# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .sandboxes.sandbox_command import SandboxCommand

__all__ = ["SandboxExecResponse"]


class SandboxExecResponse(BaseModel):
    data: SandboxCommand
