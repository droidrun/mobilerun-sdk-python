# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CarrierListParams"]


class CarrierListParams(TypedDict, total=False):
    country: str
    """Filter by country name"""

    country_iso: Annotated[str, PropertyInfo(alias="countryISO")]
    """Filter by country ISO code"""

    order_by: Annotated[
        Literal["id", "mcc", "mnc", "operator", "country", "country_iso"], PropertyInfo(alias="orderBy")
    ]
    """Field to order by"""

    order_dir: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderDir")]
    """Order direction"""

    page: int
    """Page number"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Items per page"""
