# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PackageCredentials"]


class PackageCredentials(BaseModel):
    credential_names: List[str] = FieldInfo(alias="credentialNames")

    package_name: str = FieldInfo(alias="packageName")
