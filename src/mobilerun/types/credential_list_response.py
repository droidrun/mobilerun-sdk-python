# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .credentials.packages.credential import Credential

__all__ = ["CredentialListResponse", "Pagination"]


class Pagination(BaseModel):
    has_next: bool = FieldInfo(alias="hasNext")

    has_prev: bool = FieldInfo(alias="hasPrev")

    page: int

    pages: int

    page_size: int = FieldInfo(alias="pageSize")

    total: int


class CredentialListResponse(BaseModel):
    items: List[Credential]

    pagination: Pagination
