# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScriptSource"]


class ScriptSource(BaseModel):
    script_id: str = FieldInfo(alias="scriptId")

    sha256: str

    size_bytes: int = FieldInfo(alias="sizeBytes")

    source: str
