# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.devices import traffic_session_list_params, traffic_session_create_params
from ...types.devices.traffic_session_list_response import TrafficSessionListResponse
from ...types.devices.traffic_session_create_response import TrafficSessionCreateResponse
from ...types.devices.traffic_session_delete_response import TrafficSessionDeleteResponse
from ...types.devices.traffic_session_retrieve_response import TrafficSessionRetrieveResponse

__all__ = ["TrafficSessionsResource", "AsyncTrafficSessionsResource"]


class TrafficSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrafficSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TrafficSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrafficSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return TrafficSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        device_id: str,
        *,
        idempotency_key: str,
        expires_in_seconds: int | Omit = omit,
        max_body_bytes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficSessionCreateResponse:
        """
        Starts one live-only decoded HTTP/1.1, HTTP/2, HTTP/3 and WebSocket traffic
        session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            path_template("/devices/{device_id}/traffic/sessions", device_id=device_id),
            body=maybe_transform(
                {
                    "expires_in_seconds": expires_in_seconds,
                    "max_body_bytes": max_body_bytes,
                },
                traffic_session_create_params.TrafficSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficSessionCreateResponse,
        )

    def retrieve(
        self,
        session_id: str,
        *,
        device_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficSessionRetrieveResponse:
        """
        Returns status and the device stream credential for a live session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template(
                "/devices/{device_id}/traffic/sessions/{session_id}", device_id=device_id, session_id=session_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficSessionRetrieveResponse,
        )

    def list(
        self,
        device_id: str,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficSessionListResponse:
        """
        List device traffic sessions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get(
            path_template("/devices/{device_id}/traffic/sessions", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    traffic_session_list_params.TrafficSessionListParams,
                ),
            ),
            cast_to=TrafficSessionListResponse,
        )

    def delete(
        self,
        session_id: str,
        *,
        device_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficSessionDeleteResponse:
        """
        Stop device traffic inspection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._delete(
            path_template(
                "/devices/{device_id}/traffic/sessions/{session_id}", device_id=device_id, session_id=session_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficSessionDeleteResponse,
        )


class AsyncTrafficSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrafficSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrafficSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrafficSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncTrafficSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        device_id: str,
        *,
        idempotency_key: str,
        expires_in_seconds: int | Omit = omit,
        max_body_bytes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficSessionCreateResponse:
        """
        Starts one live-only decoded HTTP/1.1, HTTP/2, HTTP/3 and WebSocket traffic
        session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            path_template("/devices/{device_id}/traffic/sessions", device_id=device_id),
            body=await async_maybe_transform(
                {
                    "expires_in_seconds": expires_in_seconds,
                    "max_body_bytes": max_body_bytes,
                },
                traffic_session_create_params.TrafficSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficSessionCreateResponse,
        )

    async def retrieve(
        self,
        session_id: str,
        *,
        device_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficSessionRetrieveResponse:
        """
        Returns status and the device stream credential for a live session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template(
                "/devices/{device_id}/traffic/sessions/{session_id}", device_id=device_id, session_id=session_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficSessionRetrieveResponse,
        )

    async def list(
        self,
        device_id: str,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficSessionListResponse:
        """
        List device traffic sessions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._get(
            path_template("/devices/{device_id}/traffic/sessions", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    traffic_session_list_params.TrafficSessionListParams,
                ),
            ),
            cast_to=TrafficSessionListResponse,
        )

    async def delete(
        self,
        session_id: str,
        *,
        device_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficSessionDeleteResponse:
        """
        Stop device traffic inspection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._delete(
            path_template(
                "/devices/{device_id}/traffic/sessions/{session_id}", device_id=device_id, session_id=session_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficSessionDeleteResponse,
        )


class TrafficSessionsResourceWithRawResponse:
    def __init__(self, traffic_sessions: TrafficSessionsResource) -> None:
        self._traffic_sessions = traffic_sessions

        self.create = to_raw_response_wrapper(
            traffic_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            traffic_sessions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            traffic_sessions.list,
        )
        self.delete = to_raw_response_wrapper(
            traffic_sessions.delete,
        )


class AsyncTrafficSessionsResourceWithRawResponse:
    def __init__(self, traffic_sessions: AsyncTrafficSessionsResource) -> None:
        self._traffic_sessions = traffic_sessions

        self.create = async_to_raw_response_wrapper(
            traffic_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            traffic_sessions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            traffic_sessions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            traffic_sessions.delete,
        )


class TrafficSessionsResourceWithStreamingResponse:
    def __init__(self, traffic_sessions: TrafficSessionsResource) -> None:
        self._traffic_sessions = traffic_sessions

        self.create = to_streamed_response_wrapper(
            traffic_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            traffic_sessions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            traffic_sessions.list,
        )
        self.delete = to_streamed_response_wrapper(
            traffic_sessions.delete,
        )


class AsyncTrafficSessionsResourceWithStreamingResponse:
    def __init__(self, traffic_sessions: AsyncTrafficSessionsResource) -> None:
        self._traffic_sessions = traffic_sessions

        self.create = async_to_streamed_response_wrapper(
            traffic_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            traffic_sessions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            traffic_sessions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            traffic_sessions.delete,
        )
