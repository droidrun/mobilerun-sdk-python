# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FunctionSource"]


class FunctionSource(BaseModel):
    function_id: str = FieldInfo(alias="functionId")

    sha256: str

    size_bytes: int = FieldInfo(alias="sizeBytes")

    source: str
