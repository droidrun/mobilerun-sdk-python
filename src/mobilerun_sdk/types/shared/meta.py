# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from pydantic import Field as FieldInfo

__all__ = ["Meta"]

class Meta(BaseModel):
    has_next: bool = FieldInfo(alias = "hasNext")

    has_prev: bool = FieldInfo(alias = "hasPrev")

    page: int

    pages: int

    page_size: int = FieldInfo(alias = "pageSize")

    total: int