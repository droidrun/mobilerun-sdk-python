# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from pydantic import Field as FieldInfo

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, List

__all__ = ["ProxyListConnectionsResponse", "Item", "Pagination"]

class Item(BaseModel):
    """A single proxy connection, aggregated across its lifetime.

    Byte counts are totals for the whole connection.
    """
    bytes_in: int = FieldInfo(alias = "bytesIn")
    """Total bytes received from upstream over the connection's lifetime."""

    bytes_out: int = FieldInfo(alias = "bytesOut")
    """Total bytes sent to upstream over the connection's lifetime."""

    country: str
    """Upstream country code (ISO 3166-1 alpha-2), or empty if unknown."""

    dst_host: str = FieldInfo(alias = "dstHost")
    """Destination host the client connected to."""

    dst_port: int = FieldInfo(alias = "dstPort")
    """Destination port the client connected to."""

    duration_ms: int = FieldInfo(alias = "durationMs")
    """Elapsed time between startedAt and endedAt, in milliseconds."""

    ended_at: datetime = FieldInfo(alias = "endedAt")
    """Time of the connection's last recorded activity (close time once closed)."""

    protocol: Literal["tcp", "udp", "unknown"]
    """Transport protocol of a connection."""

    provider: str
    """Upstream provider that served the connection."""

    proxy_id: str = FieldInfo(alias = "proxyId")
    """The proxy the connection was routed through.

    All-zero when the upstream was unresolved at capture time.
    """

    session_id: str = FieldInfo(alias = "sessionId")
    """Unique id of this connection."""

    src_ip: str = FieldInfo(alias = "srcIp")
    """Client source IP address."""

    started_at: datetime = FieldInfo(alias = "startedAt")
    """When the connection started."""

    status: Literal["active", "closed"]
    """
    `active` while the connection is still open (no terminal record yet); `closed`
    once it has ended.
    """

    total_bytes: int = FieldInfo(alias = "totalBytes")
    """bytesIn + bytesOut."""

    user_id: str = FieldInfo(alias = "userId")
    """The user that made the connection."""

    close_reason: Optional[str] = FieldInfo(alias = "closeReason", default = None)
    """Why the connection closed; null while still active."""

class Pagination(BaseModel):
    """Pagination metadata for a list response."""
    has_next: bool = FieldInfo(alias = "hasNext")
    """Whether a next page exists."""

    has_prev: bool = FieldInfo(alias = "hasPrev")
    """Whether a previous page exists."""

    page: int
    """Current page number (1-based)."""

    pages: int
    """Total number of pages."""

    page_size: int = FieldInfo(alias = "pageSize")
    """Number of items per page."""

    total: int
    """Total number of items across all pages."""

class ProxyListConnectionsResponse(BaseModel):
    """A page of connections."""
    items: List[Item]

    pagination: Pagination
    """Pagination metadata for a list response."""