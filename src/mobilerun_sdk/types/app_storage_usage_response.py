# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AppStorageUsageResponse", "Data"]


class Data(BaseModel):
    included_bytes: Optional[float] = FieldInfo(alias="includedBytes", default=None)
    """Bytes included in the plan (Autumn granted).

    Null when unlimited, unknown, or storage billing is off.
    """

    max_bytes: Optional[float] = FieldInfo(alias="maxBytes", default=None)
    """
    Hard admission bound in bytes: included + max purchasable overage, or included
    when overage is not allowed. Null = unlimited, unknown, or storage billing is
    off.
    """

    overage_allowed: bool = FieldInfo(alias="overageAllowed")
    """True when usage above includedBytes is billed as overage instead of blocked"""

    used_bytes: float = FieldInfo(alias="usedBytes")
    """
    Bytes currently used (decimal: Autumn storage_mb × 1,000,000; the local sum of
    the user’s app versions when storage billing is off)
    """


class AppStorageUsageResponse(BaseModel):
    data: Data
