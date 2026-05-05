# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AppCreateSignedUploadURLResponse", "R2UploadURL"]


class R2UploadURL(BaseModel):
    file_name: str = FieldInfo(alias="fileName")

    r2_upload_url: str = FieldInfo(alias="r2UploadUrl")


class AppCreateSignedUploadURLResponse(BaseModel):
    id: str
    """App ID in the database"""

    r2_upload_urls: List[R2UploadURL] = FieldInfo(alias="r2UploadUrls")
    """Pre-signed Cloudflare R2 URLs for uploading APK files"""
