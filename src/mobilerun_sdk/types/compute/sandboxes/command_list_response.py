# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .sandbox_command_summary import SandboxCommandSummary

__all__ = ["CommandListResponse", "Data"]


class Data(BaseModel):
    items: List[SandboxCommandSummary]


class CommandListResponse(BaseModel):
    data: Data
