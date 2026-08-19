# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from pydantic import Field as FieldInfo

from typing_extensions import Literal

__all__ = ["PackageCreateResponse", "Data"]

class Data(BaseModel):
    package_name: str = FieldInfo(alias = "packageName")

class PackageCreateResponse(BaseModel):
    data: Data

    message: str

    success: Literal[True]