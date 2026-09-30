# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["ScreenshotsResource", "AsyncScreenshotsResource"]


class ScreenshotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScreenshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ScreenshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ScreenshotsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        screenshot_id: str,
        *,
        execution_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Redirects (302) to a freshly signed, time-limited image URL for a screenshot
        captured during this execution. Owner-gated: 404 if the execution or the
        screenshot does not belong to the caller.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        if not screenshot_id:
            raise ValueError(f"Expected a non-empty value for `screenshot_id` but received {screenshot_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template(
                "/executions/{execution_id}/screenshots/{screenshot_id}",
                execution_id=execution_id,
                screenshot_id=screenshot_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncScreenshotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScreenshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScreenshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncScreenshotsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        screenshot_id: str,
        *,
        execution_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Redirects (302) to a freshly signed, time-limited image URL for a screenshot
        captured during this execution. Owner-gated: 404 if the execution or the
        screenshot does not belong to the caller.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        if not screenshot_id:
            raise ValueError(f"Expected a non-empty value for `screenshot_id` but received {screenshot_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/executions/{execution_id}/screenshots/{screenshot_id}",
                execution_id=execution_id,
                screenshot_id=screenshot_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ScreenshotsResourceWithRawResponse:
    def __init__(self, screenshots: ScreenshotsResource) -> None:
        self._screenshots = screenshots

        self.retrieve = to_raw_response_wrapper(
            screenshots.retrieve,
        )


class AsyncScreenshotsResourceWithRawResponse:
    def __init__(self, screenshots: AsyncScreenshotsResource) -> None:
        self._screenshots = screenshots

        self.retrieve = async_to_raw_response_wrapper(
            screenshots.retrieve,
        )


class ScreenshotsResourceWithStreamingResponse:
    def __init__(self, screenshots: ScreenshotsResource) -> None:
        self._screenshots = screenshots

        self.retrieve = to_streamed_response_wrapper(
            screenshots.retrieve,
        )


class AsyncScreenshotsResourceWithStreamingResponse:
    def __init__(self, screenshots: AsyncScreenshotsResource) -> None:
        self._screenshots = screenshots

        self.retrieve = async_to_streamed_response_wrapper(
            screenshots.retrieve,
        )
