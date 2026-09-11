# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AppStorageUsageResponse", "Data"]


class Data(BaseModel):
    available_bytes: float = FieldInfo(alias="availableBytes")
    """Remaining bytes — the reliable maximum TOTAL size for the next upload.

    Advisory snapshot: the quota is enforced under a lock at confirm, so concurrent
    uploads may reduce actual headroom.
    """

    max_file_bytes: float = FieldInfo(alias="maxFileBytes")
    """Per-file upload cap in bytes (env.MAX_UPLOAD_FILE_BYTES).

    A single file larger than this is rejected at confirm even when it fits the
    remaining quota. Source of truth for the client-side per-file limit.
    """

    quota_bytes: float = FieldInfo(alias="quotaBytes")
    """Total storage allowance for the user, in bytes"""

    used_bytes: float = FieldInfo(alias="usedBytes")
    """Bytes currently consumed across all of the user’s app versions"""


class AppStorageUsageResponse(BaseModel):
    data: Data
