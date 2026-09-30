# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IntegrationListResponse", "Data", "DataCapability"]


class DataCapability(BaseModel):
    id: str

    revision: int


class Data(BaseModel):
    capability: DataCapability

    connection: Literal["connected", "not_connected", "expired"]
    """Connection state for your org.

    Only `connected` integrations can be used as a destination.
    """

    connect_key: str = FieldInfo(alias="connectKey")
    """Opaque key for the Cloud connect dialog."""

    deprecated: bool
    """True for the previous revision during a switch; prefer the non-deprecated one."""

    icon_url: Optional[str] = FieldInfo(alias="iconUrl", default=None)
    """Server-resolved brand logo URL; null when unknown.

    Show this instead of deriving a logo from connectKey.
    """

    label: str

    supports_targets: bool = FieldInfo(alias="supportsTargets")
    """True when targets (e.g.

    channels) can be listed via `GET /webhooks/integrations/{capabilityId}/targets`.
    """


class IntegrationListResponse(BaseModel):
    data: List[Data]
