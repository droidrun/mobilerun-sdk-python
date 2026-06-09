# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FileMintUploadURLResponse"]


class FileMintUploadURLResponse(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")

    file_id: str = FieldInfo(alias="fileId")

    put_url: str = FieldInfo(alias="putUrl")
