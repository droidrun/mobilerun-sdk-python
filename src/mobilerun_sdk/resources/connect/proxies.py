# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.connect import proxy_buy_params, proxy_list_params, proxy_list_connections_params
from ...types.connect.proxy_buy_response import ProxyBuyResponse
from ...types.connect.proxy_list_response import ProxyListResponse
from ...types.connect.proxy_ping_response import ProxyPingResponse
from ...types.connect.proxy_retrieve_response import ProxyRetrieveResponse
from ...types.connect.proxy_list_connections_response import ProxyListConnectionsResponse

__all__ = ["ProxiesResource", "AsyncProxiesResource"]


class ProxiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ProxiesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyRetrieveResponse:
        """Returns the proxy identified by the path ID.

        The response includes the proxy's
        password.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/connect/proxies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyRetrieveResponse,
        )

    def list(
        self,
        *,
        country: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyListResponse:
        """
        Returns proxies owned by the calling tenant (the X-Owner-Id header, falling back
        to X-User-ID). Credentials are omitted from the list.

        Args:
          country: Filter to proxies in this country (ISO 3166-1 alpha-2, lowercase).

          page: Page number (1-based).

          page_size: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/connect/proxies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "page": page,
                        "page_size": page_size,
                    },
                    proxy_list_params.ProxyListParams,
                ),
            ),
            cast_to=ProxyListResponse,
        )

    def buy(
        self,
        *,
        country: str,
        type: Literal["dedicated_residential", "residential", "mobile"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyBuyResponse:
        """
        Provisions a proxy for the caller in the selected country.

        Args:
          country: ISO 3166-1 alpha-2 country code to provision the proxy in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/connect/proxies",
            body=maybe_transform(
                {
                    "country": country,
                    "type": type,
                },
                proxy_buy_params.ProxyBuyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyBuyResponse,
        )

    def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the proxy identified by the path ID and releases its provisioning.
        Returns 404 if no such proxy exists for the caller.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/connect/proxies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_connections(
        self,
        id: str,
        *,
        close_reason: str | Omit = omit,
        country: str | Omit = omit,
        dst_host: str | Omit = omit,
        dst_port: int | Omit = omit,
        ended_after: Union[str, datetime] | Omit = omit,
        ended_before: Union[str, datetime] | Omit = omit,
        max_bytes_in: int | Omit = omit,
        max_bytes_out: int | Omit = omit,
        max_duration_ms: int | Omit = omit,
        max_total_bytes: int | Omit = omit,
        min_bytes_in: int | Omit = omit,
        min_bytes_out: int | Omit = omit,
        min_duration_ms: int | Omit = omit,
        min_total_bytes: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["startedAt", "endedAt", "bytesIn", "bytesOut", "totalBytes", "durationMs"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        protocol: Literal["tcp", "udp", "unknown"] | Omit = omit,
        provider: str | Omit = omit,
        session_id: str | Omit = omit,
        started_after: Union[str, datetime] | Omit = omit,
        started_before: Union[str, datetime] | Omit = omit,
        status: Literal["active", "closed"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyListConnectionsResponse:
        """
        Returns the connection history recorded for this proxy, one item per connection
        (aggregated across the connection's lifetime). Supports filtering on every
        property plus ordering and pagination. Returns 503 when the connection-insights
        backend is disabled or unreachable.

        Args:
          close_reason: Filter to connections that closed with this reason (closed connections only).

          country: Filter to connections served from this upstream country (ISO 3166-1 alpha-2).

          dst_host: Filter to connections to this destination host (exact match).

          dst_port: Filter to connections to this destination port.

          ended_after: Filter to connections whose last activity was at or after this time (inclusive).

          ended_before: Filter to connections whose last activity was at or before this time
              (inclusive).

          max_bytes_in: Filter to connections with at most this many bytes received from upstream.

          max_bytes_out: Filter to connections with at most this many bytes sent to upstream.

          max_duration_ms: Filter to connections lasting at most this many milliseconds.

          max_total_bytes: Filter to connections with at most this much total traffic (bytesIn + bytesOut).

          min_bytes_in: Filter to connections with at least this many bytes received from upstream.

          min_bytes_out: Filter to connections with at least this many bytes sent to upstream.

          min_duration_ms: Filter to connections lasting at least this many milliseconds.

          min_total_bytes: Filter to connections with at least this much total traffic (bytesIn +
              bytesOut).

          order: Sort direction.

          order_by: Property to order the results by.

          page: Page number (1-based).

          page_size: Number of items per page.

          protocol: Filter to connections of this transport protocol.

          provider: Filter to connections served by this upstream provider.

          session_id: Filter to a single connection by its session id.

          started_after: Filter to connections that started at or after this time (inclusive).

          started_before: Filter to connections that started at or before this time (inclusive).

          status: Filter by connection status.

          user_id: Filter to connections made by this user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/connect/proxies/{id}/connections", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "close_reason": close_reason,
                        "country": country,
                        "dst_host": dst_host,
                        "dst_port": dst_port,
                        "ended_after": ended_after,
                        "ended_before": ended_before,
                        "max_bytes_in": max_bytes_in,
                        "max_bytes_out": max_bytes_out,
                        "max_duration_ms": max_duration_ms,
                        "max_total_bytes": max_total_bytes,
                        "min_bytes_in": min_bytes_in,
                        "min_bytes_out": min_bytes_out,
                        "min_duration_ms": min_duration_ms,
                        "min_total_bytes": min_total_bytes,
                        "order": order,
                        "order_by": order_by,
                        "page": page,
                        "page_size": page_size,
                        "protocol": protocol,
                        "provider": provider,
                        "session_id": session_id,
                        "started_after": started_after,
                        "started_before": started_before,
                        "status": status,
                        "user_id": user_id,
                    },
                    proxy_list_connections_params.ProxyListConnectionsParams,
                ),
            ),
            cast_to=ProxyListConnectionsResponse,
        )

    def ping(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyPingResponse:
        """
        Returns the most recent cached network-latency measurement for the proxy,
        sampled periodically by connecting through the proxy to a fixed target.
        `latency` is null when no measurement is available yet (e.g. the proxy is not
        active, or it has not been sampled since coming online).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/connect/proxies/{id}/ping", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyPingResponse,
        )


class AsyncProxiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncProxiesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyRetrieveResponse:
        """Returns the proxy identified by the path ID.

        The response includes the proxy's
        password.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/connect/proxies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyRetrieveResponse,
        )

    async def list(
        self,
        *,
        country: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyListResponse:
        """
        Returns proxies owned by the calling tenant (the X-Owner-Id header, falling back
        to X-User-ID). Credentials are omitted from the list.

        Args:
          country: Filter to proxies in this country (ISO 3166-1 alpha-2, lowercase).

          page: Page number (1-based).

          page_size: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/connect/proxies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "page": page,
                        "page_size": page_size,
                    },
                    proxy_list_params.ProxyListParams,
                ),
            ),
            cast_to=ProxyListResponse,
        )

    async def buy(
        self,
        *,
        country: str,
        type: Literal["dedicated_residential", "residential", "mobile"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyBuyResponse:
        """
        Provisions a proxy for the caller in the selected country.

        Args:
          country: ISO 3166-1 alpha-2 country code to provision the proxy in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/connect/proxies",
            body=await async_maybe_transform(
                {
                    "country": country,
                    "type": type,
                },
                proxy_buy_params.ProxyBuyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyBuyResponse,
        )

    async def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the proxy identified by the path ID and releases its provisioning.
        Returns 404 if no such proxy exists for the caller.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/connect/proxies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_connections(
        self,
        id: str,
        *,
        close_reason: str | Omit = omit,
        country: str | Omit = omit,
        dst_host: str | Omit = omit,
        dst_port: int | Omit = omit,
        ended_after: Union[str, datetime] | Omit = omit,
        ended_before: Union[str, datetime] | Omit = omit,
        max_bytes_in: int | Omit = omit,
        max_bytes_out: int | Omit = omit,
        max_duration_ms: int | Omit = omit,
        max_total_bytes: int | Omit = omit,
        min_bytes_in: int | Omit = omit,
        min_bytes_out: int | Omit = omit,
        min_duration_ms: int | Omit = omit,
        min_total_bytes: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["startedAt", "endedAt", "bytesIn", "bytesOut", "totalBytes", "durationMs"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        protocol: Literal["tcp", "udp", "unknown"] | Omit = omit,
        provider: str | Omit = omit,
        session_id: str | Omit = omit,
        started_after: Union[str, datetime] | Omit = omit,
        started_before: Union[str, datetime] | Omit = omit,
        status: Literal["active", "closed"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyListConnectionsResponse:
        """
        Returns the connection history recorded for this proxy, one item per connection
        (aggregated across the connection's lifetime). Supports filtering on every
        property plus ordering and pagination. Returns 503 when the connection-insights
        backend is disabled or unreachable.

        Args:
          close_reason: Filter to connections that closed with this reason (closed connections only).

          country: Filter to connections served from this upstream country (ISO 3166-1 alpha-2).

          dst_host: Filter to connections to this destination host (exact match).

          dst_port: Filter to connections to this destination port.

          ended_after: Filter to connections whose last activity was at or after this time (inclusive).

          ended_before: Filter to connections whose last activity was at or before this time
              (inclusive).

          max_bytes_in: Filter to connections with at most this many bytes received from upstream.

          max_bytes_out: Filter to connections with at most this many bytes sent to upstream.

          max_duration_ms: Filter to connections lasting at most this many milliseconds.

          max_total_bytes: Filter to connections with at most this much total traffic (bytesIn + bytesOut).

          min_bytes_in: Filter to connections with at least this many bytes received from upstream.

          min_bytes_out: Filter to connections with at least this many bytes sent to upstream.

          min_duration_ms: Filter to connections lasting at least this many milliseconds.

          min_total_bytes: Filter to connections with at least this much total traffic (bytesIn +
              bytesOut).

          order: Sort direction.

          order_by: Property to order the results by.

          page: Page number (1-based).

          page_size: Number of items per page.

          protocol: Filter to connections of this transport protocol.

          provider: Filter to connections served by this upstream provider.

          session_id: Filter to a single connection by its session id.

          started_after: Filter to connections that started at or after this time (inclusive).

          started_before: Filter to connections that started at or before this time (inclusive).

          status: Filter by connection status.

          user_id: Filter to connections made by this user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/connect/proxies/{id}/connections", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "close_reason": close_reason,
                        "country": country,
                        "dst_host": dst_host,
                        "dst_port": dst_port,
                        "ended_after": ended_after,
                        "ended_before": ended_before,
                        "max_bytes_in": max_bytes_in,
                        "max_bytes_out": max_bytes_out,
                        "max_duration_ms": max_duration_ms,
                        "max_total_bytes": max_total_bytes,
                        "min_bytes_in": min_bytes_in,
                        "min_bytes_out": min_bytes_out,
                        "min_duration_ms": min_duration_ms,
                        "min_total_bytes": min_total_bytes,
                        "order": order,
                        "order_by": order_by,
                        "page": page,
                        "page_size": page_size,
                        "protocol": protocol,
                        "provider": provider,
                        "session_id": session_id,
                        "started_after": started_after,
                        "started_before": started_before,
                        "status": status,
                        "user_id": user_id,
                    },
                    proxy_list_connections_params.ProxyListConnectionsParams,
                ),
            ),
            cast_to=ProxyListConnectionsResponse,
        )

    async def ping(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyPingResponse:
        """
        Returns the most recent cached network-latency measurement for the proxy,
        sampled periodically by connecting through the proxy to a fixed target.
        `latency` is null when no measurement is available yet (e.g. the proxy is not
        active, or it has not been sampled since coming online).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/connect/proxies/{id}/ping", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyPingResponse,
        )


class ProxiesResourceWithRawResponse:
    def __init__(self, proxies: ProxiesResource) -> None:
        self._proxies = proxies

        self.retrieve = to_raw_response_wrapper(
            proxies.retrieve,
        )
        self.list = to_raw_response_wrapper(
            proxies.list,
        )
        self.buy = to_raw_response_wrapper(
            proxies.buy,
        )
        self.cancel = to_raw_response_wrapper(
            proxies.cancel,
        )
        self.list_connections = to_raw_response_wrapper(
            proxies.list_connections,
        )
        self.ping = to_raw_response_wrapper(
            proxies.ping,
        )


class AsyncProxiesResourceWithRawResponse:
    def __init__(self, proxies: AsyncProxiesResource) -> None:
        self._proxies = proxies

        self.retrieve = async_to_raw_response_wrapper(
            proxies.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            proxies.list,
        )
        self.buy = async_to_raw_response_wrapper(
            proxies.buy,
        )
        self.cancel = async_to_raw_response_wrapper(
            proxies.cancel,
        )
        self.list_connections = async_to_raw_response_wrapper(
            proxies.list_connections,
        )
        self.ping = async_to_raw_response_wrapper(
            proxies.ping,
        )


class ProxiesResourceWithStreamingResponse:
    def __init__(self, proxies: ProxiesResource) -> None:
        self._proxies = proxies

        self.retrieve = to_streamed_response_wrapper(
            proxies.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            proxies.list,
        )
        self.buy = to_streamed_response_wrapper(
            proxies.buy,
        )
        self.cancel = to_streamed_response_wrapper(
            proxies.cancel,
        )
        self.list_connections = to_streamed_response_wrapper(
            proxies.list_connections,
        )
        self.ping = to_streamed_response_wrapper(
            proxies.ping,
        )


class AsyncProxiesResourceWithStreamingResponse:
    def __init__(self, proxies: AsyncProxiesResource) -> None:
        self._proxies = proxies

        self.retrieve = async_to_streamed_response_wrapper(
            proxies.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            proxies.list,
        )
        self.buy = async_to_streamed_response_wrapper(
            proxies.buy,
        )
        self.cancel = async_to_streamed_response_wrapper(
            proxies.cancel,
        )
        self.list_connections = async_to_streamed_response_wrapper(
            proxies.list_connections,
        )
        self.ping = async_to_streamed_response_wrapper(
            proxies.ping,
        )
