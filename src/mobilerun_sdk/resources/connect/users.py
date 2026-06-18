# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
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
from ...types.connect import user_list_params, user_create_params, user_update_params, user_list_connections_params
from ...types.connect.user_list_response import UserListResponse
from ...types.connect.user_create_response import UserCreateResponse
from ...types.connect.user_update_response import UserUpdateResponse
from ...types.connect.user_retrieve_response import UserRetrieveResponse
from ...types.connect.user_list_connections_response import UserListConnectionsResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        password: str | Omit = omit,
        proxy_id: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserCreateResponse:
        """
        Creates a SOCKS5 credential, optionally bound to a proxy for dedicated routing.
        Username and password are generated when omitted.

        Args:
          password: Desired SOCKS5 password, 1-255 bytes (RFC 1929). Generated when omitted.

          proxy_id: Proxy to bind the user to for dedicated routing.

          username: Desired SOCKS5 username, 1-255 bytes (RFC 1929). Generated when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/connect/users",
            body=maybe_transform(
                {
                    "password": password,
                    "proxy_id": proxy_id,
                    "username": username,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserCreateResponse,
        )

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
    ) -> UserRetrieveResponse:
        """
        Get a SOCKS5 user by ID, including its password

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/connect/users/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        proxy_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUpdateResponse:
        """
        Rebind the user to a different proxy (or detach it by passing null).

        Args:
          proxy_id: Proxy to rebind to, or null to detach. Omit to leave the user's current binding
              unchanged — only an explicit null detaches.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/connect/users/{id}", id=id),
            body=maybe_transform({"proxy_id": proxy_id}, user_update_params.UserUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        proxy_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """Returns SOCKS5 users owned by the caller.

        Passwords are omitted from the list.

        Args:
          page: Page number (1-based).

          page_size: Number of items per page.

          proxy_id: Filter to users bound to this proxy. Users not bound to it (including unbound
              users) are excluded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/connect/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "proxy_id": proxy_id,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    def delete(
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
        Delete a SOCKS5 user

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
            path_template("/connect/users/{id}", id=id),
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
        proxy_id: str | Omit = omit,
        session_id: str | Omit = omit,
        started_after: Union[str, datetime] | Omit = omit,
        started_before: Union[str, datetime] | Omit = omit,
        status: Literal["active", "closed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListConnectionsResponse:
        """
        Returns the connection history recorded for this user, one item per connection
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

          proxy_id: Filter to connections routed through this proxy.

          session_id: Filter to a single connection by its session id.

          started_after: Filter to connections that started at or after this time (inclusive).

          started_before: Filter to connections that started at or before this time (inclusive).

          status: Filter by connection status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/connect/users/{id}/connections", id=id),
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
                        "proxy_id": proxy_id,
                        "session_id": session_id,
                        "started_after": started_after,
                        "started_before": started_before,
                        "status": status,
                    },
                    user_list_connections_params.UserListConnectionsParams,
                ),
            ),
            cast_to=UserListConnectionsResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        password: str | Omit = omit,
        proxy_id: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserCreateResponse:
        """
        Creates a SOCKS5 credential, optionally bound to a proxy for dedicated routing.
        Username and password are generated when omitted.

        Args:
          password: Desired SOCKS5 password, 1-255 bytes (RFC 1929). Generated when omitted.

          proxy_id: Proxy to bind the user to for dedicated routing.

          username: Desired SOCKS5 username, 1-255 bytes (RFC 1929). Generated when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/connect/users",
            body=await async_maybe_transform(
                {
                    "password": password,
                    "proxy_id": proxy_id,
                    "username": username,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserCreateResponse,
        )

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
    ) -> UserRetrieveResponse:
        """
        Get a SOCKS5 user by ID, including its password

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/connect/users/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        proxy_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUpdateResponse:
        """
        Rebind the user to a different proxy (or detach it by passing null).

        Args:
          proxy_id: Proxy to rebind to, or null to detach. Omit to leave the user's current binding
              unchanged — only an explicit null detaches.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/connect/users/{id}", id=id),
            body=await async_maybe_transform({"proxy_id": proxy_id}, user_update_params.UserUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdateResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        proxy_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """Returns SOCKS5 users owned by the caller.

        Passwords are omitted from the list.

        Args:
          page: Page number (1-based).

          page_size: Number of items per page.

          proxy_id: Filter to users bound to this proxy. Users not bound to it (including unbound
              users) are excluded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/connect/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "proxy_id": proxy_id,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    async def delete(
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
        Delete a SOCKS5 user

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
            path_template("/connect/users/{id}", id=id),
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
        proxy_id: str | Omit = omit,
        session_id: str | Omit = omit,
        started_after: Union[str, datetime] | Omit = omit,
        started_before: Union[str, datetime] | Omit = omit,
        status: Literal["active", "closed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListConnectionsResponse:
        """
        Returns the connection history recorded for this user, one item per connection
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

          proxy_id: Filter to connections routed through this proxy.

          session_id: Filter to a single connection by its session id.

          started_after: Filter to connections that started at or after this time (inclusive).

          started_before: Filter to connections that started at or before this time (inclusive).

          status: Filter by connection status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/connect/users/{id}/connections", id=id),
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
                        "proxy_id": proxy_id,
                        "session_id": session_id,
                        "started_after": started_after,
                        "started_before": started_before,
                        "status": status,
                    },
                    user_list_connections_params.UserListConnectionsParams,
                ),
            ),
            cast_to=UserListConnectionsResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.list_connections = to_raw_response_wrapper(
            users.list_connections,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.list_connections = async_to_raw_response_wrapper(
            users.list_connections,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.list_connections = to_streamed_response_wrapper(
            users.list_connections,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.list_connections = async_to_streamed_response_wrapper(
            users.list_connections,
        )
