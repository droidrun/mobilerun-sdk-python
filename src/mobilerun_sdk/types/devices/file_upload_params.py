# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    path: Required[str]

    file: Required[FileTypes]

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
