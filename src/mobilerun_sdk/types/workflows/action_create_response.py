# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .action import Action
from ..._models import BaseModel

__all__ = ["ActionCreateResponse"]


class ActionCreateResponse(BaseModel):
    data: Action
