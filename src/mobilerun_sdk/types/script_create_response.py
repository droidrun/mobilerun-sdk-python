# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .script import Script
from .._models import BaseModel

__all__ = ["ScriptCreateResponse"]


class ScriptCreateResponse(BaseModel):
    data: Script
