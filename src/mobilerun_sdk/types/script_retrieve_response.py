# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .script import Script
from .._models import BaseModel

__all__ = ["ScriptRetrieveResponse"]


class ScriptRetrieveResponse(BaseModel):
    data: Script
