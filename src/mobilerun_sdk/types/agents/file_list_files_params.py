# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FileListFilesParams"]


class FileListFilesParams(TypedDict, total=False):
    zone: Literal["user", "agent", "workflow", "skills"]
