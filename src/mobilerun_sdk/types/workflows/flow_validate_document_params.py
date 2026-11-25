# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlowValidateDocumentParams"]


class FlowValidateDocumentParams(TypedDict, total=False):
    document: object
    """Routine document; format at GET /flows/document-schema"""
