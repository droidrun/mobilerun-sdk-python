# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from pydantic import Field as FieldInfo

__all__ = ["AppStorageUsageResponse", "Data"]

class Data(BaseModel):
    available_bytes: float = FieldInfo(alias = "availableBytes")
    """Remaining bytes — the reliable maximum size for the next upload.

    Advisory snapshot: the quota is enforced under a lock at confirm, so concurrent
    uploads may reduce actual headroom.
    """

    quota_bytes: float = FieldInfo(alias = "quotaBytes")
    """Total storage allowance for the user, in bytes"""

    used_bytes: float = FieldInfo(alias = "usedBytes")
    """Bytes currently consumed across all of the user’s app versions"""

class AppStorageUsageResponse(BaseModel):
    data: Data