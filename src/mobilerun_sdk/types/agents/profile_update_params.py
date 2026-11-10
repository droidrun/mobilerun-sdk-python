# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProfileUpdateParams", "AvatarConfig"]


class ProfileUpdateParams(TypedDict, total=False):
    avatar_config: Annotated[Optional[AvatarConfig], PropertyInfo(alias="avatarConfig")]

    avatar_kind: Annotated[Optional[Literal["blob"]], PropertyInfo(alias="avatarKind")]

    color: Optional[
        Literal["slate", "red", "orange", "amber", "lime", "green", "teal", "cyan", "blue", "indigo", "violet", "pink"]
    ]
    """
    Set the avatar palette color without changing its seed; null removes only the
    color. Omitted color stays unchanged, including during a seed update.
    """

    display_name: Annotated[Optional[str], PropertyInfo(alias="displayName")]
    """
    Single-line name shown for the Agent; surrounding whitespace is trimmed and it
    needs at least one letter or number.
    """

    instructions: Optional[str]
    """
    The Agent's individual instructions passage; an empty or whitespace-only text
    clears it. Line breaks count three characters toward the rendered size limit.
    """

    model_profile: Annotated[Optional[str], PropertyInfo(alias="modelProfile")]
    """
    Model profile id from GET /agents/model-profiles; null uses the environment
    default.
    """


class AvatarConfig(TypedDict, total=False):
    seed: Required[Union[str, int]]
