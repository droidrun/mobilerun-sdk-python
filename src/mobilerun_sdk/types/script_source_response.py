# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .script_source import ScriptSource

__all__ = ["ScriptSourceResponse"]


class ScriptSourceResponse(BaseModel):
    data: ScriptSource
