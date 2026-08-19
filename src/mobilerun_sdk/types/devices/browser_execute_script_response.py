# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from pydantic import Field as FieldInfo

__all__ = ["BrowserExecuteScriptResponse"]

class BrowserExecuteScriptResponse(BaseModel):
    result: object
    """JSON-serialized return value of the script (null if it returned undefined).

    Non-JSON-serializable numbers (Infinity, NaN, -0) are returned as their string
    representation.
    """

    schema_: Optional[str] = FieldInfo(alias = "$schema", default = None)
    """A URL to the JSON Schema for this object."""