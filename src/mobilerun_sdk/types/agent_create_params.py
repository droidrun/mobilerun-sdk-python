# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """
    Single-line name shown for the Agent; surrounding whitespace is trimmed and it
    needs at least one letter or number.
    """

    avatar_seed: Annotated[Union[str, int], PropertyInfo(alias="avatarSeed")]

    color: Literal[
        "slate", "red", "orange", "amber", "lime", "green", "teal", "cyan", "blue", "indigo", "violet", "pink"
    ]

    instructions: str
    """
    The Agent's individual instructions passage; an empty or whitespace-only text
    clears it. Line breaks count three characters toward the rendered size limit.
    """
