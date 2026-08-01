# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .file_info import FileInfo

__all__ = ["FileListResponse"]


class FileListResponse(BaseModel):
    files: Optional[List[FileInfo]] = None

    path: str

    total: int

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
