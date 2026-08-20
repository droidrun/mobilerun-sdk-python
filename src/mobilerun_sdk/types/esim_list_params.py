# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EsimListParams"]


class EsimListParams(TypedDict, total=False):
    mine: Literal["true", "false"]
    """Only include eSIMs created by the calling actor."""

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    status: Literal["all", "in_stock", "owned", "installing", "installed", "install_failed", "retired"]
