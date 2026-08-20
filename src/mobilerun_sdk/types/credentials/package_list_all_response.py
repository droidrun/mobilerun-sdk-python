# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PackageListAllResponse", "Data"]


class Data(BaseModel):
    package_name: str = FieldInfo(alias="packageName")


class PackageListAllResponse(BaseModel):
    data: List[Data]
