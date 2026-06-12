# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents.chat import abort_perform_params
from ....types.agents.chat.abort_perform_response import AbortPerformResponse
from ....types.agents.chat.abort_force_clear_response import AbortForceClearResponse

__all__ = ["AbortResource", "AsyncAbortResource"]


class AbortResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AbortResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AbortResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AbortResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AbortResourceWithStreamingResponse(self)

    def force_clear(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AbortForceClearResponse:
        """Unconditionally clears the in-flight chat state for the caller.

        Idempotent
        escape hatch when /chat/abort cannot settle.
        """
        return self._post(
            "/agents/chat/abort/force",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AbortForceClearResponse,
        )

    def perform(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AbortPerformResponse:
        """Abort the in-flight chat turn owned by `sessionId`.

        Idempotent. A turn owned by
        a different session is left untouched (204).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agents/chat/abort",
            body=maybe_transform({"session_id": session_id}, abort_perform_params.AbortPerformParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AbortPerformResponse,
        )


class AsyncAbortResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAbortResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAbortResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAbortResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncAbortResourceWithStreamingResponse(self)

    async def force_clear(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AbortForceClearResponse:
        """Unconditionally clears the in-flight chat state for the caller.

        Idempotent
        escape hatch when /chat/abort cannot settle.
        """
        return await self._post(
            "/agents/chat/abort/force",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AbortForceClearResponse,
        )

    async def perform(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AbortPerformResponse:
        """Abort the in-flight chat turn owned by `sessionId`.

        Idempotent. A turn owned by
        a different session is left untouched (204).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agents/chat/abort",
            body=await async_maybe_transform({"session_id": session_id}, abort_perform_params.AbortPerformParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AbortPerformResponse,
        )


class AbortResourceWithRawResponse:
    def __init__(self, abort: AbortResource) -> None:
        self._abort = abort

        self.force_clear = to_raw_response_wrapper(
            abort.force_clear,
        )
        self.perform = to_raw_response_wrapper(
            abort.perform,
        )


class AsyncAbortResourceWithRawResponse:
    def __init__(self, abort: AsyncAbortResource) -> None:
        self._abort = abort

        self.force_clear = async_to_raw_response_wrapper(
            abort.force_clear,
        )
        self.perform = async_to_raw_response_wrapper(
            abort.perform,
        )


class AbortResourceWithStreamingResponse:
    def __init__(self, abort: AbortResource) -> None:
        self._abort = abort

        self.force_clear = to_streamed_response_wrapper(
            abort.force_clear,
        )
        self.perform = to_streamed_response_wrapper(
            abort.perform,
        )


class AsyncAbortResourceWithStreamingResponse:
    def __init__(self, abort: AsyncAbortResource) -> None:
        self._abort = abort

        self.force_clear = async_to_streamed_response_wrapper(
            abort.force_clear,
        )
        self.perform = async_to_streamed_response_wrapper(
            abort.perform,
        )
