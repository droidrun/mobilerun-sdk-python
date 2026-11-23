# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .sandbox_command import SandboxCommand

__all__ = ["CommandRetrieveResponse"]


class CommandRetrieveResponse(BaseModel):
    data: SandboxCommand
