# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["DeviceSummaryParams"]


class DeviceSummaryParams(TypedDict, total=False):
    state: Optional[
        List[
            Literal[
                "creating",
                "assigned",
                "ready",
                "rebooting",
                "migrating",
                "resetting",
                "terminated",
                "maintenance",
                "stopped",
                "unknown",
            ]
        ]
    ]
