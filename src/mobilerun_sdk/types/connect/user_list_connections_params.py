# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserListConnectionsParams"]


class UserListConnectionsParams(TypedDict, total=False):
    close_reason: Annotated[str, PropertyInfo(alias="closeReason")]
    """Filter to connections that closed with this reason (closed connections only)."""

    country: str
    """Filter to connections served from this upstream country (ISO 3166-1 alpha-2)."""

    dst_host: Annotated[str, PropertyInfo(alias="dstHost")]
    """Filter to connections to this destination host (exact match)."""

    dst_port: Annotated[int, PropertyInfo(alias="dstPort")]
    """Filter to connections to this destination port."""

    ended_after: Annotated[Union[str, datetime], PropertyInfo(alias="endedAfter", format="iso8601")]
    """
    Filter to connections whose last activity was at or after this time (inclusive).
    """

    ended_before: Annotated[Union[str, datetime], PropertyInfo(alias="endedBefore", format="iso8601")]
    """
    Filter to connections whose last activity was at or before this time
    (inclusive).
    """

    max_bytes_in: Annotated[int, PropertyInfo(alias="maxBytesIn")]
    """Filter to connections with at most this many bytes received from upstream."""

    max_bytes_out: Annotated[int, PropertyInfo(alias="maxBytesOut")]
    """Filter to connections with at most this many bytes sent to upstream."""

    max_duration_ms: Annotated[int, PropertyInfo(alias="maxDurationMs")]
    """Filter to connections lasting at most this many milliseconds."""

    max_total_bytes: Annotated[int, PropertyInfo(alias="maxTotalBytes")]
    """
    Filter to connections with at most this much total traffic (bytesIn + bytesOut).
    """

    min_bytes_in: Annotated[int, PropertyInfo(alias="minBytesIn")]
    """Filter to connections with at least this many bytes received from upstream."""

    min_bytes_out: Annotated[int, PropertyInfo(alias="minBytesOut")]
    """Filter to connections with at least this many bytes sent to upstream."""

    min_duration_ms: Annotated[int, PropertyInfo(alias="minDurationMs")]
    """Filter to connections lasting at least this many milliseconds."""

    min_total_bytes: Annotated[int, PropertyInfo(alias="minTotalBytes")]
    """
    Filter to connections with at least this much total traffic (bytesIn +
    bytesOut).
    """

    order: Literal["asc", "desc"]
    """Sort direction."""

    order_by: Annotated[
        Literal["startedAt", "endedAt", "bytesIn", "bytesOut", "totalBytes", "durationMs"],
        PropertyInfo(alias="orderBy"),
    ]
    """Property to order the results by."""

    page: int
    """Page number (1-based)."""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Number of items per page."""

    protocol: Literal["tcp", "udp", "unknown"]
    """Filter to connections of this transport protocol."""

    provider: str
    """Filter to connections served by this upstream provider."""

    proxy_id: Annotated[str, PropertyInfo(alias="proxyId")]
    """Filter to connections routed through this proxy."""

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """Filter to a single connection by its session id."""

    started_after: Annotated[Union[str, datetime], PropertyInfo(alias="startedAfter", format="iso8601")]
    """Filter to connections that started at or after this time (inclusive)."""

    started_before: Annotated[Union[str, datetime], PropertyInfo(alias="startedBefore", format="iso8601")]
    """Filter to connections that started at or before this time (inclusive)."""

    status: Literal["active", "closed"]
    """Filter by connection status."""
