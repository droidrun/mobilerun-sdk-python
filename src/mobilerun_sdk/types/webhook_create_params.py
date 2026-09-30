# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebhookCreateParams", "Variant0", "Variant1", "Variant1Capability"]


class Variant0(TypedDict, total=False):
    url: Required[str]

    description: str

    event_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="eventTypes")]

    kind: Literal["http"]
    """Delivery transport. Omitted ⇒ `http`."""


class Variant1(TypedDict, total=False):
    args: Required[Dict[str, object]]
    """
    Target args exactly as returned by
    `GET /webhooks/integrations/{capabilityId}/targets`.
    """

    capability: Required[Variant1Capability]

    kind: Required[Literal["integration"]]

    description: str

    event_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="eventTypes")]


class Variant1Capability(TypedDict, total=False):
    id: Required[str]

    revision: Required[int]


WebhookCreateParams: TypeAlias = Union[Variant0, Variant1]
