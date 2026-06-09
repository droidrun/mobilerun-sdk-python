# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProxyPingResponse", "Latency"]


class Latency(BaseModel):
    """An aggregated latency measurement taken through the proxy."""

    avg_ms: int = FieldInfo(alias="avgMs")
    """Mean round-trip time over successful probes, in milliseconds."""

    jitter_ms: int = FieldInfo(alias="jitterMs")
    """Round-trip time spread (max - min) over successful probes, in milliseconds."""

    max_ms: int = FieldInfo(alias="maxMs")
    """Maximum round-trip time over successful probes, in milliseconds."""

    measured_at: datetime = FieldInfo(alias="measuredAt")
    """When this measurement was taken."""

    min_ms: int = FieldInfo(alias="minMs")
    """Minimum round-trip time over successful probes, in milliseconds."""

    packet_loss: float = FieldInfo(alias="packetLoss")
    """
    Fraction of probes that failed, 0..1 (1 means the proxy was unreachable; rtt
    fields are 0).
    """

    samples: int
    """Number of probes taken in this measurement."""

    target: str
    """The host:port the latency was measured against, through the proxy."""


class ProxyPingResponse(BaseModel):
    """The latest cached latency reading for a proxy."""

    latency: Optional[Latency] = None
    """An aggregated latency measurement taken through the proxy."""

    proxy_id: str = FieldInfo(alias="proxyId")
