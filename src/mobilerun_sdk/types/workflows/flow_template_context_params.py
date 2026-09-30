# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FlowTemplateContextParams"]


class FlowTemplateContextParams(TypedDict, total=False):
    template_resolution_version: Annotated[int, PropertyInfo(alias="templateResolutionVersion")]
