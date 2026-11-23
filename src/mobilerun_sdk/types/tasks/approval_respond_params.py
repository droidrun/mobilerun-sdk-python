# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ApprovalRespondParams"]


class ApprovalRespondParams(TypedDict, total=False):
    task_id: Required[str]

    decision: Required[Literal["approve", "deny"]]
    """Approve lets the task continue; deny ends it as failed"""
