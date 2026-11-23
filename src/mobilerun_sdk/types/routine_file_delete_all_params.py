# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RoutineFileDeleteAllParams"]


class RoutineFileDeleteAllParams(TypedDict, total=False):
    execution_id: Annotated[str, PropertyInfo(alias="executionId")]

    folder: str
