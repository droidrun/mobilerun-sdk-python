# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RequestCreateParams"]


class RequestCreateParams(TypedDict, total=False):
    platform: Required[Literal["android", "ios"]]

    requested: Required[str]

    surface: Literal["store", "mcp", "api"]
