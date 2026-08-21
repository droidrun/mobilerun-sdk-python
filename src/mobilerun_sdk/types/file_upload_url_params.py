# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileUploadURLParams"]


class FileUploadURLParams(TypedDict, total=False):
    filename: Required[str]

    mime_type: Required[Annotated[str, PropertyInfo(alias="mimeType")]]

    size_bytes: Required[Annotated[int, PropertyInfo(alias="sizeBytes")]]

    zone: Literal["user", "skills"]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
