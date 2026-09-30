# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NotificationApplyPreferencesPresetParams"]


class NotificationApplyPreferencesPresetParams(TypedDict, total=False):
    preset: Required[Literal["recommended", "failures", "everything"]]
